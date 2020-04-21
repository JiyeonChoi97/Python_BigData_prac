from pandas import DataFrame
from pandas import Series
import numpy
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

# 1. 리스트를 활용한 열 추가
df['한국사'] = [92, 83, 72, None, 80]
print(df)
print('-'*30)

# 2. 단일값 추가
df['세계사'] = 100
print(df)
print('-'*30)

# 3. Series를 통한 열 추가
# -> 데이터의 객수가 일치하지 않으면, 빈곳에는 'NaN'이 저장
df['사회'] = Series([82, 90, 92, 64], index = ['철수', '영희', '민철', '수현'])
print(df)
print('-'*30)

df['사회1'] = Series([82, 90, 92, 64])
print(df)
print('-'*30)

# 4. numpy 배열을 통한 열 추가 
# -> 조건에 다른 선택적인 값을 추가 
# -> 조건이 참인 경우 A, 그렇지 않은 경우 B
df['국어결과'] = numpy.where(df['국어'] >= 70, '합격', '불합격')
print(df)
print('-'*30)

# numpy.select()를 통한 열 추가
# 여러개의 조건중에서 선택적인 값을 추가하기
# 학점을 부여하기 위한 점수의 구간을 설정하는 조건들을 리스트로 설정
conditions = [
            (df['영어']>=90),                 # A
            (df['영어']>=80),                 # B
            (df['영어']>=70),                 # C
            (df['영어']<70),                  # F
            (numpy.isnan(df['영어'])== True)  # F
    ]
print(conditions)

# 조건에 따라 부여될 학점
grade = ['A', 'B', 'C', 'F', 'F']

# 조건에 따른 학점 열 추가하기
df['영어학점'] = numpy.select(conditions, grade)
print(df)
print('-'*30)

'''
grade와 conditions의 열마다 연산을 하며, True인 값을 구한다.
만일, True가 여러개일 경우는 제일 첫번째 것으로 값이 정해진다. 

grade conditions
A       False,  True,   False,  False,  False
B       False,  True,   False,  False,  False
C       False,  True,   True,   False,  False
F       False,  False,  False,  True,   True
F       True,   False,  False,  False,  False

result  F       A       C       F       F
'''
'''
     국어    영어    수학    과학
철수   98   NaN  88.0  64.0
영희   88  90.0  62.0  72.0
민철   92  70.0   NaN   NaN
수현   63  60.0  31.0  70.0
호영  120  50.0   NaN  88.0
------------------------------
     국어    영어    수학    과학   한국사
철수   98   NaN  88.0  64.0  92.0
영희   88  90.0  62.0  72.0  83.0
민철   92  70.0   NaN   NaN  72.0
수현   63  60.0  31.0  70.0   NaN
호영  120  50.0   NaN  88.0  80.0
------------------------------
     국어    영어    수학    과학   한국사  세계사
철수   98   NaN  88.0  64.0  92.0  100
영희   88  90.0  62.0  72.0  83.0  100
민철   92  70.0   NaN   NaN  72.0  100
수현   63  60.0  31.0  70.0   NaN  100
호영  120  50.0   NaN  88.0  80.0  100
------------------------------
     국어    영어    수학    과학   한국사  세계사    사회
철수   98   NaN  88.0  64.0  92.0  100  82.0
영희   88  90.0  62.0  72.0  83.0  100  90.0
민철   92  70.0   NaN   NaN  72.0  100  92.0
수현   63  60.0  31.0  70.0   NaN  100  64.0
호영  120  50.0   NaN  88.0  80.0  100   NaN
------------------------------
     국어    영어    수학    과학   한국사  세계사    사회  사회1
철수   98   NaN  88.0  64.0  92.0  100  82.0  NaN
영희   88  90.0  62.0  72.0  83.0  100  90.0  NaN
민철   92  70.0   NaN   NaN  72.0  100  92.0  NaN
수현   63  60.0  31.0  70.0   NaN  100  64.0  NaN
호영  120  50.0   NaN  88.0  80.0  100   NaN  NaN
------------------------------
     국어    영어    수학    과학   한국사  세계사    사회  사회1 국어결과
철수   98   NaN  88.0  64.0  92.0  100  82.0  NaN   합격
영희   88  90.0  62.0  72.0  83.0  100  90.0  NaN   합격
민철   92  70.0   NaN   NaN  72.0  100  92.0  NaN   합격
수현   63  60.0  31.0  70.0   NaN  100  64.0  NaN  불합격
호영  120  50.0   NaN  88.0  80.0  100   NaN  NaN   합격
------------------------------
[철수    False
영희     True
민철    False
수현    False
호영    False
Name: 영어, dtype: bool, 철수    False
영희     True
민철    False
수현    False
호영    False
Name: 영어, dtype: bool, 철수    False
영희     True
민철     True
수현    False
호영    False
Name: 영어, dtype: bool, 철수    False
영희    False
민철    False
수현     True
호영     True
Name: 영어, dtype: bool, 철수     True
영희    False
민철    False
수현    False
호영    False
Name: 영어, dtype: bool]
     국어    영어    수학    과학   한국사  세계사    사회  사회1 국어결과 영어학점
철수   98   NaN  88.0  64.0  92.0  100  82.0  NaN   합격    F
영희   88  90.0  62.0  72.0  83.0  100  90.0  NaN   합격    A
민철   92  70.0   NaN   NaN  72.0  100  92.0  NaN   합격    C
수현   63  60.0  31.0  70.0   NaN  100  64.0  NaN  불합격    F
호영  120  50.0   NaN  88.0  80.0  100   NaN  NaN   합격    F
------------------------------
'''













