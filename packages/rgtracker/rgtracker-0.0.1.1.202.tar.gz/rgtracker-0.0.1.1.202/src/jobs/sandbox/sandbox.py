import json
import math
import pandas as pd


GB("StreamReader"). \
    foreach(lambda record: log(f'Raw - {record}')). \
    filter(lambda record: record['value']['status'] != 'reinject'). \
    aggregate([],
              lambda a, r: a + [r['value']],
              lambda a, r: a + r). \
    foreach(lambda record: log(f'Agg - {record}')). \
    run('ST:1MINUTE:S:::PG', trimStream=False)


# GB("StreamReader"). \
#     foreach(lambda record: log(f'Raw - {record}')). \
#     aggregateby(lambda e: e['value']['ts'],
#                 [],
#                 lambda k, a, r: a + [r['value']],
#                 lambda k, a, r: a + r). \
#     foreach(lambda record: log(f'Agg - {record}')). \
#     run('ST:1MINUTE:W:::UD', trimStream=False)



# register(
# prefix=f'ST:1MINUTE:{dimension}:::PG',
# convertToStr=True,
# collect=True,
# onFailedPolicy='abort',
# onFailedRetryInterval=1,
# batch=1,
# duration=0,
# trimStream=False)

# run('ST:1MINUTE::::PG', trimStream=False)
