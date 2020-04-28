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

year = df.filter(['h12_g4'])
print(year)
print('-' * 30)

df_year = year.rename(columns={'h12_g4':'출생년도'})
print(df_year)
print('-' * 30)

yy = dt.datetime.now().year     # 현재 년도

df_year['나이'] = yy - df_year['출생년도'] + 1
print(df_year)
print('-' * 30)

df_year['연령대'] = df_year['나이'] - (df_year['나이'] % 10)
print(df_year)
print('-' * 30)

print(df_year.isna().sum())
print('-' * 30)

vcount = df_year['연령대'].value_counts()
df_age_band = DataFrame(vcount)
print(df_age_band)
print('-' * 30)

df_age_band_sort = df_age_band.sort_index()
print(df_age_band_sort)
print('-' * 30)

index_after = {}
for i in list(df_age_band_sort.index):
    index_after[i] = "%d대" %i

df_age_band_sort.rename(index=index_after, inplace=True)
print(df_age_band_sort)
print('-' * 30)



# 그래프 기본설정
pyplot.rcParams['font.family']='Malgun Gothic'      # 한글 폰트 설
pyplot.rcParams['font.size']=16                   # 글자 크기 설정
pyplot.rcParams['figure.figsize']=(12,8)             # 그래프의 가로, 세로크기(inch)

df_age_band_sort.plot.bar()
pyplot.title('연령대 분포')
pyplot.grid()
pyplot.xlabel('연령대')
pyplot.ylabel('명')

for i, v in enumerate(list(df_age_band_sort['나이'])):
    txt = '%d명' %v
    pyplot.text(i, v, txt, fontsize=14, color='blue',
                 horizontalalignment='center',
                 verticalalignment='bottom')
    
pyplot.savefig('exam4.png', dpi=100) # 그래프 파일에 저장
pyplot.show()



