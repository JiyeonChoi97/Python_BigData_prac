from matplotlib import pyplot
import numpy

x = numpy.arange(-4.5, 5, 0.5)
y1 = 5*x + 30
y2 = 2 * x**2
y3 = 4 * x**2 + 10

pyplot.figure(1)    # 그래프창을 생성, 창번호 부여
pyplot.plot(x, y1)

pyplot.figure(2)
pyplot.plot(x, y2)

# 1번 창에 그래프 추가
pyplot.figure(2)
pyplot.plot(x, y3)
pyplot.show()

pyplot.figure(1)
pyplot.plot(x, y3)











