# -*- coding: utf-8 -*-
"""
Created on Sat May 15 15:03:07 2021

@author: zhang
"""
favourite_cities={
    'mao':['shenzhen','guangzhou','beijing'],
    'li':['shenzhen','nanjing'],
    'zhang':['tianjing','guangzhou'],
    'huang':['dunhuang','xizang']}
new_cities =[]

for cities in favourite_cities.values():
    for city in cities:
        new_cities.append(city)
new_cities = list(set(new_cities))
#new_cities是去重后的城市名单
print(new_cities)

new_dict = {}
new_list = []
want_to_check = 'shenzhen'
k=0


for n in range(0,len(new_cities)):
    want_to_check = new_cities[n]
    #这个w的位置很重要，之前就是在这里错了，一直卡住了
    for w in (0,1):
        if w == 0:
            for mans,cities in favourite_cities.items():
                for city in cities:
                        if w == 0:
                            if want_to_check == city:
                                new_list.append(mans)
                                new_dict[city] = new_list
        else:
            #一定要加个条件，让new_list没得加的时候才清空
            new_list =[]

print(new_list)
print(new_dict)
print('--'*20)

#九哥的代码，被完爆了2333
result = {}
for p, citys in favourite_cities.items():
    for city in citys:
        #这个get函数之前不知道，知道了这个函数之后后面就会顺很多--还是要看其他的基础书
        if result.get(city) is None:
            #的确这样子建一个空集就好了嘛，上面的代码其实陷入了一个误区，就是我的键值对
            #一定要准备好了才能一一配对。但是实际上哪怕一开始不对，后面对了就可以了
            result[city] = []
            #甚至不用新建一个list
        result[city].append(p)
print(result)
