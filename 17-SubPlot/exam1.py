from matplotlib import pyplot

# 그래프 기본설정
pyplot.rcParams['font.family']='Malgun Gothic'      # 한글 폰트 설
pyplot.rcParams['font.size']=16                   # 글자 크기 설정
pyplot.rcParams['figure.figsize']=(10, 5)             # 그래프의 가로, 세로크기(inch)

fig = pyplot.figure()
fig.suptitle('서브플루 영역 나누기', fontsize=28, color='#006600')
fig.subplots_adjust(wspace=0.5, hspace=0.5)
ax1 = fig.add_subplot(2,3,1)
ax2 = fig.add_subplot(2,3,2)
ax3 = fig.add_subplot(2,3,3)
ax4 = fig.add_subplot(2,3,4)
ax5 = fig.add_subplot(2,3,5)
ax6 = fig.add_subplot(2,3,6)
pyplot.savefig('exam1_1.png', dpi=100) # 그래프 파일에 저장
pyplot.show()
