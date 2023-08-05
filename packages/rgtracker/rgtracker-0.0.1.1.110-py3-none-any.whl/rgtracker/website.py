from rgtracker.common import *
import json
from dataclasses import dataclass, field
from datetime import datetime
from typing import ClassVar
from redisgears import executeCommand as execute
from redisgears import log


@dataclass
class Website:
    id: str
    name: str = None
    last_visited: str = None
    dimension_key: field(init=False) = None
    dimension_ts_key: field(init=False) = None
    metric_pageviews_key: field(init=False) = None
    metric_unique_device_key: field(init=False) = None
    cms_width: ClassVar[int] = 2000
    cms_depth: ClassVar[int] = 5

    def __post_init__(self):
        if len(self.last_visited.split('_')) > 1:
            self.dimension_key = f'{Type.JSON.value}::{Dimension.WEBSITE.value}:{self.id}::'
            self.dimension_ts_key = f'::{Dimension.WEBSITE.value}:{self.id}:{self.last_visited}:'
            self.metric_pageviews_key = f'{Type.CMS.value}::{Dimension.WEBSITE.value}::{self.last_visited}:{Metric.PAGEVIEWS.value}'
            self.metric_unique_device_key = f'{Type.HLL.value}::{Dimension.WEBSITE.value}:{self.id}:{self.last_visited}:{Metric.UNIQUE_DEVICES.value}'
            # log(f'__post_init__ len(last_visited) > 1  \n{self.dimension_key}\n{self.metric_pageviews_key}\n{self.metric_unique_device_key}')
        else:
            dt = datetime.fromtimestamp(int(self.last_visited) / 1000) if self.last_visited is not None else None
            rounded_last_visited = int(round_time(dt).timestamp() * 1000)
            # tracker_log(f'Rounded time: {dt} to {rounded_last_visited}', f'Website - ')
            self.dimension_key = f'{Type.JSON.value}::{Dimension.WEBSITE.value}:{self.id}::'
            self.dimension_ts_key = f'::{Dimension.WEBSITE.value}:{self.id}:{rounded_last_visited}:'
            self.metric_pageviews_key = f'{Type.CMS.value}::{Dimension.WEBSITE.value}::{rounded_last_visited}:{Metric.PAGEVIEWS.value}'
            self.metric_unique_device_key = f'{Type.HLL.value}::{Dimension.WEBSITE.value}:{self.id}:{rounded_last_visited}:{Metric.UNIQUE_DEVICES.value}'
            # log(f'__post_init__ len(last_visited) > 1  \n{self.dimension_key}\n{self.metric_pageviews_key}\n{self.metric_unique_device_key}')

    def create(self):
        execute('SADD', Dimension.WEBSITE.value, f'{self.id}:{self.name}')
        # log(f'SADD websites {self.name}:{self.id}')
        execute('JSON.SET', self.dimension_key, '.', json.dumps({
            'id': self.id,
            'name': self.name,
            'last_visited': self.last_visited,
            'sections': [],
            'pages': []
        }))
        # log(f'JSON.SET {self.dimension_key}')

    def create_metrics(self):
        try:
            execute('CMS.INITBYDIM', self.metric_pageviews_key, self.cms_width, self.cms_depth)
            # log(f'CMS.INITBYDIM {self.metric_pageviews_key} {self.cms_width} {self.cms_depth}')
        except Exception as e:
            # tracker_log(f'{e} - {self.metric_pageviews_key}', 'Website - ')
            pass

        try:
            execute('PFADD', self.metric_unique_device_key)
        except Exception as e:
            tracker_log(f'{e} - {self.metric_pageviews_key}', 'Website - ')
            pass

    def incr_metrics(self, page_id, device_id):
        # Fixme: increment by page_id
        execute('CMS.INCRBY', self.metric_pageviews_key, self.id, 1)
        # log(f'CMS.INCRBY {self.metric_pageviews_key} {self.id} {1}')
        execute('PFADD', self.metric_unique_device_key, device_id)
        # log(f'PFADD {self.metric_unique_device_key} {device_id}')

    def expire_metrics(self):
        # Todo: put expire in method params
        execute('EXPIRE', self.metric_pageviews_key, 3600)
        execute('EXPIRE', self.metric_unique_device_key, 3600)

    def is_exists(self):
        x = execute('EXISTS', self.dimension_key)
        # log(f'EXISTS {self.dimension_key} => {x}')
        return x

    def has_metrics(self):
        x = execute('EXISTS', self.metric_pageviews_key)
        # log(f'EXISTS {self.metric_pageviews_key} => {x}')
        z = execute('EXISTS', self.metric_unique_device_key)
        # log(f'EXISTS {self.metric_unique_device_key} => {z}')
        # return x + z
        return x

    def update_last_visited(self):
        execute('JSON.SET', self.dimension_key, '.last_visited', self.last_visited)
        # log(f'update_last_visited: JSON.SET {self.dimension_key} .last_visited {self.last_visited}')

    # Fixme: change method name
    def notification_of_active_websites(self, stream_names):
        parsed_key = parse_key_name(self.dimension_ts_key)

        current_ts = int(parsed_key.get("ts"))
        prev_unix_ts = int((datetime.fromtimestamp(current_ts / 1000) - timedelta(minutes=1)).timestamp() * 1000)

        ids_raw = execute('FT.SEARCH', 'I::W:::', f'@last_visited:[{prev_unix_ts} {current_ts}]', 'RETURN', '1', 'id')
        ids = []
        for d in ids_raw:
            if type(d) is list:
                ids.append(d[-1])

        tracker_log(f'Notification to Merger Services - [{prev_unix_ts} {current_ts}] active websites {ids}',
                    f'Website - ')
        execute('XADD', stream_names.get('website_pageviews'), 'MAXLEN', '8640', '*',
                'ts', parsed_key.get("ts"),
                'status', 'active',
                'ids', json.dumps(ids))
        execute('XADD', stream_names.get('website_unique_devices'), 'MAXLEN', '8640', '*',
                'ts', parsed_key.get("ts"),
                'status', 'active',
                'ids', json.dumps(ids))

    def notification_of_new_website(self, stream_names):
        parsed_key = parse_key_name(self.dimension_ts_key)
        tracker_log(f'Notification to Merger Services - [{parsed_key.get("ts")}] new website {self.id}', f'Website - ')
        execute('XADD', stream_names.get('website_pageviews'), 'MAXLEN', '8640', '*',
                'ts', parsed_key.get("ts"),
                'status', 'new',
                'ids', self.id)
        execute('XADD', stream_names.get('website_unique_devices'), 'MAXLEN', '8640', '*',
                'ts', parsed_key.get("ts"),
                'status', 'new',
                'ids', self.id)

    def send_to_enrich(self):
        execute('XADD', 'ST:ENRICH:W:::', 'MAXLEN', '10', '*', 'key', self.dimension_key)

    def log_new_website(self):
        tracker_log(f'NEW WEBSITE! {self.id} at {parse_key_name(self.dimension_ts_key).get("ts")}', f'Website - ')

    def log_new_minute(self):
        tracker_log(f'CLAP! {parse_key_name(self.dimension_ts_key).get("ts")}', f'Website - ')


def load_website(website, section, page, device, output_stream_names):
    if website.is_exists() != 1:
        # website.log_new_website()
        website.create()
        website.create_metrics()
        website.incr_metrics(page.id, device.id)
        website.expire_metrics()
        website.notification_of_new_website(stream_names=output_stream_names)
        website.send_to_enrich()
    else:
        if website.has_metrics() < 1:
            # website.log_new_minute()
            website.create_metrics()
            website.incr_metrics(page.id, device.id)
            website.expire_metrics()
            website.notification_of_active_websites(stream_names=output_stream_names)
            website.update_last_visited()
        else:
            website.incr_metrics(page.id, device.id)
            website.update_last_visited()
