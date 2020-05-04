import requests
import os
import datetime as dt
from bs4 import BeautifulSoup as bs

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'
session = requests.Session()
session.headers.update({'User_agent':user_agent, 'referer':None})

content_url = 'https://news.naver.com/'

r = session.get(content_url)

if r.status_code != 200 :
    print('[ERROR]')
    quit()

#print(r.text)

soup = bs(r.text, 'html.parser')
selector = soup.select('.lnk_hdline_main_article, .lnk_hdline_article,'
                       + '.mtype_img > dt > a, .mlist2 > li > a')

if not selector:
    print('크롤링 실패')
    quit()
    
#print(selector)

url_list = []
for item in selector:
    if 'href' in item.attrs:
        url_list.append(item['href'])

for i, v in enumerate(url_list):
    if 'https://news.naver.com' not in v :
        url_list[i] = 'https://news.naver.com' + v

print(url_list)
print(len(url_list))

