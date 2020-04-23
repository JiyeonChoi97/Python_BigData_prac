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

# 결측치를 각 열의 평균값으로 대체
simple_imp = SimpleImputer(missing_values=numpy.nan, strategy='mean') # 정제규칙 지정
print(simple_imp)
print('-'*30)

result_simple_imp = simple_imp.fit_transform(df.values)
print(result_simple_imp)
print('-'*30)

df_result = DataFrame(result_simple_imp, index=df.index, columns=df.columns)
print(df_result)
print('-'*30)

# 이상치 존재 여부 확인을 위해 상자 그림 표시 

# 그래프 기본설정
pyplot.rcParams['font.family']='Malgun Gothic'        # 한글 폰트 설
pyplot.rcParams['font.size']=16                       # 글자 크기 설정
pyplot.rcParams['figure.figsize']=(10, 6)             # 그래프의 가로, 세로크기(inch)

# 상자 그림 출력
df_result.boxplot();
pyplot.savefig('exam4_file.png', dpi=100) # 그래프 파일에 저장
pyplot.show()
print('-'*30)

# 이상치를 결측치로 변경하기
# 국어점수에 대한 이상치 필터링
df_outlier = df_result.query('국어>100')
print(df_outlier)
print('-'*30)

# 필터링 된 이상치 데이터에 대한 인덱스 추출
outlier_index = list(df_outlier.index)
print(outlier_index)
print('-'*30)

# 이상치를 갖는 인덱스에 대한 국어점
for i in outlier_index:
    df_result.loc[i, '국어'] = numpy.nan

print(df_result)
print('-'*30)

# 변경된 결측치 정제
# 결측치에 대해 평균점수 부여
result_simple_imp1 = simple_imp.fit_transform(df_result.values)
print(result_simple_imp1)
print('-'*30)

# 정제된 결과로 데이터프레임 생성
df1_result = DataFrame(result_simple_imp1, index=df_result.index,
                       columns=df_result.columns)
print(df1_result)
print('-'*30)

'''
     국어    영어    수학    과학
철수   98   NaN  88.0  64.0
영희   88  90.0  62.0  72.0
민철   92  70.0   NaN   NaN
수현   63  60.0  31.0  70.0
호영  120  50.0   NaN  88.0
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
       국어    영어         수학    과학
철수   98.0  67.5  88.000000  64.0
영희   88.0  90.0  62.000000  72.0
민철   92.0  70.0  60.333333  73.5
수현   63.0  60.0  31.000000  70.0
호영  120.0  50.0  60.333333  88.0
------------------------------
       국어    영어         수학    과학
호영  120.0  50.0  60.333333  88.0
------------------------------
['호영']
------------------------------
      국어    영어         수학    과학
철수  98.0  67.5  88.000000  64.0
영희  88.0  90.0  62.000000  72.0
민철  92.0  70.0  60.333333  73.5
수현  63.0  60.0  31.000000  70.0
호영   NaN  50.0  60.333333  88.0
------------------------------
[[98.         67.5        88.         64.        ]
 [88.         90.         62.         72.        ]
 [92.         70.         60.33333333 73.5       ]
 [63.         60.         31.         70.        ]
 [85.25       50.         60.33333333 88.        ]]
------------------------------
       국어    영어         수학    과학
철수  98.00  67.5  88.000000  64.0
영희  88.00  90.0  62.000000  72.0
민철  92.00  70.0  60.333333  73.5
수현  63.00  60.0  31.000000  70.0
호영  85.25  50.0  60.333333  88.0
------------------------------
'''