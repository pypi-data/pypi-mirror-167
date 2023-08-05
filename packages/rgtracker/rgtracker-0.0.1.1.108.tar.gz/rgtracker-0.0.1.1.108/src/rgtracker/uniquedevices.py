from rgtracker.common import *
import math
import pandas as pd
from redisgears import executeCommand as execute
from redisgears import log


def extract(record, dimension):
    return record['value']['dimension'] == dimension


# Todo: Extract dimension from stream name
def transform(records, number_of_rotated_keys):
    # tracker_log(f'Transform.input {records.get("key")} {len(records.get("value"))} {records.get("value")}', f'RotateUD-1to5-W - ')

    df = pd.DataFrame(records)
    tracker_log(f'IDS: {df["ids"].values.tolist()}', 'RotateUD-1to5-W - ')
    df['ids'] = df['ids'].apply(lambda x: json.loads(x) if x.startswith('[') else x)

    aggs = {'ids': rotate_agg}
    grouped_df = df.groupby(['ts']).agg(aggs).sort_values('ts').reset_index()
    tracker_log(f'TS {grouped_df["ts"].values.tolist()}', 'RotateUD-1to5-W - ')

    expected_rows = number_of_rotated_keys
    chunks = math.floor(len(grouped_df['ts']) / expected_rows + 1)
    i = 0
    j = expected_rows

    results = {
        'ids': [],
        'merge': [],
        'reinject': []
    }
    for x in range(chunks):
        df_sliced = grouped_df[i:j]
        if df_sliced.shape[0] >= number_of_rotated_keys:

            ids = [id for id in df_sliced['ids']]
            unique_ids = {x for l in ids for x in l}
            tracker_log(f'UNIQUE_IDS: {unique_ids}', 'RotateUD-1to5-W - ')
            for unique_ids in unique_ids:
                results.get('ids').append(unique_ids)

            results.get('merge').append({
                'name': create_key_name(
                    Type.HLL.value,
                    '',
                    'W',
                    '',
                    get_ts_df(df_sliced["ts"].iloc[0], df_sliced["ts"]),
                    Metric.UNIQUE_DEVICES.value
                ),
                'keys': [create_key_name(Type.HLL.value, '', 'W', '', ts, Metric.UNIQUE_DEVICES.value) for ts in
                         df_sliced['ts']]
            })
        else:
            [results.get('reinject').append({
                'ts': row[1],
                'ids': row[0]
            }) for row in zip(df_sliced['ids'], df_sliced['ts'])]

        i += expected_rows
        j += expected_rows

    return results


def load(job_name, records, dimension, write_to_ts, timeseries_name, key_expire_duration_sc, reinject_stream_name,
         output_stream_name):
    def get_ts(ts):
        if len(ts.split('_')) > 1:
            return ts.split("_")[-1]
        else:
            return ts

    # tracker_log(f'Load.input {records}', f'RotateUD-1to5-W - ')

    tracker_log(f'Load: {records}', f'{job_name} - ')

    capped_stream = get_maxlen_capped_stream(timeseries_name, dimension)

    # tracker_log(f'UD - MAXLEN {type(capped_stream)} {capped_stream}')

    for hll_reinject in records.get('reinject'):
        execute('XADD', reinject_stream_name, 'MAXLEN', f'{capped_stream}', '*',
                'ts', hll_reinject.get('ts'),
                'status', 'reinject',
                'ids', hll_reinject.get('ids'))
        # tracker_log(f'Reinject {hll_reinject}', f'{job_name} - ')

    for hll_merge in records.get("merge"):
        if execute('EXISTS', hll_merge.get('name')) != 1:
            execute('PFMERGE', hll_merge.get('name'), *hll_merge.get('keys'))

            tracker_log(f'Merge {hll_merge}', f'{job_name} - ')

            parsed_key_name = parse_key_name(hll_merge.get('name'))

            if write_to_ts:
                for id in records.get('ids'):
                    unique_devices = execute('PFCOUNT', *hll_merge.get('keys'))
                    index_name = create_key_name(
                        type=Type.INDEX.value,
                        name='',
                        dimension=dimension,
                        record_id='',
                        ts='',
                        metric='')
                    timeseries_key_name = create_key_name(
                        type=Type.TIMESERIES.value,
                        name=timeseries_name,
                        dimension=dimension,
                        record_id=id,
                        metric=Metric.UNIQUE_DEVICES.value)

                    if dimension == Dimension.WEBSITE.value:
                        record_infos = execute('FT.SEARCH', index_name, f'@id:{{{id}}}', 'RETURN', '3',
                                               'name', 'AS', 'website_name')
                        # tracker_log(f'Get {dimension} infos - {record_infos}', f'{job_name} ')
                        execute('TS.ADD', timeseries_key_name, get_ts(parsed_key_name.get('ts')), unique_devices,
                                'ON_DUPLICATE', 'LAST',
                                'LABELS', 'ts_name', timeseries_name,
                                'dimension', dimension, Dimension.METRIC.value, Metric.UNIQUE_DEVICES.value,
                                'website_id', id, *record_infos[-1])
                        tracker_log(f'Write {unique_devices} devices to {timeseries_key_name} at {get_ts(parsed_key_name.get("ts"))}', f'{job_name} - ')
                    elif dimension == Dimension.SECTION.value:
                        record_infos = execute('FT.SEARCH', index_name, f'@id:{{{id}}}', 'RETURN', '5',
                                               'name', 'AS', 'section_name', 'website_id', 'website_name')
                        # tracker_log(f'Get {dimension} infos - {record_infos}', f'{job_name} ')
                        execute('TS.ADD', timeseries_key_name, get_ts(parsed_key_name.get("ts")), unique_devices,
                                'ON_DUPLICATE', 'LAST',
                                'LABELS', 'ts_name', timeseries_name,
                                'dimension', dimension, Dimension.METRIC.value, Metric.UNIQUE_DEVICES.value,
                                'section_id', id, *record_infos[-1])
                        # tracker_log(f'Write to Timeseries {id}->{timeseries_key_name}', f'{job_name} ')
                    elif dimension == Dimension.PAGE.value:
                        record_infos = execute('FT.SEARCH', index_name, f'@id:{{{id}}}', 'RETURN', '5',
                                               'website_id', 'website_name', 'section_id', 'section_name', 'article_id')
                        # tracker_log(f'Get {dimension} infos - {record_infos}', f'{job_name} ')
                        execute('TS.ADD', timeseries_key_name, get_ts(parsed_key_name.get("ts")), unique_devices,
                                'ON_DUPLICATE', 'LAST',
                                'LABELS', 'ts_name', timeseries_name,
                                'dimension', dimension, Dimension.METRIC.value, Metric.UNIQUE_DEVICES.value,
                                'page_id', id, *record_infos[-1])
                        # tracker_log(f'Write to Timeseries {id}->{timeseries_key_name}', f'{job_name} ')

            execute('XADD', output_stream_name, 'MAXLEN', f'{capped_stream}', '*',
                    'ts', parsed_key_name.get('ts'),
                    'ids', hll_merge.get('ids'))

            execute('EXPIRE', hll_merge.get('name'), key_expire_duration_sc)
