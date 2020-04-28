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
gen_year = df.filter(['h12_g3','h12_g4'])
print(gen_year)
print('-' * 30)

df_gen_year = gen_year.rename(columns={'h12_g3':'성별', 'h12_g4':'출생년도'})
df_gen_year['성별'] = numpy.where(df_gen_year['성별']==1, '남자', '여자')
print(df_gen_year)
print('-' * 30)

df_gen_year['연령대'] = (dt.datetime.now().year - df_gen_year['출생년도'] + 1) // 10 * 10
print(df_gen_year)
print('-' * 30)

print(df_gen_year.isna().sum())
print('-' * 30)


df_age_gen_count = df_gen_year.groupby(['성별', '연령대'], as_index=False).count()
print(df_age_gen_count)
print('-' * 30)

df_age_gen = df_age_gen_count.rename(columns={'출생년도':'명'})
print(df_age_gen)
print('-' * 30)

pv_age_gen = df_age_gen.pivot('연령대', '성별', '명')
print(pv_age_gen)
print('-' * 30)

index_after = {}
for i in list(pv_age_gen.index):
    index_after[i] = '%d대' %i
    
pv_age_gen.rename(index=index_after, inplace=True)
print(pv_age_gen)
print('-' * 30)


pv_age_gen.plot.bar(rot=0)
pyplot.title('성별과 연령대별 분포')
pyplot.grid()
pyplot.xlabel('연령대')
pyplot.ylabel('명')

pyplot.savefig('prac2.png', dpi=100) # 그래프 파일에 저장
pyplot.show()
