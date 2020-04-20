import numpy

# 범위를 지정해서 numpy 배열 생성
# arange([start,] stop[, step])
arr1 = numpy.arange(0, 10, 2)
print(arr1)
print(type(arr1))
print(arr1.dtype)
print('-' * 30)

arr1 = numpy.arange(0, 10)
print(arr1)
print(type(arr1))
print(arr1.dtype)
print('-' * 30)

arr1 = numpy.arange(5)
print(arr1)
print(type(arr1))
print(arr1.dtype)
print('-' * 30)







