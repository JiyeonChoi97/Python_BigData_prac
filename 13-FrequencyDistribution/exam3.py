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

# 몇개 구간으로 나눌지 결정한다.
step = 5

# 히스토그램 작성
n, bins, patches = pyplot.hist(grade_df['평균'], bins=step)

# 도수분포표 만들기
idx = []
for i in range(0, len(bins) - 1):
    k = '%.1f~%.1f' %(bins[i], bins[i+1])
    idx.append(k)

print(idx)
print('-'*30)

# 데이터 프레임 만들기
df = DataFrame(n, index=idx, columns=['빈도'])
print(df)

pyplot.savefig('exam3_file.png') # 그래프 파일에 저장

