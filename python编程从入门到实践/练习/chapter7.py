# -*- coding: utf-8 -*-
"""
Created on Sun May 16 10:45:32 2021

@author: zhang
"""
# #7-1
# car_message = input('What car do you want ? ')
# print('Let me see if I can find you a '+car_message)

# #7-2
# person_message=input('how many people do you have ? ')
# if int(person_message) >= 8:
#     print('There is no table for you!')
# else:
#     print('Please come in!')

# #7-3
# number_message = input('Please give me a number :')
# if int(number_message)%10 == 0:
#     print('This number can be eliminated by 10.')
# else:
#     print('A bad number!')

# 7-4 while循环
# food_list=[]
# while True:
#     food_message = input('Please give me your favorite food adding in pizza:')
#     if food_message != 'q':
#         print('We will add '+food_message+ 'in your pizza.')
#         #一开始这里写成 food_list +=food_message就错了
#         food_list.append(food_message)
#         continue
#     else:
#         break
# print(food_list)

#7-4 for循环
#这里都没有次数，何必要强行用for循环呢？

# #7-5
# #这里为什么要用到while？
# #这里还是要注意一下，这里出现了负数肯定可以运行的，其实不太好
# age_message = input('Please give me your age:')
# real_age = int(age_message)
# if real_age <= 3:
#     price = 0
# elif real_age <= 12:
#     price = 10
# else:
#     price = 15
# print('Your price is '+str(price))

# #7-7
# while True:
#     print('nice!!')

#7-8
#这里其实用pop（）函数最好
# sandwich_orders = ['normal','pastrami','added bacon','pastrami','added egg']
# finished_sandwiches = []
# while len(sandwich_orders)>0:
#     print('I made your '+sandwich_orders[0]+' sandwich.')
#     finished_sandwiches.append(sandwich_orders[0])
#     del sandwich_orders[0]

# print(sandwich_orders)
# #为什么这里不能用 is None，因为它只能用来指代什么都没有的情况
# if len(sandwich_orders) == 0:
#     print('Your order is finished.'+'\nThe sandwichs you have ordered:')
#     for a in range(len(finished_sandwiches)):
#         print(finished_sandwiches[a])

#7-9
#妙啊
# print('The pastrami cannot be sold now.')
# while 'pastrami' in sandwich_orders:
#     sandwich_orders.remove('pastrami')
# print(sandwich_orders)

#7-10
# responses = {}
# active = True
# while active:
#     name = input('What is your name?')
#     place=input('If you could visit one place in the world,where would you go ? ')
    
#     responses[name]=place
    
#     repeat = input('would you like to let another person respond?(yes/no)')
#     if repeat == 'no':
#         active = False
#     else:
#         continue
# print('-'*10+'RESULT'+'-'*10)
# for name,place in responses.items():
#     print(name.title()+' want to go '+place.title())
        
    
    











