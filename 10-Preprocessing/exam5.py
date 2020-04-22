from pandas import DataFrame
from pandas import merge    

# 데이터 생성
score_kor = DataFrame({'이름':['영희', '철수'], '국어':[87,91]})
score_eng = DataFrame({'성명':['영희', '철수'], '영어':[90,82]})
print(score_kor)
print('-' * 30)
print(score_eng)
print('-' * 30)

# 1. merge의 기본적인 사용
# -> 양쪽 데이터프레임에 모두 존재하는 데이터만 보여준다. 
#df = merge(score_kor, score_eng)    # error 발생 : 공통 컬럼이 없어서

# 2. 왼쪽의 이름 컬럼과 오른쪽의 성명 컬럼이 같은 데이터를 병합
# -> left_on, right_on
df = merge(score_kor, score_eng, left_on=['이름'], right_on=['성명']) 
print(df)
print('-' * 30)

# 3. 중복되는 값을 갖는 '성명' 컬럼은 필요없으므로 삭제
df.drop('성명', axis=1, inplace=True)
print(df)
print('-' * 30)

'''
   이름  국어
0  영희  87
1  철수  91
------------------------------
   성명  영어
0  영희  90
1  철수  82
------------------------------
   이름  국어  성명  영어
0  영희  87  영희  90
1  철수  91  철수  82
------------------------------
   이름  국어  영어
0  영희  87  90
1  철수  91  82
------------------------------
'''