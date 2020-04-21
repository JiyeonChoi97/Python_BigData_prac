from pandas import DataFrame

# 딕셔너리를 원소로 갖는 리스트
grade_data = [
                {'국어':98, '영어':None, '수학':88, '과학':64},
                {'국어':88, '영어':90, '수학':62, '과학':72},
                {'국어':92, '영어':70, '수학':None, '과학':None},
                {'국어':63, '영어':60, '수학':31, '과학':70},
                {'국어':120, '영어':50, '수학':None, '과학':88}
             ]


# 딕셔너리의 키가 컬럼이름으로 사용되므로, 인덱스만 지정
df = DataFrame(grade_data, index=['철수', '영희', '민철', '수현', '호영'])
print(df)
print('-'*30)

# 1. 각 열별로 데이터 확인
print(df.dtypes)
print('-'*30)

# 2. 특정 열에 대한 타입과 값 확인
print(df['국어'])
print(type(df['국어']))
print('-'*30)

# 3. 특정 열의 값들을 읽기
arr = df['국어'].values
print(arr)
print(type(arr))
print('-'*30)

# 4. 열의 값들을 list로 변환
k_list = list(df['국어'])
print(k_list)
print(type(k_list))
print('-'*30)

'''
     국어    영어    수학    과학
철수   98   NaN  88.0  64.0
영희   88  90.0  62.0  72.0
민철   92  70.0   NaN   NaN
수현   63  60.0  31.0  70.0
호영  120  50.0   NaN  88.0
------------------------------
국어      int64
영어    float64
수학    float64
과학    float64
dtype: object
------------------------------
철수     98
영희     88
민철     92
수현     63
호영    120
Name: 국어, dtype: int64
<class 'pandas.core.series.Series'>
------------------------------
[ 98  88  92  63 120]
<class 'numpy.ndarray'>
------------------------------
[98, 88, 92, 63, 120]
<class 'list'>
------------------------------
'''

