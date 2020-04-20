import numpy

data1 = [1, 2, 3, 4, 5]
data2 = [1.7, 2, 5.5, 7, 9.9]

# numpy 1차원 배열 생성
arr1 = numpy.array(data1)
arr2 = numpy.array(data2)  # 정수와 실수가 섞여있으면, 모두 실수로 변환

# 저장 내용 확인
print("arr1 :", arr1)
print("arr2 :", arr2)
print('-' * 30)

# numpy 배열 속성 확인
print(type(arr1))    # 변수에 저장된 데이터 종류
print(type(arr2))
print(arr1.dtype)    # numpy 배열에 저장된 데이터 종류
print(arr2.dtype)





