from rgtracker.common import *
import math
import pandas as pd
from redisgears import executeCommand as execute
from redisgears import log


def extract(record, dimension):
    return record['value']['dimension'] == dimension


def transform(records, number_of_rotated_keys):
    # tracker_log(f'Transform.input {records.get("key")} {len(records.get("value"))} {records.get("value")}', f'RotateUD-1to5-W - ')

    df = pd.DataFrame(records.get("value"))
    df_sort = df.drop_duplicates('ts').sort_values('ts')


    expected_rows = number_of_rotated_keys
    chunks = math.floor(len(df_sort['ts']) / expected_rows + 1)
    i = 0
    j = expected_rows
    results = {

        'merge': [],
        'reinject': []
    }
    for x in range(chunks):
        df_sliced = df_sort[i:j]
        if df_sliced.shape[0] >= number_of_rotated_keys:
            results.get('merge').append({
                'id': df_sliced["id"].iloc[0],
                'name': create_key_name(
                    Type.HLL.value,
                    '',
                    df_sliced["dimension"].iloc[0],
                    df_sliced["id"].iloc[0],
                    get_ts_df(df_sliced["ts"].iloc[0], df_sliced["ts"]),
                    Metric.UNIQUE_DEVICES.value
                ),
                'keys': [create_key_name(Type.HLL.value, '', row[0], row[2], row[1], Metric.UNIQUE_DEVICES.value) for
                         row in
                         zip(df_sliced['dimension'], df_sliced['ts'], df_sliced['id'])]
            })
        else:
            [results.get('reinject').append({
                'key': create_key_name(
                    Type.HLL.value,
                    '',
                    row[0],
                    row[2],
                    row[1],
                    Metric.UNIQUE_DEVICES.value
                ),
                'dimension': row[0],
                'ts': row[1],
                'id': row[2]
            }) for row in zip(df_sliced['dimension'], df_sliced['ts'], df_sliced['id'])]

        i += expected_rows
        j += expected_rows

    # tracker_log(f'Transform.output {results}', f'RotateUD-1to5-W - ')
    return results


def load(job_name, records, dimension, write_to_ts, timeseries_name, key_expire_duration_sc, reinject_stream_name,
         output_stream_name):
    def get_ts(ts):
        if len(ts.split('_')) > 1:
            return ts.split("_")[-1]
        else:
            return ts

    # tracker_log(f'Load.input {records}', f'RotateUD-1to5-W - ')

    capped_stream = get_maxlen_capped_stream(timeseries_name, dimension)

    # tracker_log(f'UD - MAXLEN {type(capped_stream)} {capped_stream}')

    for hll_reinject in records.get('reinject'):
        execute('XADD', reinject_stream_name, 'MAXLEN', f'{capped_stream}', '*',
                'id', hll_reinject.get('id'),
                'dimension', hll_reinject.get('dimension'),
                'ts', hll_reinject.get('ts'),
                'merged_key', hll_reinject.get('key'))
        tracker_log(f'Reinject {hll_reinject}', f'{job_name} - ')

    for hll_merge in records.get("merge"):
        if execute('EXISTS', hll_merge.get('name')) != 1:
            execute('PFMERGE', hll_merge.get('name'), *hll_merge.get('keys'))

            tracker_log(f'Merge {hll_merge}', f'{job_name} - ')

            parsed_key_name = parse_key_name(hll_merge.get('name'))

            if write_to_ts:
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
                    record_id=hll_merge.get('id'),
                    metric=Metric.UNIQUE_DEVICES.value)

                if dimension == Dimension.WEBSITE.value:
                    record_infos = execute('FT.SEARCH', index_name, f'@id:{{{hll_merge.get("id")}}}', 'RETURN', '3',
                                           'name', 'AS', 'website_name')
                    # tracker_log(f'Get {dimension} infos - {record_infos}', f'{job_name} ')
                    execute('TS.ADD', timeseries_key_name, get_ts(parsed_key_name.get('ts')), unique_devices,
                            'ON_DUPLICATE', 'LAST',
                            'LABELS', 'ts_name', timeseries_name,
                            'dimension', dimension, Dimension.METRIC.value, Metric.UNIQUE_DEVICES.value,
                            'website_id', hll_merge.get('id'), *record_infos[-1])
                    # tracker_log(f'Write to Timeseries {hll_merge.get("id")}->{timeseries_key_name}', f'{job_name} ')
                    tracker_log(f'Write {unique_devices} devices to {timeseries_key_name} at {get_ts(parsed_key_name.get("ts"))}', f'{job_name} - ')
                elif dimension == Dimension.SECTION.value:
                    record_infos = execute('FT.SEARCH', index_name, f'@id:{{{hll_merge.get("id")}}}', 'RETURN', '5',
                                           'name', 'AS', 'section_name', 'website_id', 'website_name')
                    # tracker_log(f'Get {dimension} infos - {record_infos}', f'{job_name} ')
                    execute('TS.ADD', timeseries_key_name, get_ts(parsed_key_name.get("ts")), unique_devices,
                            'ON_DUPLICATE', 'LAST',
                            'LABELS', 'ts_name', timeseries_name,
                            'dimension', dimension, Dimension.METRIC.value, Metric.UNIQUE_DEVICES.value,
                            'section_id', hll_merge.get('id'), *record_infos[-1])
                    # tracker_log(f'Write to Timeseries {hll_merge.get("id")}->{timeseries_key_name}', f'{job_name} ')
                elif dimension == Dimension.PAGE.value:
                    record_infos = execute('FT.SEARCH', index_name, f'@id:{{{hll_merge.get("id")}}}', 'RETURN', '5',
                                           'website_id', 'website_name', 'section_id', 'section_name', 'article_id')
                    # tracker_log(f'Get {dimension} infos - {record_infos}', f'{job_name} ')
                    execute('TS.ADD', timeseries_key_name, get_ts(parsed_key_name.get("ts")), unique_devices,
                            'ON_DUPLICATE', 'LAST',
                            'LABELS', 'ts_name', timeseries_name,
                            'dimension', dimension, Dimension.METRIC.value, Metric.UNIQUE_DEVICES.value,
                            'page_id', hll_merge.get('id'), *record_infos[-1])
                    # tracker_log(f'Write to Timeseries {hll_merge.get("id")}->{timeseries_key_name}', f'{job_name} ')

            execute('XADD', output_stream_name, 'MAXLEN', f'{capped_stream}', '*',
                    'dimension', dimension,
                    'id', hll_merge.get('id'),
                    'ts', parsed_key_name.get('ts'),
                    'merged_key', hll_merge.get('name'))

            execute('EXPIRE', hll_merge.get('name'), key_expire_duration_sc)
