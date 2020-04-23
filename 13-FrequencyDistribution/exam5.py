from pandas import DataFrame
from pandas import read_csv
from matplotlib import pyplot
import stemgraphic

# 데이터 생성
grade_csv = read_csv("data/grade.csv", encoding='euc-kr')

# 전처리 '이름' 컬럼을 인덱스로 설정
grade_df = grade_csv.rename(index=grade_csv['이름']).drop('이름', axis=1)
print(grade_df)
print('-'*30)

# 평균점수 컬럼 추가 : axis=1 -> 행단위
grade_df['평균'] = grade_df.mean(axis=1)
print(grade_df)
print('-'*30)

# 그래프 기본설정
pyplot.rcParams['font.family']='Malgun Gothic'      # 한글 폰트 설
pyplot.rcParams['font.size']=12                    # 글자 크기 설정
pyplot.rcParams['figure.figsize']=(25, 12)             # 그래프의 가로, 세로크기(inch)

# 줄기- 잎 그림 생성하기
stemgraphic.stem_graphic(grade_df['평균'], scale=5)
pyplot.savefig('exam5_file.png', dpi=100) # 그래프 파일에 저장
pyplot.show()




