from pandas import DataFrame
from pandas import merge    

# 데이터 생성
score_math = DataFrame({'수학':[90,82]}, index=['민철', '봉구'])
print(score_math)
print('-' * 30)

score_sci = DataFrame({'과학':[80,72]}, index=['민철', '철수'])
print(score_sci)
print('-' * 30)

# merge 기본 사용
#df = merge(score_math, score_sci)           # error 발생 : 공통 컬럼이 없어서

# 1. 왼쪽에서 index를 기준으로 사용하고, 오른쪽에서도 인덱스를 기준으로 사용
# -> 양쪽 데이터프레임의 인덱스가 같은 행끼리 병합됨
df = merge(score_math, score_sci, left_index=True, right_index=True)
print(df)
print('-' * 30)

# 2. 인덱스가 겹치지 않더라도 병합시키기
df = merge(score_math, score_sci, left_index=True, right_index=True, how='outer')
print(df)
print('-' * 30)

'''
    수학
민철  90
봉구  82
------------------------------
    과학
민철  80
철수  72
------------------------------
    수학  과학
민철  90  80
------------------------------
      수학    과학
민철  90.0  80.0
봉구  82.0   NaN
철수   NaN  72.0
------------------------------
'''