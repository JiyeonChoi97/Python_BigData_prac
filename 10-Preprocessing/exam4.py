from pandas import DataFrame
from pandas import merge      

# 데이터 생성
df_a = DataFrame({'고객명':['민수', '수영'], 
                  '데이터':['20000', '100000'],
                  '날짜':['2020-01-01', '2020-02-01']})
print(df_a)
print('-' * 30)

df_b = DataFrame({'고객명':['민수', '수영'], 
                  '데이터':['21세', '20세']})
print(df_b)
print('-' * 30)

# 1. '고객명'컬럼과 '데이터'컬럼이 동시에 일치하는 데이터를 찾아 병합한다.
# -> 양쪽 데이터프레임에 모두 존재하는 데이터만 보여준다.
df = merge(df_a, df_b)
print(df)
print('-' * 30)
 
# 2. on 파라미터를 사용하여 기준열 지정하기 
# -> 기존 열이 아니면서 이름이 같은 열에는 _x 또는 _y와 같은 접미사가 붙는다.
merge_tmp = merge(df_a, df_b, on=['고객명'])
print(merge_tmp)
print('-' * 30)

# 3. 컬럼 이름 재지정
merge_result = merge_tmp.rename(columns={'데이터_x':'금액',
                                         '데이터_y':'나이'})
print(merge_result)
print('-' * 30)

'''
  고객명     데이터          날짜
0  민수   20000  2020-01-01
1  수영  100000  2020-02-01
------------------------------
  고객명  데이터
0  민수  21세
1  수영  20세
------------------------------
Empty DataFrame
Columns: [고객명, 데이터, 날짜]
Index: []
------------------------------
  고객명   데이터_x          날짜 데이터_y
0  민수   20000  2020-01-01   21세
1  수영  100000  2020-02-01   20세
------------------------------
  고객명      금액          날짜   나이
0  민수   20000  2020-01-01  21세
1  수영  100000  2020-02-01  20세
------------------------------
'''