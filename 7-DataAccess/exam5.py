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

# 1. 열 => 행 순으로 접근하기(읽기 전용)
print(df['국어']['철수'])
print('-'*30)
#df['국어']['철수']=100
print(df)
print('-'*30)

# 2. 행 => 열 순으로 접근하기(일기, 쓰기 전용)
print(df.loc['철수','국어'])
df.loc['철수','국어']=100
print(df)
print('-'*30)


print(df.loc['철수','국어'])        # 100
print(df.loc['철수']['국어'])       # 100.0
df.loc['철수']['국어'] = 200        # 저장이 안됨 
print(df)
print('-'*30)

'''
     국어    영어    수학    과학
철수   98   NaN  88.0  64.0
영희   88  90.0  62.0  72.0
민철   92  70.0   NaN   NaN
수현   63  60.0  31.0  70.0
호영  120  50.0   NaN  88.0
------------------------------
98
------------------------------
     국어    영어    수학    과학
철수   98   NaN  88.0  64.0
영희   88  90.0  62.0  72.0
민철   92  70.0   NaN   NaN
수현   63  60.0  31.0  70.0
호영  120  50.0   NaN  88.0
------------------------------
98
     국어    영어    수학    과학
철수  100   NaN  88.0  64.0
영희   88  90.0  62.0  72.0
민철   92  70.0   NaN   NaN
수현   63  60.0  31.0  70.0
호영  120  50.0   NaN  88.0
------------------------------
100
100.0
     국어    영어    수학    과학
철수  100   NaN  88.0  64.0
영희   88  90.0  62.0  72.0
민철   92  70.0   NaN   NaN
수현   63  60.0  31.0  70.0
호영  120  50.0   NaN  88.0
------------------------------
D:\bigdata1_jiyeon\python\workspace_b\7-DataAccess\exam5.py:34: SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
  df.loc['철수']['국어'] = 200        # 저장이 안됨
'''