# -*- coding:utf-8 -*-

'''
功能：下载网页上所有图片，框架无问题，规则自定义
'''

from urllib import request
from bs4 import BeautifulSoup
import re, time, os

url = r'https://lankning.github.io/2020/10/18/%E5%AD%A6%E7%A7%91%E7%AC%94%E8%AE%B0/%E7%BA%A2%E5%AE%9D%E4%B9%A6%E5%BF%85%E8%80%83%E8%AF%8D/'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
page = request.Request(url, headers=headers)
page_info = request.urlopen(page).read().decode('utf-8')
soup = BeautifulSoup(page_info, 'html.parser')

# Beautiful Soup和正则表达式结合，提取出所有图片的链接（img标签中，class=**，以.jpg结尾的链接）
links = soup.find_all('img',src=re.compile(r'.jpg$'))
# print(links)
# 设置保存的路径，否则会保存到程序当前路径
local_path = r'pics'
if bool(1-os.path.exists(local_path)):
    os.mkdir(local_path)


for link in links:
    if ('http' in link.attrs['src']):
        print("skip.")
    else:
        print(link.attrs['src'])
        url = 'https://lankning.github.io'+link.attrs['src']
        # 保存链接并命名，time防止命名冲突
        name = url.split('/')[-1]
        request.urlretrieve(url, local_path+r'\%s.jpg' % time.time())