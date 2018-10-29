import os
import sys

from django.conf import settings
# from user.models import *

MOD = 0xffffffff


def foo(a, b=123):
    c = {'x': 111, 'y': 222}  # 定义一个字典
    d = [1, 3, 5]
    return a, b, c


def bar(x):
    if x % 2 == 0:
        return True




def test(a, b, c, d=1):
    print(a+b+c+d)

test(1,2,4,5)
# 偏函数 为简化步骤，给某个参数赋值，所造的函数叫偏函数
import functools
newtest=functools.partial(test,c=5)
newtest(1,2)
num='100101'
result=int(num,base=2)
print(result)
int2=functools.partial(int,base=2)
result=int2(num)
print(result)

# 高阶函数
def calculate(num1,num2,cal):
    print(cal(num1,num2))
def sum(a,b):
    return a+b
def jianfa(a,b):
    return a-b
calculate(2,5,sum)
calculate(2,5,jianfa)
print('123')