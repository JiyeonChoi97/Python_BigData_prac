from matplotlib import pyplot
import numpy

x = numpy.arange(0, 5, 1)
y1 = x
y2 = x + 1
y3 = x + 2
y4 = x + 3

pyplot.plot(x, y1, x, y2, x, y3, x, y4)
pyplot.show()

# x축문자, y축문자, 제목, 격자 그리기
pyplot.plot(x, y1)
pyplot.xlabel('X-axis')
pyplot.ylabel('Y-axis')
pyplot.title('Plot Graph')
pyplot.grid(True)
pyplot.show()

# 범례 출력
pyplot.plot(x, y1, x, y2, x, y3, x, y4)
pyplot.legend(['data1', 'data2', 'data3', 'data3'])
pyplot.show()

pyplot.plot(x, y1, x, y2, x, y3, x, y4)
pyplot.legend(['y=x', 'y=x+1', 'y=x+2', 'y=x+3'])
pyplot.show()

pyplot.plot(x, y1, x, y2, x, y3, x, y4)
pyplot.legend(['y=x', 'y=x+1', 'y=x+2', 'y=x+3'], loc='lower right')
pyplot.show()

pyplot.plot(x, y1, x, y2, x, y3, x, y4)
pyplot.legend(['y=x', 'y=x+1', 'y=x+2', 'y=x+3'], loc='center')
pyplot.show()







