from matplotlib import pyplot

# 데이터 생성
result = [79, 86, 93, 72, 92, 88, 79, 100, 65, 70]

# boxplot 그래프 그리기
pyplot.boxplot(result)
pyplot.savefig('exam16_file.png') # 그래프 파일에 저장
pyplot.show()
