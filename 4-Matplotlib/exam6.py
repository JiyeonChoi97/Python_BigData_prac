from matplotlib import pyplot
import numpy

x = numpy.linspace(-4, 4, 100)
y1 = x**3
y2 = 10 * x**2 -2

print(x)

pyplot.plot(x, y1, x, y2)
pyplot.show()

pyplot.plot(x, y1, x, y2)
pyplot.xlim(-1, 1)
pyplot.ylim(-3, 3)
pyplot.show()