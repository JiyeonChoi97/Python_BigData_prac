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

df_year_sal['연령대'] = (dt.datetime.now().year - df_year['출생년도'] + 1) // 10 * 10
print(df_year_sal)
print('-' * 30)

print(df_year_sal.isna().sum())
print('-' * 30)

df_year_sal.dropna(inplace=True)
print(df_year_sal.isna().sum())
print('-' * 30)

# 평균 급여 계산
df_year_sal_mean = df_year_sal.filter(['연령대', '월급']).groupby('연령대').mean()
print(df_year_sal_mean)
print('-' * 30)

index_after = {}
for i in list(df_year_sal_mean.index):
    index_after[i] = '%d대' %i
    
df_year_sal_mean.rename(index=index_after, inplace=True)
print(df_year_sal_mean)
print('-' * 30)

df_year_sal_mean.plot(marker='o')
pyplot.title('연령대별 평균급여 변화')
pyplot.grid()
pyplot.xlabel('연령대')
pyplot.ylabel('만원')

for i, v in enumerate(list(df_year_sal_mean['월급'])):
    txt = '%d만원' %v
    pyplot.text(i, v, txt, fontsize=14, color='blue',
                 horizontalalignment='center',
                 verticalalignment='bottom')
    
pyplot.savefig('exam5.png', dpi=100) # 그래프 파일에 저장

pyplot.show()


