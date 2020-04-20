from pandas import Series

items=[10,30,50,70,90]
column = Series(items)
print(column)
print('-'*40)

# 특정조건에 맞는 항목들만 추출
# 시리즈 이름[이름에 대한 조건식]
# -> 30 초과인 항목들만 추출
in1 = column[column > 30]
print(in1)
print(type(in1))
print('-'*40)

# AND 조건
# -> 70이하 and 10 초과인 항목들만 추출
in2 = column[(column > 10) & (column <= 70)]
print(in2)
print(type(in2))
print('-'*40)

# OR 조건
# -> 10이하 or 70 이상인 항목들만 추출
in3 = column[(column <= 10) | (column >= 70)]
print(in3)
print(type(in3))
print('-'*40)

'''
0    10
1    30
2    50
3    70
4    90
dtype: int64
----------------------------------------
2    50
3    70
4    90
dtype: int64
<class 'pandas.core.series.Series'>
----------------------------------------
1    30
2    50
3    70
dtype: int64
<class 'pandas.core.series.Series'>
----------------------------------------
0    10
3    70
4    90
dtype: int64
<class 'pandas.core.series.Series'>
----------------------------------------
'''