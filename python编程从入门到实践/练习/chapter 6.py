# -*- coding: utf-8 -*-
"""
Created on Thu May 13 09:46:23 2021

@author: zhang
"""
#this is a document for chapter 6
'''
#6-1
mao = {'first_name':'mao','last_name':'mao2','age':'21','city':'shenzhen'}
for k,v in mao.items():
    print('My '+ k +' is '+ v +' !')


#6-2
#笔记：如果字典长度太长直接换行就好了，字典不能用+=语法
favourite_numbers = {'abby':'1','bella':'2','celina':'3',
                     'dad':'4','molly':'5'}
print(favourite_numbers)
for k,v in favourite_numbers.items():
    print(k.title()+"'s favourite number is "+v+"!")


#6-3
computer_languages={'python':'a simple language',
                    'C':'a basic language',
                    'C++':"maybe it's hard",
                    'java':'maybe it is used to bulid website',
                    'R':'it is used in statistic'}
for k,v in computer_languages.items():
    print(k + '\n'+'     '+v + '\n')
'''