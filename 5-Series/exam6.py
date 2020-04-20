from pandas import date_range
from pandas import Series

# 데이터 생성
s1 = date_range(start='2020-01-01', end='2020-01-05') # 1일씩 증가 

week1 = Series([10, 20, 30, 40, 50], index=s1)
print(week1)

'''
2020-01-01    10
2020-01-02    20
2020-01-03    30
2020-01-04    40
2020-01-05    50
Freq: D, dtype: int64
'''
