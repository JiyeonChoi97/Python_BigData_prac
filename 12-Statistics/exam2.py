from pandas import DataFrame
from pandas import read_csv
from matplotlib import pyplot

# 성적표 데이터
grade_csv = read_csv("data/grade.csv", encoding='euc-kr')
print(grade_csv.head())
print(grade_csv.tail())
print('-'*30)

# 전처리
# '이름' 열을 인덱스로 사용
name = {}
for i, v in enumerate(list(grade_csv['이름'])):
    name[i] = v

grade_df = grade_csv.rename(index=name)
print(grade_df)
print('-'*30)

# '이름' 컬럼 삭제
grade_df.drop('이름', axis=1, inplace=True)
print(grade_df)
print('-'*30)

# 1. 전체 컬럼에 대한 요약통계량 일괄 확인
des = grade_df.describe()
print(des)
print('-'*30)

# 2. 특정 컬럼에 대한 요약 통계량 확인
desc_kor = grade_df['국어'].describe()
print(desc_kor)
print(type(desc_kor))
print('-'*30)

# 3. 요약 통계량 시각화 : boxplot
# 최대, 최소, 사분위수

# pyplot 객체 기본 환경 설정
pyplot.rcParams['font.family']='Malgun Gothic'      # 한글 폰트 설
pyplot.rcParams['font.size']=14                     # 글자 크기 설정
pyplot.rcParams['figure.figsize']=(8,6)             # 그래프의 가로, 세로크기(inch)

# 전체 데이터프레임의 상자그림 생성
grade_df.boxplot()
pyplot.savefig('exam2_file.png') # 그래프 파일에 저장
pyplot.show()

# 특정 컬럼만을 상자그림으로 표시
grade_df.boxplot(['국어', '수학'])
pyplot.savefig('exam2_file_korea+math.png', dpi=200) # 그래프 파일에 저장
pyplot.show()







