from pandas import DataFrame
import numpy

# 서울, 부산, 인천의 5년 단위 인구 분포
city_people = {
        '도시':['서울', '서울', '서울', '부산', '부산', '부산', '인천', '인천'],
        '연도':['2015', '2010', '2005', '2015', '2010', '2005', '2015', '2010'],
        '인구':[9904312, 9631482, 9762546, 3448737, 3393191, 3512547, 2890451, 2632035],
        '지역':['수도권', '수도권', '수도권', '경상권', '경상권', '경상권', '수도권', '수도권']
    }

# 1. 데이터프레임 생성
census = DataFrame(city_people)
print(census)
print('-'*30)

# 2. 피벗테이블 : 각 도시별 연도에 따른 인구수
# pivot(index, columns, values)
pv1 = census.pivot('도시', '연도', '인구')
print(pv1)
print('-'*30)

# 열과 행의 구성 확인
print(pv1.columns)
print(pv1.index)
print('-'*30)

# 3. 피벗테이블 생성 제약
# -> 컬럼과 인덱스 이름으로 사용되는 데이터의 쌍이 중복되는 경우가 있다면 에러 

# 지역과 연도에 대한 조합은 두쌍이 나타나므로 에러 
#pv2 = census.pivot('지역', '연도', '인구')
#print(pv2)

# 4. 그룹분석 결과를 피벗테이블로 조합하기 
# -> 각지역의 인도별 평균 인구수를 피벗테이블로 생성
# 집계 대상을 추출
filter_df = census.filter(['지역', '연도', '연구'])
print(filter_df)
print('-'*30)

# 그룹 분석
group_df = filter_df.groupby([filter_df['지역'], filter_df['연도']], as_index=False).mean()
print(group_df)
print('-'*30)

# 피벗 테이블 분석
pivot_df = group_df.pivot('지역', '연도', '인구')
print(pivot_df)
print('-'*30)






