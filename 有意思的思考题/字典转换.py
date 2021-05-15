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