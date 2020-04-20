from matplotlib import pyplot

# 데이터 생성
math = [76, 82, 84, 83, 90, 86, 85, 92, 72, 71, 100, 87, 81,
        75, 94, 78, 81, 60, 79, 69, 74, 87, 82, 68, 79]

# 한글 설정
pyplot.rcParams['font.family'] = 'Malgun Gothic'

# 기본 히스토그램 그래프 출력
pyplot.hist(math) # 기본값으로 10개의 계급으로 나눠서 표시
pyplot.show()

# 계급을 8개로 나눠서 표시
pyplot.hist(math, bins=8) # 60~65, 66~70, ... , 96~100
pyplot.xlabel('시험 점수')
pyplot.ylabel('도수')
pyplot.title('수학 시험의 히스토그램')
pyplot.grid()
pyplot.show()

