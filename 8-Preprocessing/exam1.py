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

# 1. 단일 조건
# -> 기본적인 비교식을 사용한다.
# 국어점수 > 80 인 학생 조회
result = df.query('국어>80')
print(result)
print(type(result))
print('-'*30)

# 2. and 조건 사용
# 국어점수가 80점을 넘고, 수학점수도 80점을 넘는 학생 조회
result2 = df.query('국어>80 and 수학>80')
print(result2)
print(type(result2))
print('-'*30)

# 3. or 조건 사용
# 국어점수가 70점 미만이거나 수학점수가 70점 미만인 학생 조회
result3 = df.query('국어<70 or 수학<70')
print(result3)
print(type(result3))
print('-'*30)

# 4. in 조건 사용
# -> 특정 리스트의 원소중 겹치는 값 찾기

# 검색 조건에 대한 리스트 준비
item = [98,88]
print(item)
print('-'*30)

# item리스트에 포함되어 있는 국어점수 데이터 찾기
result4 = df.query('국어 in @item')
print(result4)
print(type(result4))
print('-'*30)

# 5. not in 조건 사용
# -> 특정 리스트의 원소와 겹치지 않는 값 찾기
# item리스트에 포함되어 있지 않는 국어점수 데이터 찾기
result5 = df.query('국어 not in @item')
print(result5)
print(type(result5))
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
철수   98   NaN  88.0  64.0
영희   88  90.0  62.0  72.0
민철   92  70.0   NaN   NaN
호영  120  50.0   NaN  88.0
<class 'pandas.core.frame.DataFrame'>
------------------------------
    국어  영어    수학    과학
철수  98 NaN  88.0  64.0
<class 'pandas.core.frame.DataFrame'>
------------------------------
    국어    영어    수학    과학
영희  88  90.0  62.0  72.0
수현  63  60.0  31.0  70.0
<class 'pandas.core.frame.DataFrame'>
------------------------------
[98, 88]
------------------------------
    국어    영어    수학    과학
철수  98   NaN  88.0  64.0
영희  88  90.0  62.0  72.0
<class 'pandas.core.frame.DataFrame'>
------------------------------
     국어    영어    수학    과학
민철   92  70.0   NaN   NaN
수현   63  60.0  31.0  70.0
호영  120  50.0   NaN  88.0
<class 'pandas.core.frame.DataFrame'>
------------------------------
'''