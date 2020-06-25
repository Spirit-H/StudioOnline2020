# -*- coding: utf-8 -*-
"""
Created on Thu May  7 10:42:25 2020

@author: Spirit H
"""

import urllib.request as r
import json
import matplotlib.pyplot as plt
import matplotlib.font_manager as f#FontProperties
#import pkg_resources.py2_warn 4全球天气查询.py

font = f.FontProperties(fname = r"c:\windows\fonts\simsun.ttc",size = 15)
w = {'city':[] , 'temp':[]}
print('按1开始查询,按其他键退出')
stt = input()
if stt == '1':
    plt.xlim((0,7))
while stt == '1' :
    print('请输入城市拼音(输入break退出查询):')
    py = input()
    if py == 'break' :
        break
    w['city'].append(py)
    #获取目标当前天气
    url = 'http://api.openweathermap.org/data/2.5/weather?q=' + py + '&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996'
    data=r.urlopen(url).read().decode('utf-8')
    data=json.loads(data)
    #获得目标未来天气
    url2 = 'http://api.openweathermap.org/data/2.5/forecast?q=' + py + ',cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
    data2=r.urlopen(url2).read().decode('utf-8')
    data2=json.loads(data2)
    #获得未来一周温度
    ftemp = [data['main']['temp']]
    for i in range(7):
        ftemp.append(data2['list'][i]['main']['temp'])
    w['temp'].append(ftemp)
    #输出
    print(py + '当前温度：' + str(data['main']['temp']) + '摄氏度')
    print('\n')
    plt.plot(ftemp)
    #plt.legend(loc=2)
    plt.xlabel('天数',fontproperties=font)
    plt.ylabel('摄氏度',fontproperties=font)
    plt.title(py+'未来一周天气',fontproperties=font)
    plt.show()

if stt == '1' and len(w['city']) != 1:   #
    for j in range(len(w['city'])):
        name = w['city'][j]
        plt.plot(w['temp'][j] , label=name)
    plt.legend(loc=2)
    plt.xlabel('天数',fontproperties=font)
    plt.ylabel('摄氏度',fontproperties=font)
    plt.title('未来一周天气比较图',fontproperties=font)

    
        



