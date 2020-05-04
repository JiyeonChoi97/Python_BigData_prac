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

#print(url_list)
#print(len(url_list))

datetime = dt.datetime.now().strftime('%y%m%d_%H%M%S')
print(datetime)
dirname = '뉴스기사_%s' %datetime

#print(dirname)

# 폴더 만들기
if not os.path.exists(dirname):
    os.mkdir(dirname)

for i, url in enumerate(url_list):
    print('%d번째 뉴스기사 수집중.... >> %s' %(i+1, url))
    
    r = session.get(url)
    if r.status_code != 200:
        print('[Error]')
        continue
    
    soup = bs(r.text, 'html.parser')
    
    main_content = soup.select('#main_content')
    
    ''' 뉴스 제목 뽑아오기 '''
    
    title = main_content[0].select('#articleTitle')
    
    title_str = title[0].text.strip()
    
    # 기사 제목에 있는 특수문자 제거
    title_str = title_str.replace("'", "")
    title_str = title_str.replace("\"", "")
    title_str = title_str.replace("?", "")
    title_str = title_str.replace("/  ", "")
    title_str = title_str.replace(">", "")
    title_str = title_str.replace("<", "")
    #print(title_str)
    
    ''' 뉴스 내용 뽑아오기 '''
    article = main_content[0].select("#articleBodyContents")
    article_item = article[0]
    
    for target in article_item.find_all('script') : target.extract()
    for target in article_item.find_all('a') : target.extract()
    for target in article_item.find_all('span') : target.extract()
    for target in article_item.find_all('div') : target.extract()
    for target in article_item.find_all('br') : target.replace_with('\n')
    
    article_str = article_item.text.strip()
    #print(article_item)
    
    if title_str and article_str:
        fname = dirname + '/' + str(i+1) + '_' + title_str + '.txt'
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(article_str)
            print(" >> 파일저장 성공 : " + fname)


































