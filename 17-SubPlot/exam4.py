import numpy
from pandas import DataFrame
from matplotlib import pyplot
from pandas import read_excel

df = read_excel('data/시도별_월별_교통사고_20200424145200.xlsx')
df_traffic = df.filter(['시도별(1)', '2018. 01', '2018. 02', '2018. 03', '2018. 04', 
                        '2018. 05', '2018. 06', '2018. 07', '2018. 08', 
                        '2018. 09', '2018. 10', '2018. 11', '2018. 12'])

df_traffic.drop(0, inplace=True)    # '발생건수'삭제 


df_traffic = df_traffic.rename(index=df_traffic['시도별(1)']).drop('시도별(1)', axis=1)

dic_month= {'2018. 01':'1월', '2018. 02':'2월', '2018. 03':'3월', '2018. 04':'4월', 
            '2018. 05':'5월', '2018. 06':'6월', '2018. 07':'7월', '2018. 08':'8월', 
            '2018. 09':'9월', '2018. 10':'10월', '2018. 11':'11월', '2018. 12':'12월'}

df_traffic.rename(columns=dic_month, inplace=True)
df =df_traffic.T

df.drop(['경기', '강원', '충북', '전북', '제주', '충남', 
                 '전남', '경북', '경남', '광주', '대전', '울산', '세종'], axis=1, inplace=True)

# 그래프 기본설정
pyplot.rcParams['font.family']='Malgun Gothic'      # 한글 폰트 설
pyplot.rcParams['font.size']=16                   # 글자 크기 설정
pyplot.rcParams['figure.figsize']=(20,10)             # 그래프의 가로, 세로크기(inch)

fig = pyplot.figure()
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)

fig.suptitle('2018년 교통사고 현황', fontsize=28, color='#00ff00')
fig.subplots_adjust(wspace=0.2, hspace=0.3)

df.plot(ax=ax1, color=['#66ff00', '#ff6600', '#ff0000', '#00ffff'])
ax1.grid()
ax1.title.set_text('2018년 서울, 부산, 대구, 인천의 교통사고')
ax1.title.set_fontsize(22)
ax1.title.set_color('#ff00ff')
ax1.set_xticks(list(range(0, 12)))
ax1.set_xticklabels(list(df.index), fontsize=12, color='#ff0000')
ax1.set(xlabel='월', ylabel='교통사고 수 ')
ax1.set_xlim([-0.5, 11.5])
ax1.set_ylim([0, 3500])

df.plot.bar(ax=ax2, rot=0,  color=['orange', 'red', 'pink', 'purple'])
ax2.grid()
ax2.title.set_text('2018년 서울, 부산, 대구, 인천의 빈도')
ax2.title.set_fontsize(22)
ax2.title.set_color('#00f0ff')
ax2.set_xticks(list(range(0, 12)))
ax2.set_xticklabels(list(df.index), fontsize=12, color='#ff0000')
ax2.set(xlabel='월', ylabel='교통사고 수 ')


df['서울'].plot.pie(ax=ax3, labels=df.index, autopct='%.1f%%',
                  textprops={'color':'#000000', 'fontsize':12})
ax3.title.set_text('서울의 월별 교통사고 비율')
ax3.set(ylabel=None)
ax3.legend(labels=df.index, title='범주', bbox_to_anchor=(1, 1.15 ))


df.plot.scatter(x='서울', y='부산', ax=ax4, color='#ff6600',
                label='교통사고', marker='X')
ax4.title.set_text('서울과 부산의 교통사고 관계')
ax4.set(xlabel='서울', ylabel='부산')
pyplot.savefig('exam4_1.png', dpi=100) # 그래프 파일에 저장
pyplot.show()

