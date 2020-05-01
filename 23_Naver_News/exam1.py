import requests
from bs4 import BeautifulSoup as bs

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'
session = requests.Session()
session.headers.update({'User_agent':user_agent, 'referer':None})

content_url = 'https://news.naver.com/main/ranking/read.nhn?mid=etc&sid1=111&rankingType=popular_day&oid=055&aid=0000811630&date=20200501&type=2&rankingSectionId=101&rankingSeq=4'

r = session.get(content_url)

if r.status_code != 200 :
    print('[ERROR]')
    quit()

#print(r.text)

with open('naver 뉴스.txt', 'w', encoding='utf-8') as f:  #파일로 출력
    f.write(r.text)

soup = bs(r.text, 'html.parser')

selector = soup.select('#articleBodyContents')

if not selector:
    print('크롤링 실패')
    quit()
    
print(selector)











