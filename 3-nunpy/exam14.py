import numpy

data1 = [10, 20, 30, 40, 50, 60]

# numpy 1차원 배열
arr1 = numpy.array(data1)
print(arr1)
print('-' * 30)

# 1차원 슬라이싱
print(arr1[1:4])
print(arr1[1:])
print(arr1[:4])
print('-' * 30)

arr1[2:5] = [35, 45, 55]  # 부분값 변경
print(arr1)
print('-' * 30)

arr1[2:5] = 37            # 부분값 변경
print(arr1)
print('-' * 30)

# numpy 2차원 배열
arr2 = numpy.arange(10, 100, 10).reshape(3, 3)
print(arr2)
print('-' * 30)

# 2차원 슬라이싱
# 배열명[행시작:행끝, 열시작:열끝]
print(arr2[1:3, 1:3])
print('-' * 30)

# 배열명[행위치][열시작:열끝]
print(arr2[1][0:2])
print('-' * 30)

# 부분값 변경
# 배열명[행시작:행끝, 열시작:열끝]
arr2[0:2, 1:3] = [[25, 35], [55, 65]]
print(arr2)
print('-' * 30)








