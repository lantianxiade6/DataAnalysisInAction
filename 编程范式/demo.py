from random import random

'''
函数式编程示例：
有3辆车，一共5次机会，每次它们都有70%的概率向前走一步，打出每一次这3辆车的前行状态
'''

# #【1】简单函数封装版
# def move_cars():
#     for i,_ in enumerate(car_positions):#会默认以car_positions为参数
#         if random()>0.3:#调用random函数生成一共0-1的随机数，若大于0.3则相应加1
#             car_positions[i] += 1

# def draw_car(car_position):
#     print ('-'*car_position)

# def run_step_of_race():
#     global time#使用全局变量里面的time
#     time -= 1#time每次调用都减1
#     move_cars()#调用move_cars函数

# def draw():
#     print('')
#     print('第',5-time,'次：')
#     for car_position in car_positions:
#         draw_car(car_position)#调用draw_car函数

# time=5#初始值，这个就有问题了，因为这个初始值会被修改，所以这些函数是有状态的。
# car_positions=[1,1,1]

# while time:
#     run_step_of_race()
#     draw()


#【2】函数式编程版:
# def move_cars(car_positions):
#     return list(map(lambda x:x+1 if random()>0.3 else x, car_positions))#对car_positions的每一个元素调用匿名函数

# def output_car(car_position):
#     return '-'*car_position

# def run_step_of_race(state):
#     return {'time':state['time']-1,
#             'car_positions':move_cars(state['car_positions'])}

# def draw(state):
#     print('第',5-state['time'],'次：')
#     print('\n'.join(map(output_car,state['car_positions'])))

# def race(state):
#     draw(state)
#     if state['time']:
#         race(run_step_of_race(state))#递归

# race({'time':5,'car_positions':[1,1,1]})#共用变量全程都通过参数传递

# #【3】map
# def toUpper(item):
#     return item.upper()

# output=list(map(toUpper,['hao','chen','yue']))#批量转小写
# print(output)

# #【4】filter/reduce
# from functools import reduce
# num=[2,-5,9,7,-2,5,3,1,0,-3,8]
# positive_num=list(filter(lambda x:x>0,num))#过滤出正数
# total=reduce(lambda x,y:x+y,positive_num)#算总和
# average=total/len(positive_num)#算均值
# print(average)

#【5】函数式pipeline
def even_filter(nums):#取出偶数，结果是一个生成器
    for num in nums:
        if num %2 ==0:
            yield num

def multiply_by_three(nums):#乘3，结果是一个生成器
    for num in nums:
        yield num*3

def covert_to_string(nums):#转字符串，结果是一个生成器
    for num in nums:
        yield 'The number : %s' % num

nums=[1,2,3,4,5,6,7,8,9,10]
#旧方法
# pipeline=covert_to_string(multiply_by_three(even_filter(nums)))#结果也是一个生成器
# for num in pipeline:#被迭代的时候才会正在运算
#     print(num)

#真正的pipeline
from functools import reduce
def pipeline_func(data,fns):
    return reduce(lambda a,x: x(a), fns,data)#对一堆函数即fns做一个reduce
print(list(pipeline_func(nums,[even_filter,multiply_by_three,covert_to_string])))