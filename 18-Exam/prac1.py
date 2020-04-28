import numpy
import pandas as pd
from pandas import DataFrame
from pandas import ExcelFile
from matplotlib import pyplot
'''
xlsx = ExcelFile('data/dataset2017.xlsx')
df = xlsx.parse(xlsx.sheet_names[0])
'''
gen_sal = df.filter(['h12_g3', 'p1202_8aq1'])
print(gen_sal)
print('-' * 30)

df_gen_sal = gen_sal.rename(columns={'h12_g3':'성별', 'p1202_8aq1':'월급'})
df_gen_sal['성별'] = numpy.where(df_gen_sal['성별']==1, '남자', '여자')
print(df_gen_sal)
print('-' * 30)

print(df_gen_sal.isna().sum())
print('-' * 30)

df_gen_sal.dropna(inplace=True)
print(df_gen_sal.isna().sum())
print('-' * 30)

df_gen_sal['월급'] = numpy.where(((df_gen_sal['월급']<1) | (df_gen_sal['월급']>9998)), 
                               numpy.nan, df_gen_sal['월급'])
print(df_gen_sal.isna().sum())
print('-' * 30)

df_gen_sal.dropna(inplace=True)
print(df_gen_sal.isna().sum())
print('-' * 30)

df_gen_sal_mean = df_gen_sal.groupby('성별').mean()
print(df_gen_sal_mean)
print('-' * 30)

# 그래프 기본설정
pyplot.rcParams['font.family']='Malgun Gothic'      # 한글 폰트 설
pyplot.rcParams['font.size']=16                   # 글자 크기 설정
pyplot.rcParams['figure.figsize']=(12,8)             # 그래프의 가로, 세로크기(inch)

df_gen_sal_mean.plot.bar(rot=0)
pyplot.title('성별에 따른 평균 월급 차이 분석')
pyplot.grid()
pyplot.xlabel('성별')
pyplot.ylabel('월급')

for i, v in enumerate(list(df_gen_sal_mean['월급'])):
    txt = '%d만원' %v
    pyplot.text(i, v, txt, fontsize=14, color='#000099',
                horizontalalignment='center', 
                verticalalignment='bottom')

pyplot.savefig('prac1.png', dpi=100) # 그래프 파일에 저장

pyplot.show()


'''
       h12_g3  p1202_8aq1
0           2         NaN
1           2         NaN
2           1         NaN
3           1       108.9
4           2         NaN
      ...         ...
15417       2         NaN
15418       2         NaN
15419       1        72.0
15420       2         NaN
15421       1         NaN

[15422 rows x 2 columns]
------------------------------
       성별     월급
0      여자    NaN
1      여자    NaN
2      남자    NaN
3      남자  108.9
4      여자    NaN
   ..    ...
15417  여자    NaN
15418  여자    NaN
15419  남자   72.0
15420  여자    NaN
15421  남자    NaN

[15422 rows x 2 columns]
------------------------------
성별        0
월급    10915
dtype: int64
------------------------------
성별    0
월급    0
dtype: int64
------------------------------
성별     0
월급    14
dtype: int64
------------------------------
성별    0
월급    0
dtype: int64
------------------------------
            월급
성별            
남자  333.422185
여자  176.359967
------------------------------
'''