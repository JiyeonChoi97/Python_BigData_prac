from matplotlib import pyplot

# 데이터 생성
fruit = ['사과', '바나나', '딸기', '오렌지', '포도']
result = [7,6,3,2,2]

# 한글 설정
pyplot.rcParams['font.family'] = 'Malgun Gothic'
pyplot.rcParams['font.size'] = 10
pyplot.rcParams['figure.figsize'] = (7, 7)

# print(pyplot.rcParams.keys)

# x축 기준각도 90도를 시작으로 시계방향으로 표시, 사과만 강조(분리)
explode_value=(0.1,0,0.1,0,0) # 각각의 부분이 떨어지는 비율
pyplot.pie(result, labels=fruit, autopct='%.1f%%',
           startangle=90, counterclock=False,
           explode=explode_value, shadow=True)
# 그래프 파일에 저장
pyplot.savefig('pi.png', dpi=300) # 출판계 dpi=300설정
pyplot.show()
