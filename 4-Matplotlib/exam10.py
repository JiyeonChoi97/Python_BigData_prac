from matplotlib import pyplot
import numpy

# 데이터 생성
height = [165, 177, 160, 180, 185, 155, 172]
weight = [62, 67, 55, 74, 90, 43, 64]

pyplot.scatter(height, weight)
pyplot.xlabel('Height(cm)')
pyplot.ylabel('Weight(kg)')
pyplot.title('Height & Weight')
pyplot.grid(True)
pyplot.show()

# 원의 크기와 색상 지정
pyplot.scatter(height, weight, s=500, c='r')
pyplot.xlabel('Height(cm)')
pyplot.ylabel('Weight(kg)')
pyplot.title('Height & Weight')
pyplot.grid(True)
pyplot.show()

# 데이터별로 마커의 크기와 색상 지정
#size = 100 * numpy.arange(1, 8)
size = [100, 200, 300, 400, 500, 600, 700]
colors = ['r', 'g', 'b','c', 'm', 'k', 'y']
pyplot.scatter(height, weight, s=size, c=colors)
pyplot.show()







