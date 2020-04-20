import numpy

data1 = [10, 20, 30, 40, 50]

arr1 = numpy.array(data1)
print(arr1)
print('-' * 30)

# 통계 연산
arr_sum = arr1.sum()    # 합
print(arr_sum, type(arr_sum))
print('-' * 30)

arr_mean = arr1.mean()  # 평균
print(arr_mean, type(arr_mean))
print('-' * 30)

arr_std = arr1.std()    # 표준 편차
print(arr_std, type(arr_std))
print('-' * 30)

arr_var = arr1.var()    # 분산
print(arr_var, type(arr_var))
print('-' * 30)

arr_max = arr1.max()    # 최대값
print(arr_max, type(arr_max))
print('-' * 30)

arr_min = arr1.min()    # 최소값
print(arr_min, type(arr_min))
print('-' * 30)

arr_cumsum = arr1.cumsum()    # 누적합
print(arr_cumsum, type(arr_cumsum))
print('-' * 30)

arr_cumprod = arr1.cumprod()  # 누적곱
print(arr_cumprod, type(arr_cumprod))
print('-' * 30)




