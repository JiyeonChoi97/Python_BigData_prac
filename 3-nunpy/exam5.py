import numpy

# 범위의 시작과 끝을 지정하고, 데이터의 개수도 지정해서
# numpy 배열을 생성
arr1 = numpy.linspace(1, 5, 10) # 1~5 사이의 10개 데이터 생성 
print(arr1)
print(type(arr1))
print(arr1.shape)
print('-' * 30)

arr1 = numpy.linspace(1, 10, 10) 
print(arr1)
print(type(arr1))
print(arr1.shape)
print('-' * 30)

arr1 = numpy.linspace(1, numpy.pi, 20) 
print(arr1)
print(type(arr1))
print(arr1.shape)
print('-' * 30)










