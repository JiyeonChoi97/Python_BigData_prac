from pandas import DataFrame
from pandas import concat      # 행단위 병합 함수

# 데이터 생성
df_top = DataFrame({'국어':[90,82], '수학':[81,76]}, index=['민철', '철수'])
print(df_top)
print('-' * 30)

df_middle = DataFrame({'국어':[70,62], '영어':[77,68]}, index=['영민', '정수'])
print(df_middle)
print('-' * 30)

df_bottom = DataFrame({'영어':[70,88], '과학':[81,76]}, index=['민철', '태영'])
print(df_bottom)
print('-' * 30)

# 1. A에 B를 이어붙이기
# -> 단순히 세로로 병합만 수행한다. 
# -> 데이터프레임간에 컬럼이 다르면, 존재하지 않는 컬럼은 결측치로 채워 넣는다. 
df_a = df_top.append(df_middle)
print(df_a)
print('-'*30)

df_a = df_top.append([df_middle, df_bottom])
print(df_a)
print('-'*30)

# 2. A, B, C 를 병합하기
# -> 단순히 세로로 방향을 덧붙이는 개념이므로 인덱스가 중복되는 경우도 발생
df_b = concat([df_top, df_middle, df_bottom])
print(df_b)
print('-'*30)

'''
<<<<행단위 병합>>>>
    국어  수학
민철  90  81
철수  82  76
------------------------------
    국어  영어
영민  70  77
정수  62  68
------------------------------
    영어  과학
민철  70  81
태영  88  76
------------------------------
    국어    수학    영어
민철  90  81.0   NaN
철수  82  76.0   NaN
영민  70   NaN  77.0
정수  62   NaN  68.0
------------------------------
      국어    수학    영어    과학
민철  90.0  81.0   NaN   NaN
철수  82.0  76.0   NaN   NaN
영민  70.0   NaN  77.0   NaN
정수  62.0   NaN  68.0   NaN
민철   NaN   NaN  70.0  81.0
태영   NaN   NaN  88.0  76.0
------------------------------
      국어    수학    영어    과학
민철  90.0  81.0   NaN   NaN
철수  82.0  76.0   NaN   NaN
영민  70.0   NaN  77.0   NaN
정수  62.0   NaN  68.0   NaN
민철   NaN   NaN  70.0  81.0
태영   NaN   NaN  88.0  76.0
------------------------------
'''