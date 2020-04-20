from matplotlib import pyplot
import numpy

x = numpy.arange(-4.5, 5, 0.5)
y = 2 * x**2

print([x, y])

pyplot.plot(x, y)
pyplot.show()
