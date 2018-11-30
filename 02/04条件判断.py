#!/usr/bin/env python3
# -*- coding: utf-8 -*-

age = 20
if age >= 18:
    print('your age is', age)
    print('adult')

age = 3
if age >= 18:
    print('your age is', age)
else:
    print("小屁孩")

age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

#elif是else if的缩写，完全可以有多个elif，所以if语句的完整形式就是：
x = 0.01
if x:
    print('True')

#只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False。

birth = input('birth')
print(birth)
#input()返回的数据类型是str

height = 1.75
weight = 80.5
bim = weight/(height*height)
if bim < 18.5:
    print('体重过轻')
elif bim < 25:
    print("normal")
elif bim < 28:
    print('体重过重')
elif bim < 32:
    print('fat')
else:
    print('you are so fat')













