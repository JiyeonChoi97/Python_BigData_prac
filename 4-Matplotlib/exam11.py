from matplotlib import pyplot
import numpy

# 데이터 생성
city = ['서울', '인천', '대전', '대구', '울산', '부산', '광주']
lat = [37.56, 37.45, 36.35, 35.87, 35.53, 35.18, 35.16] 		# 위도
lng = [126.97, 126.70, 127.38, 128.60, 129.31, 129.07, 126.85] 	# 경도
pop_den = [16154, 2751, 2839, 2790, 1099, 4454, 2995] 	# 인구밀도(명/km^2), 2017

size = numpy.array(pop_den) * 0.2
colors = ['r', 'g', 'b', 'c','m','k','y']
pyplot.scatter(lng, lat, s=size, c=colors, alpha=0.5)
pyplot.xlabel('경도 (longitude)')
pyplot.ylabel('위도 (latitude)')
pyplot.title('지역별 인구밀도(2017)')

# zip() : list자료형 여러개를 결합해서, slice하는 함수
print(list(zip(lng, lat, city)))

for x, y, name in zip(lng, lat, city)  :
    pyplot.text(x, y, name)
    
pyplot.show()










