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

local_year = df.filter(['h12_g4', 'h12_reg7'])
print(local_year)
print('-' * 30)

df_local_year = local_year.rename(columns={'h12_g4':'출생년도',
                                           'h12_reg7':'지역코드'})
print(df_local_year)
print('-' * 30)

df_local_year['나이'] = (dt.datetime.now().year - df_local_year['출생년도'] + 1) 
print(df_local_year)
print('-' * 30)

df_local_year.drop('출생년도', axis=1, inplace=True)
print(df_local_year)
print('-' * 30)

df_localcode = DataFrame({'지역코드':list(range(1,8)),
                          '지역':['서울', '인천,경기', '부산,경남,울산', 
                                '대구,경북', '대전,충남', '강원,충북',
                                '광주,전남,전북,제주']})
print(df_localcode)
print('-' * 30)

df_local_age = pd.merge(df_local_year, df_localcode, how='outer')
print(df_local_age)
print('-' * 30)

df_local_age.drop('지역코드', axis=1, inplace=True)
print(df_local_age)
print('-' * 30)

conditions = [(df_local_age['나이']<30),
              (df_local_age['나이']<60),
              (df_local_age['나이']>=60)]

level = ['청년층', '중년충', '노년층']

df_local_age['연령층'] = numpy.select(conditions, level)
print(df_local_age)
print('-' * 30)

print(df_local_age.isna().sum())
print('-' * 30)

df_local_age_group = df_local_age.filter(['지역', '연령층', '나이'])\
                    .groupby(['지역', '연령층'], as_index=False).count()
print(df_local_age_group)
print('-' * 30)

df_local_age_group.rename(columns={'나이':'조사인원'}, inplace=True)
print(df_local_age_group)
print('-' * 30)

pv_local_age_group = df_local_age_group.pivot('지역','연령층', '조사인원')
print(pv_local_age_group)
print('-' * 30)

pv_local_age_group = pv_local_age_group.reindex(columns=['청년층', '중년층', '노년층'])
print(pv_local_age_group)
print('-' * 30)

pv_local_age_group.plot.bar(rot=0)
pyplot.title('지역별 연령층 분포')
pyplot.grid()
pyplot.xlabel('지역')
pyplot.ylabel('조사인원(명)')
pyplot.savefig('exam7_1.png', dpi=100) # 그래프 파일에 저장
pyplot.show()

fig = pyplot.figure(figsize=(30,20))
ax1 = fig.add_subplot(1,3,1)
ax2 = fig.add_subplot(1,3,2)
ax3 = fig.add_subplot(1,3,3)

pv_local_age_group['청년층'].plot.pie(ax = ax1, autopct = '%.1f%%',
                                   textprops={'color':'#000000'})

ax1.title.set_text('청년층')
ax1.set(ylabel=None)

pv_local_age_group['중년층'].plot.pie(ax = ax2, autopct = '%.1f%%',
                                   textprops={'color':'#000000'})

ax1.title.set_text('중년층')
ax1.set(ylabel=None)

pv_local_age_group['노년층'].plot.pie(ax = ax3, autopct = '%.1f%%',
                                   textprops={'color':'#000000'})

ax1.title.set_text('노년층')
ax1.set(ylabel=None)

pyplot.savefig('exam7_2.png', dpi=100) # 그래프 파일에 저장

pyplot.show()













