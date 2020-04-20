from matplotlib import pyplot
import numpy

x = numpy.arange(0, 10, 0.1)
y1 = 0.3 * (x-5)**2 + 1
y2 = -1.5 * x + 3
y3 = numpy.sin(x)**2
y4 = 10 * numpy.exp(-x) + 1

# 창 1개에 여러개의 그래프 출력
# 2 x 2 모양으로 출력
pyplot.figure(figsize=(10, 6))
pyplot.subplot(2, 2, 1)   # index=1 : (0, 0)
pyplot.plot(x, y1)

pyplot.subplot(2, 2, 2)   # index=1 : (0, 1)
pyplot.plot(x, y2)

pyplot.subplot(2, 2, 3)   # index=1 : (1, 0)
pyplot.plot(x, y3)

pyplot.subplot(2, 2, 4)   # index=1 : (1, 1)
pyplot.plot(x, y4)








