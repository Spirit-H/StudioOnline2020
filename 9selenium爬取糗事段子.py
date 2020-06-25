# -*- coding: utf-8 -*-
"""
Created on Thu May 21 15:08:16 2020

@author: Spirit H
"""


from selenium import webdriver
from time import sleep

'''通过代码打开浏览器'''
browser = webdriver.Chrome(executable_path = "D:\chromedriver\chromedriver_win32\chromedriver")
'''输入网址等待元素加载并刷新'''
url = 'http://www.qiushibaike.com/text/page/1/'
browser.get(url)
sleep(1)
browser.refresh()
'''获取匹配元素'''
content = browser.find_elements_by_class_name("content")
handle = browser.current_window_handle

text_list = []

for i in content:
    i.click()
    sleep(1)
    handles = browser.window_handles
    for i in handles:
        if i != handle:
            nowhandle = i
    browser.switch_to_window(nowhandle)
    user_name = browser.find_element_by_xpath("//*[@id='articleSideLeft']/a/img")
    user_name = user_name.get_attribute("alt")
    
    text = browser.find_elements_by_class_name("content")[0]
    text_list.append([user_name , text.text])
    sleep(1)
    browser.close()
    browser.switch_to_window(handle)
    sleep(1)
    
    
print('catching...done')
print('downloading...' , end = '')

with open('selenium爬取糗事百科.txt' , 'a' , encoding = 'utf-8') as f:
    for i in text_list:
        f.write('作者名：' + i[0] + '\n')
        f.write('内容' + '\n')
        f.write(i[1])
        f.write('\n'*2)
        
print('done')