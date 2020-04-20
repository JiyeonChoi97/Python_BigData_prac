from matplotlib import pyplot
import numpy

data1 = [10, 14, 19, 20, 25]

# 리스트 내용을 그래프로 출력
# x축을 지정하지 않으면, 0부터 1씩 증가값을 가지고, 데이터는 y축 값이 된다.
pyplot.plot(data1)
pyplot.show()

# numpy 배열 이용
arr = numpy.array(data1)
pyplot.plot(arr)
pyplot.show()

# x축, y축 값 지정
# plot(x, y)
pyplot.plot([1, 2, 3, 4, 5], data1)
pyplot.show()












