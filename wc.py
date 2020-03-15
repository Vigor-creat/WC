#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import os


#基本功能

# 功能c
def Character_count(file_path):  # 统计字符数

    file = open(file_path, 'r', encoding='utf-8') 

    character_count = str(len(file.read())) #file.read()将文件全部数据作为字符串返回，包括换行符。

    return character_count



#功能w
def Word_count(file_path):  # 统计单词数

    with open(file_path, 'r', encoding = 'utf-8') as f:

        flie_dict = {} # 读取文件后得到一个可迭代对象file_dict。
        
        word_count = 0

        for line in f.readlines():

            array_match = re.findall('[a-zA-Z]+', line) # 正则表达式re.findall作用返回line中的字符串，并组成一个新的数组。

            word_count = len(array_match) + word_count # 将每一行构建的数组的元素值累加。

    return word_count



#功能l
def Line_count(file_path): # 统计行数

    file = open(file_path, 'r', encoding = 'utf-8') # r只读，w可写，a追加。

    lines = len(file.readlines()) # file.readlines()读取文件所有内容，按行为单位放到一个列表中，返回list类型。

    return lines


#扩展功能

#功能s
def get_file_path(dir_name): # 获取测试文件夹下所有文件地址

    list_path = [] # 创建一个地址列表存储测试文件夹下所有文件地址   

    for root,dirs,files in os.walk(dir_name): 

        for file in files:  

            path = os.path.join(root,file)
            
            list_path.append(path) # list_path.append()函数用于添加列表元素

    return list_path

def get_file_name(dir_name): 

    list_file_name = [] # 创建一个文件名列表存储测试文件夹下所有文件对应的文件名

    for root,dirs,files in os.walk(dir_name): 

        for file in files:  

            list_file_name.append(file)  

    return list_file_name


if __name__ == "__main__":    #主函数  

    dir_path = input('请输入文件夹路径：') 

    list_path = get_file_path(dir_path)

    list_file_name = get_file_name(dir_path)

    for i in range(len(list_path)):
        
        print('文件%s中的字符数：%s' % (list_file_name[i], Character_count(list_path[i])))

        print('文件%s中的单词数：%d' % (list_file_name[i], Word_count(list_path[i])))

        print('文件%s中的行数：%d\n' % (list_file_name[i], Line_count(list_path[i])))

#功能a

