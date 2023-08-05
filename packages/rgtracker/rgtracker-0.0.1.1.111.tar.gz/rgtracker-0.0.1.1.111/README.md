## Redis Naming Convention

### Redis Key

TYPE:NAME:DIMENSION:ID:TIMESTAMP:METRIC  
__Example__ :
* JSON -> J::P:001::
* TS   -> TS:5MINUTES:S:001::UD

```python
@unique
class RedisNC(IntEnum):
    TYPE = 0,
    NAME = 1,
    DIMENSION = 2,
    RECORD_ID = 3,
    TS = 4,
    METRIC = 5
```

```python
@unique
class Type(Enum):
    STREAM = 'ST'
    HASH = 'H'
    JSON = 'J'
    INDEX = 'I'
    TIMESERIES = 'TS'
    BLOOM = 'B'
    SORTEDSET = 'SS'
    SET = 'S'
    LIST = 'L'
    CHANNEL = 'C'
    CMS = 'CMS'
    HLL = 'HLL'
```

```python
NAME = "custom_dev_choice"
```

```python
@unique
class Dimension(Enum):
    WEBSITE = 'W'
    SECTION = 'S'
    PAGE = 'P'
    DEVICE = 'D'
    AUDIO = 'A'
    VIDEO = 'V'
    PODCAST = 'PC'
    METRIC = 'M'
```

```python
ID = "unique_key_identifier" # hash
```

```python
TIMESTAMP = "timestamp_key" # int
```

```python
@unique
class Metric(Enum):
    PAGEVIEWS = 'PG'
    DEVICES = 'D'
    UNIQUE_DEVICES = 'UD'
```


### Redis JSON

__Website__ 
```json
{
    "id": "28be7111962bea2626e3dd6c71116b3111211119ae09", (string - hash)
    "name": "RTL", (string - uppercase)
    "last_visited": 17111562426214, (numeric - timestamp)
    "sections": [
        {
            "id": "c111c621111bbe062bd4410d5b625dd11193fd631118", (string - hash)
            "pretty_name": "actu/monde", (string) -TODO-> "name": "actu/monde"
            "last_visited": 1711141110111125, (numeric - timestamp)
        }
    ], (tracker Section object)
    "pages": [
        {
            "id": "f0362c3463d7e27111db1f3111e9a4d111628a5eebd", (string - hash)
            "url": "https://5minutes.rtl.lu/actu/monde/a/111111134.html", (string - url without query params)
            "article_id": 111111134, (numeric)
            "last_visited": 1711141110111125, (numeric - timestamp)
        }
    ] (tracker Page object)
}
```

__Section__ 
```json
{
    "id": "", (string - hash)
    "pretty_name": "", (string)
    "level_0": "", (string) -> "levels": {"level_0": "", "level_n": "n"}
    "level_1": "", (string)
    "level_2": "", (string)
    "level_3": "", (string)
    "level_4": "", (string)
    "last_visited": 1711156271111112, (numeric - timestamp)
    "website": {
        "id": "", (string - hash)
        "name": "", (string)
    },
    "pages": [
        {
            "id": "f0362c3463d7e27111db1f3111e9a4d111628a5eebd", (string - hash)
            "url": "https://5minutes.rtl.lu/actu/monde/a/111111134.html", (string - url without query params)
            "article_id": 111111134, (numeric)
            "last_visited": 1711141110111125, (numeric - timestamp)
        }
    ]
}
```

__Page__ 
```json
{
    "id": "", (string - hash)
    "url": "", (string - url without query params)
    "article_id": "", (numeric)
    "last_visited": 17111626236220, (numeric, timestamp)
    "metadata": {
        "title": "", (string)
        "kicker": "", (string)
        "display_data": 17111626236220
    },
    "website": {
        "id": "",
        "name": ""
    },
    "section": {
        "id": "", (string - hash)
        "pretty_name": "", (string) -TODO-> "name": "" (string)
        "levels": {
            "level_0": "", (string)
            "level_1": "", (string)
            "level_2": "", (string)
            "level_3": "", (string)
            "level_4": "", (string)
        }
    }
}
```



### Redis Index

__Website__ on prefix = J::W: on JSON  
   - id TAG as id,  
   - name TAG as name,  
   - last_visited NUMERIC as last_visited, -TODO-> last_visited NUMERIC as last_visited SORTABLE true,  
   - sections[*].id TAG as section_id,  
   - sections[*].pretty_name TAG as section_pretty_name, -TODO-> sections[*].name TAG as section_name,  
   - pages[*].id TAG as page_id  


