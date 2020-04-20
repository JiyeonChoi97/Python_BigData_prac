from pandas import date_range

# 데이터 생성
s1 = date_range(start='2020-01-01', end='2020-01-04') # 1일씩 증가 
print(s1)
print(type(s1))
print('-'*40)

s1 = date_range(start='2020-1-1', end='2020-1-4') # 1일씩 증가 
print(s1)
print(type(s1))
print('-'*40)

s1 = date_range(start='2020/1/1', end='2020/1/4') # 1일씩 증가 
print(s1)
print(type(s1))
print('-'*40)

s1 = date_range(start='2020/1/1', periods=4) # 1일씩 증가 
print(s1)
print(type(s1))
print('-'*40)

# 2일씩 증가
s1 = date_range(start='2020/1/1', periods=4, freq='2D') 
print(s1)
print(type(s1))
print('-'*40)

# 1주일씩 증가 
# freq='W' : 일요일을 시작 기준으로 일주일 주기, freq='W-SUN'과 같은 의미
s1 = date_range(start='2020/1/1', periods=4, freq='W')
print(s1)
print(type(s1))
print('-'*40)

# BM : 업무 월말 날짜 기준 주기
s1 = date_range(start='2020/1/1', periods=4, freq='BM')
print(s1)
print(type(s1))
print('-'*40)

# 2BM : 업무일 기준 2개월 월말 주기
s1 = date_range(start='2020/1/1', periods=4, freq='2BM')
print(s1)
print(type(s1))
print('-'*40)



'''
DatetimeIndex(['2020-01-01', '2020-01-02', '2020-01-03', '2020-01-04'], dtype='datetime64[ns]', freq='D')
<class 'pandas.core.indexes.datetimes.DatetimeIndex'>
----------------------------------------
DatetimeIndex(['2020-01-01', '2020-01-02', '2020-01-03', '2020-01-04'], dtype='datetime64[ns]', freq='D')
<class 'pandas.core.indexes.datetimes.DatetimeIndex'>
----------------------------------------
DatetimeIndex(['2020-01-01', '2020-01-02', '2020-01-03', '2020-01-04'], dtype='datetime64[ns]', freq='D')
<class 'pandas.core.indexes.datetimes.DatetimeIndex'>
----------------------------------------
DatetimeIndex(['2020-01-01', '2020-01-02', '2020-01-03', '2020-01-04'], dtype='datetime64[ns]', freq='D')
<class 'pandas.core.indexes.datetimes.DatetimeIndex'>
----------------------------------------
DatetimeIndex(['2020-01-01', '2020-01-03', '2020-01-05', '2020-01-07'], dtype='datetime64[ns]', freq='2D')
<class 'pandas.core.indexes.datetimes.DatetimeIndex'>
----------------------------------------
DatetimeIndex(['2020-01-05', '2020-01-12', '2020-01-19', '2020-01-26'], dtype='datetime64[ns]', freq='W-SUN')
<class 'pandas.core.indexes.datetimes.DatetimeIndex'>
----------------------------------------
DatetimeIndex(['2020-01-31', '2020-02-28', '2020-03-31', '2020-04-30'], dtype='datetime64[ns]', freq='BM')
<class 'pandas.core.indexes.datetimes.DatetimeIndex'>
----------------------------------------
DatetimeIndex(['2020-01-31', '2020-03-31', '2020-05-29', '2020-07-31'], dtype='datetime64[ns]', freq='2BM')
<class 'pandas.core.indexes.datetimes.DatetimeIndex'>
----------------------------------------
'''
