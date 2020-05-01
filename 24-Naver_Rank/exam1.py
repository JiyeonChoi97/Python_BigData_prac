import requests
from bs4 import BeautifulSoup as bs
from pandas import DataFrame

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'
session = requests.Session()
session.headers.update({'User-agent':user_agent, 'referer':None})

content_url = 'https://datalab.naver.com/keyword/realtimeList.naver?age=all&where=main'

r = session.get(content_url)

if r.status_code != 200 :
    print('[ERROR]')
    quit()

#print(r.text)
    
soup = bs(r.text, 'html.parser')
    
with open('naver 실시간 검색어.txt', 'w', encoding='utf-8') as f:  #파일로 출력
    f.write(r.text)

selector = soup.select('.item_title_wrap > .item_title')

if not selector:
    print('크롤링 실패')
    quit()
    
#print(selector)

rank_list = []
keyword_list = []

for i, item in enumerate(selector):
    rank_list.append('%02d위' %(i+1))
    keyword_list.append(item.text.strip())

print(rank_list)
print(keyword_list)

df = DataFrame(keyword_list, index=rank_list, columns=['검색어'])
print(df)