__Section__ on prefix = J::S: on JSON  
   - id TAG as id,  
   - pretty_name TAG as pretty_name SEPARATOR '/', -TODO-> name TAG as name SEPARATOR '/',  
   - level_0 TAG as level_0, -TODO-> levels.level_0 TAG as level_0  
   - level_1 TAG as level_1,  
   - level_2 TAG as level_2,  
   - level_3 TAG as level_3,  
   - level_4 TAG as level_4,  
   - last_visited NUMERIC as last_vistited SORTABLE true  
   - website.id TAG as website_id,  
   - website.name TAG as website_name  


__Page__ on prefix = J::P: on JSON  
   - id TAG as id,  
   - url TEXT as url,  
   - metadata.title TEXT as title,  
   - metadata.kicker TEXT as kicker,  
   - last_visited NUMERIC as last_visited,  
   - website.id TAG as website_id,  
   - website.name TAG as website_name,  
   - section.id TAG as section_id,  
   - section.pretty_name TAG as section_pretty_name SEPARATOR '/',  
   - section.levels.level_0 TAG as section_level_0,  
   - section.levels.level_1 TAG as section_level_1,  
   - section.levels.level_2 TAG as section_level_2,  
   - section.levels.level_3 TAG as section_level_3,  
   - section.levels.level_4 TAG as section_level_4  


### Redis TimeSeries

__Website__  
   - ts_name: 5MINUTES, 10MINUTES, etc.  
   - dimension: W, S, P  
   - M: PG, UD  
   - website_id: dbc111621119a62c7111fb1f62c362f2ad162646c2e, ...  
   - name: RTL, ...  


__Section__    
   - ts_name: 5MINUTES, 10MINUTES, etc.  
   - dimension: W, S, P  
   - M: PG, UD  
   - section_id: 46f3112311146f1117a1119e4dbeb63f14a162e1111a, ...  
   - pretty_name: meenung/carte-blanche, ...  -TODO-> section_name: meenung/carte-blanche
   - website_id: dbc111621119a62c7111fb1f62c362f2ad162646c2e, ...  
   - website_name: RTL, ...  


__Page__  
   - ts_name: 5MINUTES, 10MINUTES, etc.  
   - dimension: W, S, P   
   - M: PG, UD  
   - page_id: 6271112b62cd179ca7afa1eebc711171114ed2bff111, ...  
   - website_id: dbc111621119a62c7111fb1f62c362f2ad162646c2e, ...  
   - website_name: RTL, ...  
   - section_id: 46f3112311146f1117a1119e4dbeb63f14a162e1111a, ...  
   - section_pretty_name: meenung/carte-blanche, ...   -TODO-> section_name: meenung/carte-blanche


## Pythonic Redis Backend

### Build Python project
change version in pyproject.toml
delete /dist files
python3 -m build

### Upload Python package
python3 -m twine upload --repository testpypi dist/*
python3 -m twine upload dist/*

### Update Local Python Package
pip install rgtracker==0.0.1.1.111

##  Run RedisGears Jobs
python src/jobs/produce.py
python src/jobs/create_requirements.py

gears-cli run --host localhost --port 6379 src/jobs/bigbang.py REQUIREMENTS rgtracker==0.0.1.1.111
gears-cli run --host localhost --port 6379 src/jobs/bigbang.py REQUIREMENTS rgtracker==0.0.1.1.111 pandas requests

gears-cli run --host localhost --port 6379 src/jobs/rotate_pageviews/rotate_pg_website.py REQUIREMENTS rgtracker==0.0.1.1.111 pandas  
gears-cli run --host localhost --port 6379 src/jobs/rotate_pageviews/rotate_pg_section.py REQUIREMENTS rgtracker==0.0.1.1.111 pandas  
gears-cli run --host localhost --port 6379 src/jobs/rotate_pageviews/rotate_pg_page.py REQUIREMENTS rgtracker==0.0.1.1.111 pandas  

gears-cli run --host localhost --port 6379 src/jobs/rotate_unique_devices/rotate_ud_website.py REQUIREMENTS rgtracker==0.0.1.1.111 pandas  
gears-cli run --host localhost --port 6379 src/jobs/rotate_unique_devices/rotate_ud_section.py REQUIREMENTS rgtracker==0.0.1.1.111 pandas  
gears-cli run --host localhost --port 6379 src/jobs/rotate_unique_devices/rotate_ud_page.py REQUIREMENTS rgtracker==0.0.1.1.111 pandas  

gears-cli run --host localhost --port 6379 src/jobs/enrich.py REQUIREMENTS rgtracker==0.0.1.1.111 pandas requests

### Notes
https://stackoverflow.com/questions/2211111162/how-to-apply-hyperloglog-to-a-timeseries-stream  
https://redis.com/blog/7-redis-worst-practices/  
https://redis.com/blog/streaming-analytics-with-probabilistic-data-structures/  
https://findwork.dev/blog/advanced-usage-python-requests-timeouts-retries-hooks/  
https://www.peterbe.com/plog/best-practice-with-retries-with-requests  