import numpy
import pandas as pd
from pandas import DataFrame
from pandas import ExcelFile
from matplotlib import pyplot
import datetime as dt
'''
xlsx = ExcelFile('data/dataset2017.xlsx')
df = xlsx.parse(xlsx.sheet_names[0])
print(df)
print('-' * 30)
'''

year_sal = df.filter(['h12_g4', 'p1202_8aq1'])
print(year_sal)
print('-' * 30)

df_year_sal = year_sal.rename(columns={'h12_g4':'출생년도', 'p1202_8aq1':'월급'})
print(df_year_sal)
print('-' * 30)

yy = dt.datetime.now().year
print(yy)
print('-' * 30)

df_year_sal['나이'] = yy - df_year_sal['출생년도'] + 1
print(df_year_sal)
print('-' * 30)

print(df_year_sal.isna().sum())
print('-' * 30)

df_year_sal.dropna(inplace=True)
print(df_year_sal.isna().sum())
print('-' * 30)

df_year_sal['월급'] = numpy.where(((df_year_sal['월급']<1) | (df_year_sal['월급']>9998)), 
                               numpy.nan, df_year_sal['월급'])
print(df_year_sal.isna().sum())
print('-' * 30)

df_year_sal.dropna(inplace=True)
print(df_year_sal.isna().sum())
print('-' * 30)

print(df_year_sal)
print('-' * 30)

df_year_sal_mean = df_year_sal.filter(['나이', '월급']).groupby('나이').mean()
print(df_year_sal_mean)
print('-' * 30)

# 그래프 기본설정
pyplot.rcParams['font.family']='Malgun Gothic'      # 한글 폰트 설
pyplot.rcParams['font.size']=16                   # 글자 크기 설정
pyplot.rcParams['figure.figsize']=(12,8)             # 그래프의 가로, 세로크기(inch)

df_year_sal_mean.plot()
pyplot.title('나이에 따른 평균 월급 변화')
pyplot.grid()
pyplot.xlabel('나이')
pyplot.ylabel('평균월급')
pyplot.show()




'''
       h12_g4  p1202_8aq1
0        1936         NaN
1        1945         NaN
2        1948         NaN
3        1942       108.9
4        1923         NaN
      ...         ...
15417    1967         NaN
15418    1992         NaN
15419    1995        72.0
15420    1998         NaN
15421    2001         NaN

[15422 rows x 2 columns]
------------------------------
       출생년도     월급
0      1936    NaN
1      1945    NaN
2      1948    NaN
3      1942  108.9
4      1923    NaN
    ...    ...
15417  1967    NaN
15418  1992    NaN
15419  1995   72.0
15420  1998    NaN
15421  2001    NaN

[15422 rows x 2 columns]
------------------------------
2020
------------------------------
       출생년도     월급  나이
0      1936    NaN  85
1      1945    NaN  76
2      1948    NaN  73
3      1942  108.9  79
4      1923    NaN  98
    ...    ...  ..
15417  1967    NaN  54
15418  1992    NaN  29
15419  1995   72.0  26
15420  1998    NaN  23
15421  2001    NaN  20

[15422 rows x 3 columns]
------------------------------
출생년도        0
월급      10915
나이          0
dtype: int64
------------------------------
출생년도    0
월급      0
나이      0
dtype: int64
------------------------------
출생년도     0
월급      14
나이       0
dtype: int64
------------------------------
출생년도    0
월급      0
나이      0
dtype: int64
------------------------------
       출생년도     월급  나이
3      1942  108.9  79
10     1940   20.0  81
16     1978  322.0  43
17     1975  120.0  46
24     1975  300.0  46
    ...    ...  ..
15400  1966  230.0  55
15401  1962  138.0  59
15404  1993  286.0  28
15412  1956  179.0  65
15419  1995   72.0  26

[4493 rows x 3 columns]
------------------------------
            월급
나이            
23   89.333333
24  136.720000
25  140.807692
26  138.000000
27  145.652000
..         ...
89   21.200000
90   25.000000
91   20.000000
93   20.000000
94   20.000000

[71 rows x 1 columns]
------------------------------
'''