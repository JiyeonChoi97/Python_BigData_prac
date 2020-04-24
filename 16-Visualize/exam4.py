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
pyplot.rcParams['font.size']=16                    # 글자 크기 설정
pyplot.rcParams['figure.figsize']=(10, 6)             # 그래프의 가로, 세로크기(inch)

df_traffic['서울'].plot.barh(color='#8046EB', rot=45, width=0.7)
pyplot.grid()
pyplot.legend()
pyplot.title('2018년 서울의 월별 교통사고')
pyplot.xlabel('월')
pyplot.ylabel('교통사고 수 ')
pyplot.xlim(2500, 3700)
for i, v in enumerate(list(df_traffic['서울'])):
    txt = '%d건' %v
    pyplot.text(v, i, txt, fontsize=14, color='#ff0000', horizontalalignment='left',
                verticalalignment='center')
pyplot.savefig('exam4_1.png', dpi=100) # 그래프 파일에 저장
pyplot.show()

df_traffic.plot.barh(rot=0, width=0.7)
pyplot.xlim(0, 4300)
pyplot.legend(bbox_to_anchor=(1, 0.65))
pyplot.title('2018년 서울의 월별 교통사고')
pyplot.xlabel('월')
pyplot.ylabel('교통사고 수 ')
pyplot.savefig('exam4_2.png', dpi=100) # 그래프 파일에 저장
pyplot.show()




