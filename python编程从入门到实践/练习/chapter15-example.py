# -*- coding: utf-8 -*-
"""
Created on Fri May 28 16:03:02 2021

@author: zhang
"""
import matplotlib.pyplot as plt

# input_values = [1,2,3,4,5]
# squares =[1,4,9,16,25]
# plt.plot(input_values,squares,linewidth = 5 )

# plt.title('Square Numbers', fontsize = 24)
# plt.xlabel('Value', fontsize = 14)
# plt.ylabel('Square of Value', fontsize = 14)

# plt.tick_params(axis ='both',labelsize = 14)
# #plt.plot(squares)
# plt.show()

# x_values = list(range(1,1001))
# y_values = [x**2 for x in x_values]
# plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,edgecolors='none',s=40)

# plt.title('Square Numbers', fontsize = 24)
# plt.xlabel('Value', fontsize = 14)
# plt.ylabel('Square of Value', fontsize = 14)

# plt.tick_params(axis ='both',which = 'major',labelsize = 14)

# plt.savefig('squares_plot.png', bbox_inches='tight')

#开始随机漫步吧
from random import choice

class RandomWalk():
    '''一个生成随机漫步数据的类'''
    
    def __init__(self,num_points=5000):
        '''初始化随机漫步的属性'''
        self.num_points=num_points
        
        #所有随机漫步都始于（0,0）
        self.x_values = [0]
        self.y_values = [0]
        
    def fill_walk(self):
        '''计算包含随机漫步的所有点'''
        
        #不断漫步，直到列表达到指定的长度
        for _ in range(self.num_points-1):
        # 等价于while len(self.y_values) < self.num_points:
            
            #决定前进方向以及沿这个方向前进的距离
            x_direction = choice([1,-1])
            y_direction = choice([1,-1])
            x_distance = choice([1,2,3,4])
            y_distance = choice([1,2,3,4])
            x_step = x_direction*x_distance
            y_step = y_direction*y_distance
            
            # #拒绝原地踏步
            # if x_step == 0 and y_step == 0:
            #     continue
            
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step
            
            self.x_values.append(next_x)
            self.y_values.append(next_y)

import matplotlib.pyplot as plt

rw = RandomWalk()
rw.fill_walk()

point_numbers = list(range(rw.num_points))
plt.scatter(rw.x_values, rw.y_values, s=15, c=point_numbers,cmap=plt.cm.Blues,
            edgecolors='none')

#突出起点和终点
plt.scatter(0, 0, edgecolors='none',s=100)
plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red',edgecolors='none',
            s=100)

plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)
plt.show()
print(len(rw.x_values)) 
            
            








