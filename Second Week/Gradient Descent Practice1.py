from __future__ import division
from sympy import symbols, diff, expand
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D



#初始化数据集
x = [1,2,3,4,5,6,7,8,9,10]
y = 10

#y=ax^2 + bx + 1,定义参数
a, b = symbols('a b', real=True)

# 初始化代价函数
costfuc = 0 * 1

for i in range(len(x)):
    costfuc += (a * (x[i] ** 2) + b * x[i] + 1 - y) ** 2

costfuc /= 2*len(x)

#求偏导
da = diff(costfuc, a)
db = diff(costfuc, b)

#参数初始值赋值
ra = 1
rb = 1

costvalue = costfuc.subs({a:ra,b:rb})
endcostvalue = 0#用cost的值的变化程度来判断是否已经达到最小值了
count = 0
alpha = 0.0001#学习率（步子大小）

while(costvalue - endcostvalue > 0.00001 or endcostvalue - costvalue > 0.00001) and count < 1000:
    count += 1
    costvalue = endcostvalue
    ra = ra - alpha * da.subs({a:ra, b:rb})
    rb = rb - alpha * db.subs({a:ra, b:rb})
    endcostvalue = costfuc.subs({a:ra, b:rb})

ra = round(ra, 4)
rb = round(rb, 4)
print(ra, rb)


