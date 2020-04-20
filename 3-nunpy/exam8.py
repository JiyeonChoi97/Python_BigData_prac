import numpy

data1 = ['people', 'boy', 'girl', 'man', 'woman']
data2 = ['1.5', '2.5', '3.5', '4.5', '5.5']
data3 = ['10', '20', '30', '40', '50']

# numpy 배열 생성
arr1 = numpy.array(data1)
arr2 = numpy.array(data2)
arr3 = numpy.array(data3)

print(arr1)
print(arr2)
print(arr3)
print('-' * 30)

print(arr1.dtype)
print(arr2.dtype)
print(arr3.dtype)
print('-' * 30)

# numpy 배열의 형변환 : astype

# 문자열을 실수로 형변환
arr_f = arr2.astype(float)
print(arr_f)
print(arr_f.dtype)
print('-' * 30)

# 문자열을 정수로 형변환
arr_i = arr3.astype(int)
print(arr_i)
print(arr_i.dtype)
print('-' * 30)

# 정수를 문자열로 형변환
arr = arr_i.astype(str)
print(arr)
print(arr.dtype)
print('-' * 30)




