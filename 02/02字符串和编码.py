#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('包含该哈哈哈')
#对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符：

print(ord('A'))
print('中')
print(chr(65))
print(chr(25991))
#由于Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节。如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes。

#Python对bytes类型的数据用带b前缀的单引号或双引号表示：
#要注意区分'ABC'和b'ABC'，前者是str，后者虽然内容显示得和前者一样，但bytes的每个字符都只占用一个字节。
#以Unicode表示的str通过encode()方法可以编码为指定的bytes，例如：

print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))

#反过来，如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法：

print(b'ABC'.decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

print(len('ABC'))
print(len('中文'))

#len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数：


print(len(b'ABC'))
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))


# 格式化字符串
print('hellp %s' % 'world');

print('Hi, %s, you have $%d' % ('yanbo', 10000000))

#你可能猜到了，%运算符就是用来格式化字符串的。在字符串内部，%s表示用字符串替换，%d表示用整数替换，有几个%?占位符，后面就跟几个变量或者值，顺序要对应好。如果只有一个%?，括号可以省略

#另一种格式化字符串的方法是使用字符串的format()方法，它会用传入的参数依次替换字符串内的占位符{0}、{1}……，不过这种方式写起来比%要麻烦得多：

print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))

r1 = 72
r2 = 85.0
print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', (r2-r1)/r1*100))
