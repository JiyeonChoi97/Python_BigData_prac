import requests

simple_text_url = 'http://192.168.0.96/simple_text.txt'

r = requests.get(simple_text_url)
print(r)
print('-'*30)

if r.status_code != 200:
    print('[%d Error] %s' %(r.status_code, r.reason))
    quit()
print(r.encoding)
r.encoding = 'utf-8'
print(r.text)


'''

<Response [200]>
------------------------------
ISO-8859-1
﻿Hello Python~!!!
안녕하세요. 파이썬~!!!
'''

