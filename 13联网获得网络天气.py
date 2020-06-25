# -*- coding: utf-8 -*-
"""
Created on Thu May  7 02:31:17 2020

@author: Spirit H
"""

import urllib.request as r
#当前天气
url='http://api.openweathermap.org/data/2.5/weather?q=maoming&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996'
#未来5天天气
url2='http://api.openweathermap.org/data/2.5/forecast?q=maoming,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'

data=r.urlopen(url).read().decode('utf-8')
data2=r.urlopen(url2).read().decode('utf-8')

import json
data=json.loads(data)
data2=json.loads(data2)

print('当前温度：'+str(data['main']['temp'])+'摄氏度')
a=[data['main']['temp']]
for i in range(5):
    a.append(data2['list'][i]['main']['temp'])
    
    
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties#字体管理器
font = FontProperties(fname = r"c:\windows\fonts\simsun.ttc",size = 15)
plt.plot(a)
plt.legend(loc=2)
plt.xlabel('天数',fontproperties=font)
plt.ylabel('摄氏度',fontproperties=font)
plt.title('未来五天天气',fontproperties=font)
plt.xlim((0,5))
print(plt.plot(a))


