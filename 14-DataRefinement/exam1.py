from pandas import DataFrame
from matplotlib import pyplot
# 통게 기반 결측치 정제를 위한 클래스
from sklearn.impute import SimpleImputer
import numpy

# 데이터 생성
grade_dic = {
                '국어': [98, 88, 92, 63, 120],
                '영어': [None, 90, 70, 60, 50],
                '수학': [88, 62, None, 31, None],
                '과학': [64, 72, None, 70, 88]                
            }

df = DataFrame(grade_dic, index = ['철수', '영희', '민철', '수현', '호영'])
print(df)
print('-'*30)

# 각 데이터의 결측치 여부 확인
# isna()
# -> 각 열에 대해 결측치가 아닐 경우 False, 결측치는 True
df_na = df.isna()
print(df_na)
print('-'*30)

# 각 열별로 결측치 수 파악하기
# -> 데이터프레임의 열별로 합계를 수행하면 True = 1 , False = 0으로 계산
df_na_sum = df_na.sum()
print(df_na_sum)
print('-'*30)

'''
     국어    영어    수학    과학
철수   98   NaN  88.0  64.0
영희   88  90.0  62.0  72.0
민철   92  70.0   NaN   NaN
수현   63  60.0  31.0  70.0
호영  120  50.0   NaN  88.0
------------------------------
       국어     영어     수학     과학
철수  False   True  False  False
영희  False  False  False  False
민철  False  False   True   True
수현  False  False  False  False
호영  False  False   True  False
------------------------------
국어    0
영어    1
수학    2
과학    1
dtype: int64
------------------------------
'''














