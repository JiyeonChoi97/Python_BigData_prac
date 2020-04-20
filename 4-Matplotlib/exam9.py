from matplotlib import pyplot
import numpy
import matplotlib

x = numpy.arange(0, 5, 1)
y1 = x
y2 = x + 1
y3 = x + 2
y4 = x + 3

pyplot.plot(x, y1, x, y2, x, y3, x, y4)
pyplot.xlabel('X-축')
pyplot.ylabel('y-축')
pyplot.title('선 그리기')
pyplot.grid(True)
pyplot.legend(['데이터1', '데이터2', '데이터3', '데이터4'])
pyplot.show()

# 한글 설정
matplotlib.rcParams['font.family'] = 'Malgun Gothic'

pyplot.plot(x, y1, x, y2, x, y3, x, y4)
pyplot.xlabel('X-축')
pyplot.ylabel('y-축')
pyplot.title('선 그리기')
pyplot.grid(True)
pyplot.legend(['데이터1', '데이터2', '데이터3', '데이터4'])
pyplot.show()

# 특정위치에 문자열 출력
pyplot.plot(x, y1, x, y2, x, y3, x, y4)
pyplot.text(0, 6, '데이터1')
pyplot.text(0, 5, '데이터2')
pyplot.text(3, 1, '데이터3')
pyplot.text(3, 0, '데이터4')
pyplot.show()







