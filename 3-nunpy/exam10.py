import numpy

data1 = [10, 20, 30, 40]
data2 = [100, 200, 300, 400]

# numpy 배열 생성
arr1 = numpy.array(data1)
arr2 = numpy.array(data2)

print(arr1)
print(arr2)
print('-' * 30)

# numpy 배열을 통째로 계산
arr_add = arr1 + arr2
print(arr_add)
print('-' * 30)

arr_sub = arr1 - arr2
print(arr_sub)
print('-' * 30)

arr_mul = arr1 * arr2
print(arr_mul)
print('-' * 30)

arr_div = arr1 / arr2
print(arr_div)
print('-' * 30)

arr_add2 = arr1 + 7
print(arr_add2)
print('-' * 30)

arr_square = arr1 ** 2
print(arr_square)
print('-' * 30)




