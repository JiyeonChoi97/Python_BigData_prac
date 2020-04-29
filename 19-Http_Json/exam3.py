import requests
import json
from pandas import DataFrame
from matplotlib import pyplot

json_list_url = 'http://192.168.0.96/student.json'

r = requests.get(json_list_url)

if r.status_code != 200:
    print('[%d Error] %s' %(r.status_code, r.reason))
    quit()
    
result = json.loads(r.text)
print(result)
print('-' * 30)

df = DataFrame(result['student'])
print(df)
print('-' * 30)

score_df = df.rename(index=df['name'],
                     columns={'eng':'영어', 'kro':'국어', 'math':'수학'})
print(score_df)
print('-' * 30)

# 그래프 기본설정
pyplot.rcParams['font.family']='Malgun Gothic'      # 한글 폰트 설
pyplot.rcParams['font.size']=16                   # 글자 크기 설정
pyplot.rcParams['figure.figsize']=(14,8)             # 그래프의 가로, 세로크기(inch)

score_df.plot.bar(rot=0)
pyplot.grid()
pyplot.title('학생별 시험 점수')
pyplot.xlabel('학생명')
pyplot.ylabel('점수')
pyplot.savefig('exam3.png', dpi=100) # 그래프 파일에 저장
pyplot.show()







