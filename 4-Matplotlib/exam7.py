from matplotlib import pyplot
import numpy

x = numpy.arange(0, 5, 1)
y1 = x
y2 = x + 1
y3 = x + 2
y4 = x + 3

pyplot.plot(x, y1, x, y2, x, y3, x, y4)
pyplot.show()

# 선 색상 지정 : magenta, yellow, black, cyan
pyplot.plot(x, y1, 'm',x, y2, 'y',x, y3, 'b',x, y4, 'c')
pyplot.show()

# 선 스타일 지정 : 실선, 파선, 점선, 파선 점선 혼합
pyplot.plot(x, y1, '-',x, y2, '--',x, y3, ':',x, y4, '-.')
pyplot.show()

# 마커 지정 : 원, 삼각형, 사각형, 다이아몬드
pyplot.plot(x, y1, 'o',x, y2, '^',x, y3, 's',x, y4, 'd')
pyplot.show()

# 선 생상, 스타일, 마커를 혼합해서 지정
pyplot.plot(x, y1, 'm-o',x, y2, 'y--^',x, y3, 'k:s',x, y4, 'c-.d')
pyplot.show()












