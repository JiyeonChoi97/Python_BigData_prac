import numpy

data1 = [10, 20, 30, 40, 50, 60]

# 1차원 numpy 배열
arr1 = numpy.array(data1)
print(arr1)
print('-' * 30)

# 1차원 인덱싱
print(arr1[2])
print(arr1[[1, 3, 5]])
print(arr1[arr1 > 40])
#print(data1[data1 > 40])   # error 발생, 리스트는 인덱싱에 조건을 사용할 수 없음
print('-' * 30)

# 2차원 numpy 배열
arr2 = numpy.arange(10, 100, 10).reshape(3, 3)
print(arr2)
print('-' * 30)

# 2차원 인덱싱
print(arr2[0, 2])   # 값 1개 확인  
                    # cf. 리스트는 [0][2]
arr2[0, 2] = 35
print(arr2)
print('-' * 30)

print(arr2[0, 2])
print(arr2[0][2]) 
arr2[0][2] = 37
print(arr2)
print('-' * 30)

# 1개 행 전부 변경 : numpy 배열 적용
arr2[1] = numpy.array([45, 55, 65])
print(arr2)
print('-' * 30)

# 1개 행 전부 변경 : 리스트 적용
arr2[2] = [145, 155, 165]
print(arr2)
print('-' * 30)

# 2차원 배열에서 특정위치값 여러개 선택
# 배열명[[행위치], [열위치]]
print(arr2[[0, 2], [0, 1]])  # [0, 0], [2, 1]













