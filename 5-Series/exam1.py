from pandas import Series

items=[10,30,50,70,90]
column = Series(items)
print(column)
print(type(column))


'''
0    10
1    30
2    50
3    70
4    90
dtype: int64
<class 'pandas.core.series.Series'>
'''
