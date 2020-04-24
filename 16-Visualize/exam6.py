import numpy
from pandas import DataFrame
from matplotlib import pyplot

data = {
        '기온':[23,25,26,27,28,29,30,31,33],
        '판매량':[2100,2300,2500,2800,3300,3500,3600,3700,3900]
        }

df = DataFrame(data)

# 그래프 기본설정
pyplot.rcParams['font.family']='Malgun Gothic'      # 한글 폰트 설
pyplot.rcParams['font.size']=16                   # 글자 크기 설정
pyplot.rcParams['figure.figsize']=(10, 6)             # 그래프의 가로, 세로크기(inch)

df.plot.scatter(x='기온', y='판매량', color='#ff6600',
                 marker='X', label='판매수량')
pyplot.grid()
pyplot.title('기온과 아이스크림 판매량의 상관관계')
pyplot.ylabel('아이스크림 판매수량')
pyplot.savefig('exam6_1.png', dpi=100) # 그래프 파일에 저장
pyplot.show()

df.plot.scatter(x='판매량', y='기온', color='#ff6600',
                 marker='X', label='판매수량')
pyplot.grid()
pyplot.title('기온과 아이스크림 판매량의 상관관계')
pyplot.xlabel('아이스크림 판매수량')
pyplot.savefig('exam6_2.png', dpi=100) # 그래프 파일에 저장
pyplot.show()





