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
pyplot.show()

# 히스토그램 보정하기
# bins 리스트의 원소들을 소수점 둘째자리에서 반올림 : round() 함수 이용
for i, v in enumerate(bins):
    # round(값, 소수점 자리) -> 지정된 자리수까지 남기라는 의미 
    bins[i] = round(v, 1)

print(bins)
print('-'*30)

# 히스토그램 출력
pyplot.hist(grade_df['평균'], bins=step, color='blue')
pyplot.grid()
pyplot.xlabel('점수 구간')
pyplot.ylabel('평균점수 구간별 학생수')
pyplot.title('평균점수 구간별 학생수')
# x축의 좌표에 구간별 점수를 출력
# xticks(ticks, labels)
pyplot.xticks(bins, bins)

# 구간별 인원을 텍스트로 출력 : 출력할 데이터 수만큼 반복
for i, v in enumerate(n):
    txt = '%d명' %v
    # 텍스트 출력
    # (x좌표, y좌표, 내용, 글자크기, 색상, 텍스트가로정렬, 세로정렬)
    pyplot.text(bins[i], v, txt, fontsize = 30, color='#ff0000',
                horizontalalignment='left',
                verticalalignment='bottom')
pyplot.savefig('exam2_file.png') # 그래프 파일에 저장
pyplot.show() 





















