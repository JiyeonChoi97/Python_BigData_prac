from matplotlib import pyplot

# 데이터 생성
fruit = ['사과', '바나나', '딸기', '오렌지', '포도']
result = [7,6,3,2,2]

# 한글 설정
pyplot.rcParams['font.family'] = 'Malgun Gothic'
pyplot.rcParams['font.size'] = 10
# print(pyplot.rcParams.keys)

# 파이 기본 그래프
pyplot.figure(figsize=(5,5))
pyplot.pie(result)
pyplot.show()

# x축 기준각도 0도를 시작으로 반시계방향으로 표시
pyplot.figure(figsize=(5,5))
pyplot.pie(result, labels=fruit, autopct='%.1f%%')
pyplot.show()


# x축 기준각도 90도를 시작으로 시계방향으로 표시
pyplot.figure(figsize=(5,5))
pyplot.pie(result, labels=fruit, autopct='%.1f%%',
           startangle=90, counterclock=False)
pyplot.show()

# x축 기준각도 90도를 시작으로 시계방향으로 표시, 사과만 강조(분리)
explode_value=(0.1,0,0.1,0,0) # 각각의 부분이 떨어지는 비율
pyplot.figure(figsize=(5,5))
pyplot.pie(result, labels=fruit, autopct='%.1f%%',
           startangle=90, counterclock=False,
           explode=explode_value, shadow=True)
pyplot.show()
