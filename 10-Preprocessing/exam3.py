from pandas import DataFrame
from pandas import merge      

# 데이터 생성
df_first = DataFrame({'아이디':['hello', 'world', 'python', 'hello'], 
                     '이름':[14000, 13000, 15000, 13000]})
print(df_first)
print('-' * 30)

df_second = DataFrame({'아이디':['hello', 'python', 'python', 'world'], 
                     '적립금':[300, 500, 100, 200]})
print(df_second)
print('-' * 30)

# 병합하기
# -> 양쪽 데이터프레임에 모두 존재하는 데이터만 보여준다.
# -> 모든 경우의 수를 따져서 조합을 만들어 낸다. 
df1 = merge(df_first, df_second)
print(df1)
print('-' * 30)

'''
      아이디     이름
0   hello  14000
1   world  13000
2  python  15000
3   hello  13000
------------------------------
      아이디  적립금
0   hello  300
1  python  500
2  python  100
3   world  200
------------------------------
      아이디     이름  적립금
0   hello  14000  300
1   hello  13000  300
2   world  13000  200
3  python  15000  500
4  python  15000  100
------------------------------
'''