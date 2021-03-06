from pandas import DataFrame

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

# 1. 컬럼(열)의 순서 변경
df1 = df.reindex(columns=['국어','수학','과학','영어'])
print(df1)
print('-' * 30)
print(df)
print('-' * 30)

# 2. 인덱스(행)의 순서 변경
df2 = df.reindex(index=['영희','수현','철수','민철','호영'])
print(df2)
print('-' * 30)
print(df)
print('-' * 30)

# 3. 인덱스와 컬럼의 순서를 동시에 변경
df3 = df.reindex(columns=['국어','수학','과학','영어'],
                 index=['영희','수현','철수','민철','호영'])
print(df3)
print('-' * 30)
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
     국어    수학    과학    영어
철수   98  88.0  64.0   NaN
영희   88  62.0  72.0  90.0
민철   92   NaN   NaN  70.0
수현   63  31.0  70.0  60.0
호영  120   NaN  88.0  50.0
------------------------------
     국어    영어    수학    과학
철수   98   NaN  88.0  64.0
영희   88  90.0  62.0  72.0
민철   92  70.0   NaN   NaN
수현   63  60.0  31.0  70.0
호영  120  50.0   NaN  88.0
------------------------------
     국어    영어    수학    과학
영희   88  90.0  62.0  72.0
수현   63  60.0  31.0  70.0
철수   98   NaN  88.0  64.0
민철   92  70.0   NaN   NaN
호영  120  50.0   NaN  88.0
------------------------------
     국어    영어    수학    과학
철수   98   NaN  88.0  64.0
영희   88  90.0  62.0  72.0
민철   92  70.0   NaN   NaN
수현   63  60.0  31.0  70.0
호영  120  50.0   NaN  88.0
------------------------------
     국어    수학    과학    영어
영희   88  62.0  72.0  90.0
수현   63  31.0  70.0  60.0
철수   98  88.0  64.0   NaN
민철   92   NaN   NaN  70.0
호영  120   NaN  88.0  50.0
------------------------------
     국어    영어    수학    과학
철수   98   NaN  88.0  64.0
영희   88  90.0  62.0  72.0
민철   92  70.0   NaN   NaN
수현   63  60.0  31.0  70.0
호영  120  50.0   NaN  88.0
------------------------------
'''
