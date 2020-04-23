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

# 대표값으로 대체하기
df_fillna = df.fillna(value=50)
print(df_fillna)
print('-'*30)

# 통계분석 기법으로 대체하기
# -> 결측치를 정제할 규칙 정의
# -> strategy 옵션 : mean=평균, median=중앙값, most_frequent:최빈값

# SimpleImputer 객체
# -> 각 열단위로 평균을 결측치에 지정
simple_imp = SimpleImputer(missing_values=numpy.nan, strategy='mean') # 정제규칙 지정
print(simple_imp)
print('-'*30)

result_simple_imp = simple_imp.fit_transform(df.values)
print(result_simple_imp)
print('-'*30)

# df의 평균값 확인
print(df.mean())
print('-'*30)

# 적용된 규칙으로 새로운 데이터프레임 생성
df_result = DataFrame(result_simple_imp, index=df.index, columns=df.columns)
print(df_result)
print('-'*30)

'''
     국어    영어    수학    과학
철수   98   NaN  88.0  64.0
영희   88  90.0  62.0  72.0
민철   92  70.0   NaN   NaN
수현   63  60.0  31.0  70.0
호영  120  50.0   NaN  88.0
------------------------------
     국어    영어    수학    과학
철수   98  50.0  88.0  64.0
영희   88  90.0  62.0  72.0
민철   92  70.0  50.0  50.0
수현   63  60.0  31.0  70.0
호영  120  50.0  50.0  88.0
------------------------------
SimpleImputer(add_indicator=False, copy=True, fill_value=None,
              missing_values=nan, strategy='mean', verbose=0)
------------------------------
[[ 98.          67.5         88.          64.        ]
 [ 88.          90.          62.          72.        ]
 [ 92.          70.          60.33333333  73.5       ]
 [ 63.          60.          31.          70.        ]
 [120.          50.          60.33333333  88.        ]]
------------------------------
국어    92.200000
영어    67.500000
수학    60.333333
과학    73.500000
dtype: float64
------------------------------
       국어    영어         수학    과학
철수   98.0  67.5  88.000000  64.0
영희   88.0  90.0  62.000000  72.0
민철   92.0  70.0  60.333333  73.5
수현   63.0  60.0  31.000000  70.0
호영  120.0  50.0  60.333333  88.0
------------------------------
'''