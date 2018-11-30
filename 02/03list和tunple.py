#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素。

classmates = ['michael', 'bb', 'ttt']
print(classmates)

print(len(classmates))

print(classmates[0])

#如果要取最后一个元素，除了计算索引位置外，还可以用-1做索引，直接获取最后一个元素：
print(classmates[-1])
print(classmates[-3])

#追加
classmates.append('aaaaaa')
print(classmates)

#插入
classmates.insert(1, 'jack')

#删除  要删除指定位置的元素，用pop(i)方法，其中i是索引位置：

classmates.pop()

#替换

classmates[0] = '好好学习天天向上'

print(classmates)

#list元素也可以是另一个list，比如：
s = ['python', 'java', ['asp', 'php'], 'scheme']
print(len(s))



#另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改，比如同样是列出同学的名字：
classmates = ('aaa', 'bbb', 'cccc')
print(classmates)

#但是，要定义一个只有1个元素的tuple，如果你这么定义：t = (1)会发生错误 这是因为括号()既可以表示tuple，又可以表示数学公式中的小括号，

t = (1,)
print(t)









