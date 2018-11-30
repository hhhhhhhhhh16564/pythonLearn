
d = {'michael': 95, 'bob': 75, 'tracy': 85}
d['adam'] = 67
d['hhhh'] = 99
print(d)
print(d['bob'])

#如果key不存在，dict就会报错：
#dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value：

print(d.get('bbb', -1))
#要删除一个key，用pop(key)方法，对应的value也会从dict中删除：

d.pop('bob')

#dict可以用在需要高速查找的很多地方，在Python代码中几乎无处不在，正确使用dict非常重要，需要牢记的第一条就是dict的key必须是不可变对象。
#这是因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了。这个通过key计算位置的算法称为哈希算法（Hash）

s = set([1, 2, 3])
print(s)

ss = set([1, 2, 3, 4, 5, 6, 4, 5, 3, 2, 1])
print(ss)

#添加
ss.add(555)
print(ss)

#删除
ss.remove(1)
print(ss)

#set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作：
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2)
print(s1 | s2)

a = 'abcd'
print(a.replace('a', 'hhhhhh'))

aa = ['a', 'c', 'd', 'n', 'm']
aa.sort()
print(aa)





































