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
gen_year_sal = df.filter(['h12_g3','h12_g4', 'p1202_8aq1'])
print(gen_year_sal)
print('-' * 30)

df_gen_year_sal = gen_year_sal.rename(columns={'h12_g3':'성별',
                                               'h12_g4':'출생년도',
                                               'p1202_8aq1':'급여'})
print(df_gen_year_sal)
print('-' * 30)

df_gen_year_sal['성별'] = numpy.where(df_gen_year_sal['성별']==1, '남자', '여자')
df_gen_year_sal['연령대'] = (dt.datetime.now().year - df_gen_year['출생년도'] + 1) // 10 * 10
print(df_gen_year_sal)
print('-' * 30)

print(df_gen_year_sal.isna().sum())
print('-' * 30)

df_gen_year_sal.dropna(inplace=True)
print(df_gen_year_sal.isna().sum())
print('-' * 30)

df_gen_year_sal_mean = df_gen_year_sal.groupby(['성별', '연령대'], as_index=False).mean()
print(df_gen_year_sal_mean)
print('-' * 30)

pv_gen_year_sal_mean = df_gen_year_sal_mean.pivot('연령대', '성별', '급여')
print(pv_gen_year_sal_mean)
print('-' * 30)

index_after = {}
for i in list(pv_gen_year_sal_mean.index):
    index_after[i] = '%d대' %i
    
pv_gen_year_sal_mean.rename(index=index_after, inplace=True)
print(pv_gen_year_sal_mean)
print('-' * 30)


pv_gen_year_sal_mean.plot()
pyplot.title('성별과 연령대에 따른 평균 급여')
pyplot.grid()
pyplot.xlabel('연령대')
pyplot.ylabel('급여(만원)')

pyplot.savefig('exam6.png', dpi=100) # 그래프 파일에 저장
pyplot.show()



