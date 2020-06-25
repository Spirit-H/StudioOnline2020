# -*- coding: utf-8 -*-
"""
Created on Mon May 11 20:41:54 2020

@author: Spirit H
"""


import re

with open('weatherData.txt' , 'r' , encoding = 'utf-8') as f:
    file = f.read()
    print('未来五天可能会有{}场雨'.format(len(re.findall('雨' , file))))