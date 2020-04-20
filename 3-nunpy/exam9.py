import numpy

# 난수 numpy 배열 생성

# 0<=난수<1 사이의 실수 난수 1개 생성
f1 = numpy.random.rand()
print(f1)
print(type(f1))
print('-' * 30)

arr1 = numpy.random.rand(2, 3)  # 2x3 행렬
print(arr1)
print(type(arr1))
print('-' * 30)

arr2 = numpy.random.rand(2, 3, 4) # 2x3x4 행렬
print(arr2)
print(type(arr2))
print('-' * 30)

# 1~29 사이의 정수 난수 1개 생성
n1 = numpy.random.randint(1, 30)
print(n1)
print(type(n1))
print('-' * 30)

# size : 행렬의 크기 지정
n2 = numpy.random.randint(1, 30, size=(3, 4))
print(n2)
print(type(n2))
print('-' * 30)













