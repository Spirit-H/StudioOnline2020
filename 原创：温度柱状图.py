# -*- coding: utf-8 -*-
"""
Created on Sun May 10 11:19:08 2020

@author: Spirit H
"""


import urllib.request as r
import json
import sys

def getTemp(city , day):#传入城市 和 想获取多少温度的天数
    url = 'http://api.openweathermap.org/data/2.5/forecast?q=' + city + ',cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
    data = r.urlopen(url).read().decode('utf-8')
    data = json.loads(data)
    index = judgeTime(data)
    atemp = []
    avgtemp = 0
    #获得第一天的平均天气
    for i in range(7-index+1):
        avgtemp = avgtemp + data['list'][i]['main']['temp']
    atemp.append(avgtemp/(7-index+1))
    #若天数>1
    if day > 1:
        for j in range(day-1):
            avgtemp = 0
            for i in range(8):
                avgtemp += data['list'][8-index+8*j+i]['main']['temp']
            atemp.append(avgtemp/8)
    #返回未来每天平均温度
    return atemp

def judgeTime(data):
    text = data['list'][0]['dt_txt']
    text = list(text)
    t = text[11:13]
    for i in range(8):
        if i < 4:
            a = str(3*i)
            if t == ['0',a]:
                return i
        else :
            if i < 7:
                a = str(3*i-10)
                if t == ['1',a]:
                    return i
            else :
                a = str(3*i-20)
                if t == ['2',a]:
                    return i

def buildChart(tempList):
    print('-'*(8*len(tempList)-4))
    for j in range(int(max(tempList))+1):#行
        for i in range(len(tempList)):#列
            if j < (max(tempList)-tempList[i]):
                print(' '*4 , end = '')
            else:print('|'*4 , end = '')
            print(' '*4 , end = '')
        print()
    print('今天'+' '*3 , end = '')
    if len(tempList)>1:
        for i in range(len(tempList)-1):
            print('未来{}天'.format(str(i+1)) , end = '')
            print(' '*2 , end = '')
    print()
    for i in range(len(tempList)):
        print(str(round(tempList[i] , 2))+' '*3 , end = '')
    print()
    print('-'*(8*len(tempList)-4))

print('请输入查询城市的拼音(输入0退出)：' , end = '')
city = input()
if city == '0':
    sys.exit()
print('请输入查询天数(输入0退出)：' , end = '')
day = input()
if day == '0':
    sys.exit()
a = getTemp(city,int(day))
buildChart(a)