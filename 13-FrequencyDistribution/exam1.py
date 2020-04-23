from pandas import DataFrame
from pandas import read_csv
from matplotlib import pyplot

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

# 자료의 갯수를 센다.
count = len(grade_df['평균'])
print(count)
print('-'*30)

# 최대/최소값 구하기
max_value = grade_df['평균'].max()
min_value = grade_df['평균'].min()
print(max_value)
print(min_value)
print('-'*30)

# 몇개 구간으로 나눌지 결정한다.
step = 5

# 히스토그램 생성하기
# 그래프에 대한 기본설정
pyplot.rcParams['font.family']='Malgun Gothic'      # 한글 폰트 설
pyplot.rcParams['font.size']=20                    # 글자 크기 설정
pyplot.rcParams['figure.figsize']=(15,8)             # 그래프의 가로, 세로크기(inch)

# 히스토그램 작성
n, bins, patches = pyplot.hist(grade_df['평균'], bins=step)
pyplot.savefig('exam1_file.png') # 그래프 파일에 저장
pyplot.show()

# 리턴값 확인
# n : 각 구간의 데이터 갯수 [538. 1491. 4279. 1694. 1998.]
print(n)
print('-'*30)

# bins : 각 구간의 경계치
# bins : [15.  30.7 46.4 62.1 77.8 93.5]
print(bins)
print('-'*30)

# patches : 그래프를 표현하는데 사용되는 객체들
# <a list of 5 Patch objects>
# -> 사용안함 
print(patches)
print('-'*30)







