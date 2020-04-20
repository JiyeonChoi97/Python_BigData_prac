from pandas import Series

items=[10,30,50,70,90]
column = Series(items)
print(column)
print('-'*40)

# 시리즈의 색인(index)만 추출
i = column.index
print(i)
print(type(i))
print('-'*40)

# 시리즈의 색인을 리스트로 변환
index_list = list(i)
print(index_list)
print(type(index_list))
print('-'*40)

# 시리즈의 값들만 추출
v = column.values
print(v)
print(type(v))
print('-'*40)

'''
0    10
1    30
2    50
3    70
4    90
dtype: int64
----------------------------------------
RangeIndex(start=0, stop=5, step=1)
<class 'pandas.core.indexes.range.RangeIndex'>
----------------------------------------
[0, 1, 2, 3, 4]
<class 'list'>
----------------------------------------
[10 30 50 70 90]
<class 'numpy.ndarray'>
----------------------------------------
'''
