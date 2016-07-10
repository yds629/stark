# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
 
url = 'http://www.career.fudan.edu.cn/jsp/career_talk_list.jsp'
front = 'http://www.career.fudan.edu.cn/html/xjh/1.html?view=true&key='

#查询count条记录
post_data = {
    'count':'100',
    'list':'true',
    'Referer': "http://www.career.fudan.edu.cn/jsp/career_talk_list.jsp?count=20&list=true&page=1", 
    'Host':"www.career.fudan.edu.cn",
    'User-Agent':"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0"
    } 
return_data = requests.post(url, post_data)
#print return_data.text
soup = BeautifulSoup(return_data.text)
for job in soup.find_all(id = 'tab1_bottom'):
    url = front + job.get('key')
    name = job.find(class_ = 'tab1_bottom1').get_text()
    types = job.find(class_ = 'tab1_bottom2').get_text()
    date = job.find(class_ = 'tab1_bottom3').get_text()
    time = job.find(class_ = 'tab1_bottom4').get_text()
    place = job.find(class_ = 'tab1_bottom5').get_text()
    print name, types, place, date, time
    print  url,'\n'

