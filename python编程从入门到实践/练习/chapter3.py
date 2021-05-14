# -*- coding: utf-8 -*-
"""
Created on Thu May 13 20:16:28 2021

@author: zhang
"""

#3-1&3-2
names =['maoqiaozhang','lilei','hanmeimei']
#注意range后面那个数要加一的
for n in range(0,len(names)):
    print(names[n].title()+' , hello!')

#3-3
ways = ['car','bike','ship']
for n in range(0,len(ways)):
    print('I would like to own a '+ways[n])


#3-4--3-7
invited_person = ['jobs','chairmanmao','grandfather']
for n in range(0,len(invited_person)):
    print(invited_person[n].title()+' , can you have a dinner with me ?')
    
#3-5
can_not_come = invited_person.pop()
print('\n'+can_not_come + ' , this is a pity that you cannot come!')
invited_person.append('kiki')
for n in range(0,len(invited_person)):
    print(invited_person[n].title()+' , can you have a dinner with me ?')

#3-6
print('\nI am so glad to tell you we find a big table.')
invited_person.insert(0,'gates')
invited_person.insert(2, 'bill')
invited_person.append('lady gaga')
for n in range(0,len(invited_person)):
    print(invited_person[n].title()+' , can you have a dinner with me ?')

#3-7
print('\nI am so sad to tell you our table can not be sent in time.')
for i in range(0,4):
    sorry_person=invited_person.pop()
    print(sorry_person+' , I am so sad that I cannot invite you')
for n in range(0,len(invited_person)):
    print(invited_person[n].title()+' , we also hope that you can arrive.')
del invited_person[0]
del invited_person[0]
#这个错误很有价值
#for n in range(0,len(invited_person)):
#    del invited_person[n]
print(invited_person)


#3-8
#print里面不能同时有列表和'\n'
cities = ['changsha','beijing','chengdu','xizang','xian']
print(cities)

#临时排序
print('\n')
print(sorted(cities))
print(cities)

#临时反向排序
print('\n')
print(sorted(cities,reverse=True))
print(cities)

#永久两次反向
print('\n')
#真是奇了怪了，reverse这个函数一定得这么调用，然后下面这两行代码还不能合并到一行
#reverse(cities)不行，print(cities.reverse())不行
cities.reverse()
print(cities)
cities.reverse()
print(cities)

#永久字母排序
print('\n')
cities.sort()
print(cities)
cities.sort(reverse=True)
print(cities)

#3-9
#注意要在int和str之间转化
l = len(cities)
print('I want to go to '+str(l)+' cities.')
    
#3-10、3-11略








