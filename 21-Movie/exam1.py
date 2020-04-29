import requests
import json
import datetime as dt
import pandas as pd
from pandas import DataFrame
from matplotlib import pyplot

api_key = '8a767129db0b6a3e8014a13e0ef5cca7'

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'
session = requests.Session()
session.headers.update({'User_agent':user_agent, 'referer':None})

url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=430156241533f1d058c603178cc3ca0e&targetDt=20120101'

today = dt.datetime.now()
delta = dt.timedelta(days = -1)
yesterday = today + delta
yesterday_str = yesterday.strftime('%Y%m%d')
print(yesterday_str)
print('-' * 30)

api_url = url.format(key=api_key, date=yesterday_str)

r = session.get(api_url)

if r.status_code != 200:
    print('[Error]')
    quit()
    
print(r.text)
print('-' * 30)

daily_boxoffice_dict = json.loads(r.text)
df = DataFrame(daily_boxoffice_dict['boxOfficeResult']['dailyBoxOfficeList'])
print(df)
print('-' * 30)

'''
  rnum rank rankInten rankOldAndNew  ... audiChange  audiAcc scrnCnt showCnt
0    1    1         0           OLD  ...      -14.5  5328435     697    3223
1    2    2         1           OLD  ...       -9.7  1739543     588    2321
2    3    3        -1           OLD  ...        -17  1442861     360    1832
3    4    4         0           OLD  ...      -12.8   895416     396    1364
4    5    5         0           OLD  ...        -22   202909     290     838
5    6    6         1           OLD  ...      -20.4   171285     244     895
6    7    7        -1           OLD  ...      -26.1  2823060     243     839
7    8    8         0           OLD  ...      -24.3   285959     186     348
8    9    9         0           OLD  ...      -24.7   516289     169     359
9   10   10         0           OLD  ...      -26.9   235070     175     291

[10 rows x 18 columns]
'''