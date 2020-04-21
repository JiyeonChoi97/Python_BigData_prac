from pandas import DataFrame

# 딕셔너리를 원소로 갖는 리스트
grade_data = [
                {'국어':98, '영어':None, '수학':88, '과학':64},
                {'국어':88, '영어':90, '수학':62, '과학':72},
                {'국어':92, '영어':70, '수학':None, '과학':None},
                {'국어':63, '영어':60, '수학':31, '과학':70},
                {'국어':120, '영어':50, '수학':None, '과학':88}
             ]


# 딕셔너리의 키가 컬럼이름으로 사용되므로, 인덱스만 지정
df = DataFrame(grade_data, index=['철수', '영희', '민철', '수현', '호영'])
print(df)
print('-'*30)

# 1. 특정행 삭제하기
# inplace 속성을 설정하지 않으면, 원본은 그대로 있음
d1 = df.drop('철수')
print(d1)
print('-'*30)

# 2. 여러 행 삭제하기
d2 = df.drop(['철수', '영희', '수현'])
print(d2)
print('-'*30)

# 3. 인덱스 번호를 통한 특정 위치의 행 삭제 
d3 = df.drop(df.index[0])   # 0번째 행 삭제
print(d3)
print('-'*30)

# 4. 슬라이싱을 통한 범위 내의 행 삭제하기
d4 = df.drop(df.index[1:4])
print(d4)
print('-'*30)

# 5. 삭제 결과를 원본에 반영하기
df.drop(df.index[1:4], inplace = True)
print(df)
print('-'*30)


