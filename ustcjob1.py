# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
 
url = 'http://job.ustc.edu.cn/list.php?MenuID=002001'
front = 'http://job.ustc.edu.cn/'

post_data = {
    'Referer': "http://job.ustc.edu.cn/list.php?MenuID=002001", 
    'User-Agent':"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0"
    } 
return_data = requests.post(url, post_data)
# print return_data.text
soup = BeautifulSoup(return_data.text,'lxml')

job1=soup.find_all(class_="Joplistone")[1]

for job in job1.find_all('li'):
    url = front + job.find('a').get('href')
    name = job.find('a').get_text(strip=True)
    time = job.find(class_ = 'zhiwei').get_text(strip=True)
    place = job.find(class_ = 'zhuanye').get_text(strip=True)
    print name, place,  time
    print  url,'\n'