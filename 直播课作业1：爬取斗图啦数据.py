# -*- coding: utf-8 -*-
"""
Created on Sun May 17 11:54:34 2020

@author: Spirit H
"""


import requests
from lxml.etree import HTML
from wget import download
import re
import time
import urllib.request as r

'''
for i in range(1590,2001):
    url = 'http://www.doutula.com/photo/list/?page={}'.format(i+1)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
    response = requests.get(url , headers = headers)
    selector = HTML(text = response.text)
    str_path = '//*[@id="pic-detail"]/div/div[2]/div[2]/ul/li/div/div/a[.]/img/@alt' 
    img_path = '//*[@id="pic-detail"]/div/div[2]/div[2]/ul/li/div/div/a[.]/img/@data-original'
    img_str = selector.xpath(str_path)
    img_path = selector.xpath(img_path)

    with open('text1001~2001.txt' , 'a' , encoding = 'utf-8') as f:            
        f.write('page {}'.format(i+1) + '\n')
        for j in img_str:
            f.write(j + '\n')
        f.write('\n')
    
    with open('img_path1001~2001 .txt' , 'a' , encoding = 'utf-8') as f:
        for j in range(len(img_path)):
            f.write(img_path[j] + '\n')
            #pic_path = img_path[i].split('/')[-1]
            #download(img_path[i] , 'images/{}'.format(pic_path))            
    
    print('page {} ...done'.format(i+1))

'''    
def dl_imgs(index):
    with open('Pic_URL.json' , 'r' , encoding = 'utf-8') as f:
        
        l = f.readlines()
    
    try:
        for i in range(index ,len(l)):
            url = re.findall('(.*?)\n' , l[i])[0]
            t = url.split('/')[-1]
        #print(t)
            download(url , 'images/{}'.format(t))
            print('{}...'.format(i+1) + t + '...done')
            time.sleep(0.2 )
    except Exception:
        print('{}连接超时，正在重新下载'.format(t))
        dl_imgs(i)
    
dl_imgs(12491)

        

        

