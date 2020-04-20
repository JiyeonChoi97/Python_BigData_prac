import numpy

data1 = [1, 2, 3, 4]
data2 = [10, 20, 30, 40]

# numpy 배열을 생성후, 바로 행렬로 변환
arr1 = numpy.array(data1).reshape(2, 2)
arr2 = numpy.array(data2).reshape(2, 2)

print(arr1)
print(arr2)
print('-' * 30)

# 행렬 연산
arr_dot = numpy.dot(arr1, arr2)   # 행렬곱
print(arr_dot)
print('-' * 30)

arr_transpose = numpy.transpose(arr1)   # 전치행렬
print(arr1)
print(arr_transpose)
print('-' * 30)

arr_inv = numpy.linalg.inv(arr1)   # 역행렬
print(arr1)
print(arr_inv)
print('-' * 30)

arr_det = numpy.linalg.det(arr1)   # 행렬식
print(arr1)
print(arr_det)
print('-' * 30)







