import numpy

data1 = [1, 2, 3]
data2 = [4, 5.5, 6]
data3 = [7, 8, 9]

# numpy 2차원 배열 생성 : []로 묶는다.
arr1 = numpy.array([data1, data2, data3])

# 저장 내용 확인
print(arr1)
print('-' * 30)

# 속성 확인
print(type(arr1))
print(arr1.dtype)
