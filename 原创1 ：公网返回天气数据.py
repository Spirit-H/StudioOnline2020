# -*- coding: utf-8 -*-
"""
Created on Fri May 15 20:19:20 2020

@author: Spirit H
"""

import json
import urllib.request as r
import re
from flask import Flask
app = Flask(__name__)

@app.route('/')
def weather():
    a = ['beijing' , 'tianjin' , 'shanghai' , 'chongqing' , 'xianggang' ,  
     'guangzhou' , 'shaoguan' , 'shenzhen' , 'maoming' , 'zhuhai' , 'shantou' , 
     'foshan' , 'jiangmen' , 'zhanjiang' , 'huizhou' , 'meizhou' , 'heyuan' , 
     'yangjiang' , 'qingyuan' , 'dongguan' , 'zhongshan' , 'chaozhou' , 'jieyang' , 
     'nanning' , 'liuzhou' , 'guilin' , 'wuzhou' , 'beihai' , 'yulin' , 'changsha']

    #print(len(a))

    d = []
    for city in a:
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996'.format(city)
        data = r.urlopen(url).read().decode('utf-8')
        city = re.findall('"name":"(.*?)"' , data)
        temp = re.compile('"temp":(.*?),').findall(data)
        l = city+temp
        d.append(l)
        print('{}...done'.format(city[0]))    
    
    d = json.dumps(d)
    return d

if __name__ == '__main__':
    app.run()