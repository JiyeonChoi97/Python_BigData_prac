from matplotlib import pyplot
import numpy

x = numpy.arange(-4.5, 5, 0.5)
y1 = 5*x + 30
y2 = 2 * x**2
y3 = 4 * x**2 + 10

pyplot.plot(x, y1)
#pyplot.show()

pyplot.plot(x, y2)
#pyplot.show()

pyplot.plot(x, y3)
pyplot.show()

pyplot.plot(x, y1, x, y2, x, y3)
pyplot.show()









