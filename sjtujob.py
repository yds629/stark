# -*- coding:utf-8 -*-
import requests
import re
from bs4 import BeautifulSoup
 
url = 'http://www.job.sjtu.edu.cn/eweb/jygl/zpfw.so?type=xjh'
front = 'http://www.job.sjtu.edu.cn/eweb/jygl/zpfw.so?modcode=jygl_xjhxxck&subsyscode=zpfw&type=viewXjhxx&id='

#查询count条记录
post_data = {
    'Referer': "http://www.job.sjtu.edu.cn/eweb/jygl/zpfw.so?type=xjh", 
    'User-Agent':"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0"
    } 
return_data = requests.post(url, post_data)
# print return_data.text
soup = BeautifulSoup(return_data.text,'lxml')

job1=soup.find_all(id="tbc5_05_4")[0]

pattern = re.compile('\'(.*?)\'',re.S)

for job in job1.find_all(class_="zp_llb"):
    items = re.findall(pattern,job.find('a').get('onclick'))
    url = front + items[0]
    name = job.find_all('li')[0].get_text(strip=True)
    time = job.find_all('li')[2].get_text(strip=True) + ' ' + job.find_all('li')[3].get_text(strip=True)
    place = job.find_all('li')[1].get_text(strip=True)
    print name, place, time
    print  url,'\n'
