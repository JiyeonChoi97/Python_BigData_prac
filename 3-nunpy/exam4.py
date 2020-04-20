import numpy

# .reshape(m, n) : numpy 배열을 행렬로 모양 변경
# 주의 : 배열의 갯수와 행렬의 갯수는 일치해야한다.
#        일치하지 않으면 error 발생
arr1 = numpy.arange(1, 14).reshape(4, 3)
print(arr1)
print(type(arr1))
print(arr1.dtype)
print(arr1.shape)   # 배열 형태


