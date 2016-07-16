# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
 
url = 'http://www.career.zju.edu.cn/ejob/zczphxxmorelogin.do'
front = 'http://www.career.zju.edu.cn/ejob/'

#查询count条记录
post_data = {
    'Referer': "http://www.career.zju.edu.cn/ejob/zczphxxmorelogin.do", 
    'User-Agent':"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0"
    } 
return_data = requests.post(url, post_data)
# print return_data.text
soup = BeautifulSoup(return_data.text,'lxml')

job1=soup.find_all(class_="result_con")[0]


for job in job1.find_all(class_="con"):
    url = front + job.find('a').get('href')
    name = job.find_all('td')[0].get_text(strip=True)
    time = " ".join(job.find_all('td')[2].get_text(strip=True).split()) 
    place = job.find_all('td')[1].get_text(strip=True)
    print name, place, time
    print  url,'\n'
