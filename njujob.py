# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
 
url = 'http://job.nju.edu.cn:9081/login/nju/home.jsp?type=sxzp&pageNow=1'
front = 'http://job.nju.edu.cn:9081/login/nju/'


post_data = {
	'Referer': "http://job.nju.edu.cn:9081/login/nju/home.jsp?type=sxzp&pageNow=1",
    'User-Agent':"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0"
    } 
return_data = requests.post(url, post_data)

return_data.text.replace(u'\xbb', u' ')
print return_data.text.replace(u'\xef', u' ')

# soup = BeautifulSoup(return_data.text,'lxml')

# job1=soup.find_all(class_="article-lists")[0]

# for job in job1.find_all('li'):
#     url = front + job.find('a').get('href')
#     name = job.find(class_='shortdwmc').get_text(strip=True)
#     time = job.find_all('span')[2].get_text(strip=True)
#     print name , time
#     print  url,'\n'
