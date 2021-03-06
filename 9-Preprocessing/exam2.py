from pandas import DataFrame
from pandas import Series

# 딕셔너리를 원소로 갖는 리스트
grade_data = [
                {'국어':98, '영어':None, '수학':88, '과학':64},
                {'국어':88, '영어':90, '수학':62, '과학':72},
                {'국어':92, '영어':70, '수학':None, '과학':None},
                {'국어':63, '영어':60, '수학':31, '과학':70},
                {'국어':120, '영어':50, '수학':None, '과학':88}
            ]

df = DataFrame(grade_data, index=['철수','영희','민철','수현','호영'])
print(df)
print('-' * 30)

# 1. 컬럼이름 변경하기
df1 = df.rename(columns={'국어':'kor', '영어':'eng', 
                         '수학':'mat', '과학':'sinc'})
print(df1)
print('-' * 30)
print(df)
print('-' * 30)

# 2. 인덱스 이름 변경하기
df2 = df.rename(index={'영희':'yh', '수현':'sh',
                       '호영':'hy', '철수':'cs', '민철':'mc'})
print(df2)
print('-' * 30)
print(df)
print('-' * 30)

df2 = df.rename(index=Series([1,2,3,4,5]))
print(df2)
print('-' * 30)
print(df)
print('-' * 30)

# 3. 컬럼과 인덱스 동시 변경 : 원본에 반영
df.rename(index={'영희':'yh', '수현':'sh',
                 '호영':'hy', '철수':'cs', '민철':'mc'},
          columns={'국어':'kor', '영어':'eng', 
                   '수학':'mat', '과학':'sinc'},
          inplace=True)
print(df)
print('-' * 30)

'''

     국어    영어    수학    과학
철수   98   NaN  88.0  64.0
영희   88  90.0  62.0  72.0
민철   92  70.0   NaN   NaN
수현   63  60.0  31.0  70.0
호영  120  50.0   NaN  88.0
------------------------------
    kor   eng   mat  sinc
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
수현   63  60.0  31.0  70.0
호영  120  50.0   NaN  88.0
------------------------------
     국어    영어    수학    과학
cs   98   NaN  88.0  64.0
yh   88  90.0  62.0  72.0
mc   92  70.0   NaN   NaN
sh   63  60.0  31.0  70.0
hy  120  50.0   NaN  88.0
------------------------------
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
수현   63  60.0  31.0  70.0
호영  120  50.0   NaN  88.0
------------------------------
     국어    영어    수학    과학
철수   98   NaN  88.0  64.0
영희   88  90.0  62.0  72.0
민철   92  70.0   NaN   NaN
수현   63  60.0  31.0  70.0
호영  120  50.0   NaN  88.0
------------------------------
    kor   eng   mat  sinc
cs   98   NaN  88.0  64.0
yh   88  90.0  62.0  72.0
mc   92  70.0   NaN   NaN
sh   63  60.0  31.0  70.0
hy  120  50.0   NaN  88.0
------------------------------
'''