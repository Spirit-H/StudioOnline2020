# -*- coding: utf-8 -*-
"""
Created on Fri May 15 21:12:23 2020

@author: Spirit H
"""


import urllib.request as r
import re
from lxml.html import etree

print('输入爬取的页数：' , end = '')
num = input()
print('输入数据保存的地址(如：D:\文件夹名\所要保存的文件名 , 默认保存在当前程序位置，文件名必填)')
ads = input()
print('数据收集中')
for a in range(int(num)):
    
    url = 'https://www.qiushibaike.com/text/page/{}/'.format(a+1)
    response = r.Request(url , headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 1' 
                                      '0.0; Win64; x64) AppleWebKit/537.36 (KHTML'
                                      ', like Gecko) Chrome/81.0.4044.138 Safari/537.36'})
    data = r.urlopen(response).read().decode('utf-8')
    data2 = etree.HTML(data)
    data2 = data2.xpath('//div[@class="content"]/span/text()')

    l = []
    for i in data2: 
        if i == '查看全文':
            continue
        data3 = re.findall('\n*(.*?)\n*' , i)
        for j in data3:
            l.append(j)
        if len(re.findall('\n' , i)) == 2:
            l.append('\n')
            l.append('\n')
    with open('{}.txt'.format(ads) , 'a' , encoding = 'utf-8') as f:
        for i in l:
            f.write(i)
    print('第{}页完成'.format(a+1))
    
print('信息获取成功')