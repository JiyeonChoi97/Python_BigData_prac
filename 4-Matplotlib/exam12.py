from matplotlib import pyplot
import numpy
import matplotlib

# 데이터 생성
member_IDs = ['m01', 'm02', 'm03', 'm04'] # 회원 
ex_before = [27, 35, 40, 33]   # 운동 시작전
ex_after = [30, 38, 42, 37]    # 운동 한달 후

# 한글 설정
matplotlib.rcParams['font.family'] = 'Malgun Gothic'

# 막대그래프 출력
mem_num = len(member_IDs)  # 회원수 = 4
index = numpy.arange(mem_num) 
pyplot.bar(index, ex_before)
pyplot.show()

# 막대의 색상 지정
colors = ['r', 'g', 'b', 'c']
pyplot.bar(index, ex_before, width=0.6, color=colors,
           tick_label=member_IDs)
pyplot.show()

# 가로 막대바 출력
pyplot.barh(index, ex_before, height=0.6, color=colors, 
            tick_label=member_IDs)
pyplot.show()

# 막대바를 두개 같이 출력하기
# align = 'edge' : 막대그래프를 한쪽으로 치우치게 한다.
# label : 범례에 출력시킬 문자열 설정
barWidth = 0.4
pyplot.bar(index, ex_before, width=barWidth, color='c',
           label='before')
pyplot.show()

pyplot.bar(index, ex_before, width=barWidth, color='c',
           label='before', align='edge')
pyplot.bar(index+barWidth, ex_after, width=barWidth, color='m',
           label='after', align='edge')
# 범례 출력
pyplot.legend()
# x축 눈금을 회원아이디로 변경
pyplot.xticks(index+barWidth, member_IDs)



pyplot.xlabel('회원 ID')
pyplot.ylabel('윗몸일으키기 횟수')
pyplot.title('운동 시작전과 후의 근지구력(복근) 변화비교')
pyplot.show()















