import numpy
from pandas import DataFrame
from matplotlib import pyplot
from pandas import read_excel

df = read_excel('data/시도별_월별_교통사고_20200424145200.xlsx')
col_list = list(df.columns)
df_traffic = df.filter(['시도별(1)', '2018. 01', '2018. 02', '2018. 03', '2018. 04', 
                        '2018. 05', '2018. 06', '2018. 07', '2018. 08', 
                        '2018. 09', '2018. 10', '2018. 11', '2018. 12'])
df_traffic.drop(0, inplace=True)
df_traffic = df_traffic.rename(index=df_traffic['시도별(1)']).drop('시도별(1)', axis=1)
dic_month= {'2018. 01':'1월', '2018. 02':'2월', '2018. 03':'3월', '2018. 04':'4월', 
            '2018. 05':'5월', '2018. 06':'6월', '2018. 07':'7월', '2018. 08':'8월', 
            '2018. 09':'9월', '2018. 10':'10월', '2018. 11':'11월', '2018. 12':'12월'}

df_traffic.rename(columns=dic_month, inplace=True)
df_traffic =df_traffic.T
df_traffic.drop(['경기', '강원', '충북', '전북', '제주', '충남', 
                 '전남', '경북', '경남', '광주', '대전', '울산', '세종'], axis=1, inplace=True)

# 그래프 기본설정
pyplot.rcParams['font.family']='Malgun Gothic'      # 한글 폰트 설
pyplot.rcParams['font.size']=20                   # 글자 크기 설정
pyplot.rcParams['figure.figsize']=(10, 6)             # 그래프의 가로, 세로크기(inch)

total = df_traffic.sum()
df_total = DataFrame(total, columns=['교통사고'])
df_total['교통사고'].plot.pie()
pyplot.savefig('exam5_1.png', dpi=100) # 그래프 파일에 저장
pyplot.show()

df_total['교통사고'].plot.pie(labels=['서울', '부산', '대구', '인천'],
                          colors=['#ff6600', '#ff00ff', '#ffff00', '#00ffff'],
                          explode=[0,0,0.1,0],
                          autopct='%.2f%%', shadow=True, startangle=90)
pyplot.title('주요 도시의 1년간 교통사고 비율')
pyplot.ylabel('')
pyplot.savefig('exam5_2.png', dpi=100) # 그래프 파일에 저장
pyplot.show()






