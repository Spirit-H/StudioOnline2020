# -*- coding: utf-8 -*-
"""
Created on Mon May 11 07:45:32 2020

@author: Spirit H
"""

import random
from functools import reduce

def multiply(x):
    return x*x

def add(x,y):
    return x+y

def chooseElem(x):
    return x%2==0


print('随机生成的列表：' , end = '')
d = {'price':[random.randint(1,10) for i in range(10)]}
print(d)
     
#map函数
print('列表每个元素取平方：' , end = '')
print(list(map(multiply,d['price'])))

#reduce函数
print('列表元素总和：' , end = '')
print(reduce(add,d['price']))

#filter函数
print('筛选出偶数：' , end = '')
print(list(filter(chooseElem,d['price'])))

#sorted函数
print('分别输出小到大和大到小元素排列的列表:')
print(sorted(d['price']))
print(sorted(d['price'] , reverse = True))