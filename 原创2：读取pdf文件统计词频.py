# -*- coding: utf-8 -*-
"""
Created on Sat May 16 12:11:32 2020

@author: Spirit H
"""


import PyPDF4
import re

def readPDF(pdf):
    pdfdata = open(pdf , 'rb')#打开pdf文件
    pdfdata = PyPDF4.PdfFileReader(pdfdata)
    return pdfdata    
    
def findword(data , word):
    a = ''
    for i in range(data.numPages):
        content = data.getPage(i).extractText()#获得某页内容（getpage）和文字（extractText）
        a = a + content
    times = len(re.findall('{}'.format(word) , a))#正则找次数
    print('"{}"'.format(word) + '出现的次数为{}次'.format(times))

def checklock(data):
    if data.isEncrypted:
        print('pdf文件被加密')
        return False
    else :
        print('pdf文件未加密')
        return True

def unlock(data):
    data = data.decrypt('rosebud')
    print('成功解密')
    return True

print('请输入pdf文件路径及名称(输入0退出)：')
pdf_file = input()
if pdf_file == '0':
    judge = False
else:
    judge = True

data = readPDF(pdf_file)
if checklock(data):
    judge = True
else:
    judge = unlock(data)

while judge:
    print('请输入需要查询的单词或字母（查找单词请前后用空格隔开,输入0退出）')
    word = input()
    if word == '0':
        break
    
    findword(data , word)
    