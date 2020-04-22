# 왼쪽의 인덱스와 오른쪽의 컬럼을 기준으로 열단위 병합
from pandas import DataFrame
from pandas import merge 

# 데이터 생성
score_khistory = DataFrame({'한국사':[87,91]}, index=['영희', '철수'])
print(score_khistory)
print('-' * 30)

score_whistory = DataFrame({'세계사':[90, 82], '이름':['영희', '철수']})
print(score_whistory)
print('-' * 30)

# 1. 왼쪽에서는 인덱스 사용, 오른쪽으로는 '이름'컬럼 사용
# -> 인덱스가 사라지고, 모두 커럼으로 지정된다. 
df = merge(score_khistory, score_whistory, left_index=True, right_on=['이름'])
print(df.head(5))
print('-' * 30)

# 2. 이름 컬럼을 인덱스로 지정하고 삭제하기
name_list = list(df['이름'])
name_dict= {}

for i, v in enumerate(name_list) : 
    name_dict[i] = v

df.rename(index=name_dict, inplace=True)
print(df.head(5))
print('-' * 30)

df.drop('이름', axis=1, inplace=True)
print(df.head(5))
print('-' * 30)

'''
    한국사
영희   87
철수   91
------------------------------
   세계사  이름
0   90  영희
1   82  철수
------------------------------
   한국사  세계사  이름
0   87   90  영희
1   91   82  철수
------------------------------
    한국사  세계사  이름
영희   87   90  영희
철수   91   82  철수
------------------------------
    한국사  세계사
영희   87   90
철수   91   82
------------------------------
'''