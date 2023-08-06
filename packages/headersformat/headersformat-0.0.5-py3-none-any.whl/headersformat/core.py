#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/9/14 18:29
# @Author  : jia666666
# @FileName: headers一键格式化.py
from __future__ import print_function #兼容python2的print
import re
import pyperclip
from .colors import red,green,yellow,white,good,run
def printWelcomeMessage():
    "打印欢迎语"
    WelcomeMessage="""
        __                   __                  ____                           __
       / /_  ___  ____ _____/ /__  __________   / __/___  _________ ___  ____ _/ /_
      / __ \/ _ \/ __ `/ __  / _ \/ ___/ ___/  / /_/ __ \/ ___/ __ `__ \/ __ `/ __/
     / / / /  __/ /_/ / /_/ /  __/ /  (__  )  / __/ /_/ / /  / / / / / / /_/ / /_
    /_/ /_/\___/\__,_/\__,_/\___/_/  /____/  /_/  \____/_/  /_/ /_/ /_/\__,_/\__/
    """
    print(f'''{red}{WelcomeMessage}''')


def headers_format():
    """headers格式化函数"""
    printWelcomeMessage() #打印欢迎语
    print(f'{run}请输入要格式化的headers，回车两次结束')
    string = ''
    for s in iter(input, ''):  # 空字符串是结束标记
        s = re.sub("(.*?):[\s]{0,1}(.*)", r"'\1': '\2',", s)  # 正则提取内容
        string += ('\t'+s + '\n')
    headers='headers = {\n' + string + '}'
    pyperclip.copy(headers)  # 复制到剪切板
    print(f'''{green}{headers}''')
    print(f'{good}已经复制到剪切板') # 控制台先输出，方便检视，与剪切板的内容一样
if __name__ == '__main__':
    headers_format()