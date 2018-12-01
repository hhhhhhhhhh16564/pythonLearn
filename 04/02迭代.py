L = list(range(10))
for i in  L:
    print(i)

d = {'a': 1, 'b':2, 'c':3}

#默认情况下，dict迭代的是key。如果要迭代value，可以用for value in d.values()，
for key in d :
    print(key)

for value in d.values():
    print(value)
#如果要同时迭代key和value，可以用for k, v in d.items()。
for key, value in d.items():
    print(key, value)

#由于字符串也是可迭代对象，因此，也可以作用于for循环：
for ch in 'abcd':
    print(ch)


#那么，如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断：

from  collections import Iterable

print(isinstance('abc', Iterable))
print(isinstance([1,2,3], Iterable))

#最后一个小问题，如果要对list实现类似Java那样的下标循环怎么办？Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以

for i, value in enumerate(['a', 'b', 'c', 'd']):
    print(i, value)
#上面的for循环里，同时引用了两个变量，在Python里是很常见的，比如下面的代码：
for x, y in [(1,1), (2,4), [3, 27]]:
    print(x, y)