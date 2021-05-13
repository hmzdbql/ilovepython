# -*- coding: utf-8 -*-
"""
Created on Thu May 13 09:46:23 2021

@author: zhang
"""
#this is a document for chapter 6

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

#6-4
computer_languages['a']='no.1'
computer_languages['b']='no.2'
computer_languages['c']='no.3'
print(computer_languages)


#6-5
#这里出现了个错误，将三个print并排了，这个使得输出的内容是分开的，不是按类连续的
#.keys和.values简直是两个鸡肋函数，我直接用第一种写法不好吗？
rivers = {'nile':'egypt','changjiang':'china','huanghe':'china'}
for k,v in rivers.items():
    print('The '+k.title()+' runs through '+v.title())
    
print('\n')
for river in rivers.keys():
    print('The famous rivers in the world are:'+river.title())
    
print('\n')
for country in rivers.values():
    print('These rivers in there:'+country.title())


#6-6
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }
persons = ['jen','sarah','maomao']
for person in persons:
    if person in favorite_languages.keys():
        print(person.title()+' , thanks for your help!')
    if person not in favorite_languages.keys():
         print(person.title()+' , please help us.')

#6-7
mao = {'first_name':'mao','last_name':'mao2','age':'21','city':'shenzhen'}
bmao = {'first_name':'bmao','last_name':'bmao2','age':'22','city':'guangzhou'}
cmao = {'first_name':'cmao','last_name':'cmao2','age':'23','city':'huizhou'}

people = [mao,bmao,cmao]
#print(people+'\n')的话会报错
for p in people:
    print(p)

#6-8
andy={'type':'cat','host':'zhuzhu'}
lily={'type':'dog','host':'mike'}
qq={'type':'bird','host':'john'}

pets=[andy,lily,qq]
for pet in pets:
    print(pet)


#6-9
favourite_places={
    'mike':['beijing','changsha','nanjing'],
    'lilei':['shenzhen'],
    'wuyifan':['guangzhou','shenzhen']
    }
for name,places in favourite_places.items():
    print('\nThe man is '+name)
    print('His favourite tourist place are:')
    for place in places:
        print(place)
        
#留道思考题，如果要把有相同爱好地点的人找到，要怎么做？
#先简化问题，构建一个纯字典
places_for_test = {
    'a':'shenzhen',
    'b':'beijing',
    'c':'guangzhou',
    'd':'shenzhen'}
for k1,v1 in places_for_test.items():
    for k2,v2 in places_for_test.items():
        if v1 == v2:
            if k1 != k2:
                print(k1+'---'+k2)
#妈的想不出来，先跳过


#6-10略
#6-11
cities = {
    'beijing':{'country':'china','population':'1.4billion','fact':'a geat contry'},
    'tokyo':{'country':'japan','population':'0.1billion','fact':'a big city'},
    'new york':{'country':'america','population':'0.2biliion','fact':'beatiful city'}
    }
#为什么下一行还是要用items啊？那就是基本都要咯，哪怕下面是个字典也要
for city,information in cities.items():
    print('\nThe city is '+city.title())
    #这里一开始犯了个小错误，把for还往后缩进了，所以编译器疯狂报警哈哈哈
    for k,v in information.items():
        print('The '+k+' is '+v)












