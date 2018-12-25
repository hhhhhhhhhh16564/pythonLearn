# 我们知道tuple可以表示不变集合，例如，一个点的二维坐标就可以表示成：

p = (1, 2)

from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x, p.y)

#namedtuple是一个函数 它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。

print(isinstance(p, Point)) #True
print(isinstance(p, tuple)) #True

#定义一个圆
Circle = namedtuple('Circle', ['x', 'y', 'r'])

# 使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，
# 因为list是线性存储，数据量大的时候，插入和删除效率很低。

# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：

from  collections import  deque

q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
q.pop()
q.popleft()
print(q)
# deque除了实现list的append()和pop()外，还支持appendleft()和popleft()，
# 这样就可以非常高效地往头部添加或删除元素。

# 使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，
# 返回一个默认值，就可以用defaultdict：
from  collections import  defaultdict
dd = defaultdict(lambda : 'N/A')
dd['key1'] = 'abc'
print(dd['key1'], dd['key2'])  #abc N/A

# 注意默认值是调用函数返回的，而函数在创建defaultdict对象时传入。
# 除了在Key不存在时返回默认值，defaultdict的其他行为跟dict是完全一样的。



# OrderedDict
# 使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。
from  collections import  OrderedDict

d1 = dict(a=1, b='test', c='3')
d2 = dict([('a', 1), ('b', 2), ('c', 3)])
d3 = {'a':1, 'b':2, 'c':3}
print(isinstance(d1, dict),  isinstance(d2, dict), isinstance(d3, dict))
print(d1, d2, d3)

od = OrderedDict([('a', 1), ('b',2), ('c',3)])

print(od)

# 注意，OrderedDict的Key会按照插入的顺序排列，不是Key本身排序：

od = OrderedDict()
od['z'] = 1
od['y'] = 2
od['x'] = 3
print(list(od.keys()))

# OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key：
# __xxxitem__:使用 [''] 的方式操作属性时被调用
#
# __setitem__:每当属性被赋值的时候都会调用该方法，因此不能再该方法内赋值 self.name = value 会死循环
#
# __getitem__:当访问不存在的属性时会调用该方法
#
# __delitem__:当删除属性时调用该方法
print('-----------------\n')
a = -1
#当a > 0时，b的值为3， 否则为-5
b = 3 if a > 0 else -5
print('b:',b)


from collections import OrderedDict
class LastUpdateOrderedDict(OrderedDict):
    def __init__(self, capacity):
        super(LastUpdateOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in  self else 0
        if len(self) - containsKey >= self._capacity:
            #删除第一个
            last = self.popitem(last = False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)



# ChainMap
# ChainMap可以把一组dict串起来并组成一个逻辑上的dict。ChainMap本身也是一个dict，但是查找的时候，会按照顺序在内部的dict依次查找。
#
# 什么时候使用ChainMap最合适？举个例子：应用程序往往都需要传入参数，参数可以通过命令行传入，可以通过环境变量传入，还可以有默认参数
# 。我们可以用ChainMap实现参数的优先级查找，即先查命令行参数，如果没有传入，再查环境变量，如果没有，就使用默认参数。

from collections import ChainMap
import os, argparse

#构建缺醒参数
defaults = {
    'color': 'red',
     'user': 'guest'
}

#构建命令行参数
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args()

command_line_args = {k:v for k, v in vars(namespace).items() if v}

#组合成chainMap:
combined = ChainMap(command_line_args, os.environ, defaults)

print('color = %s' % combined['color'])
print('user = %s' % combined['user'])

#字典也可以切片
d = {'a': 3, 'b': 4, 'c': 5, 'd': 6, 'e': 7, 'f': 8, 'g': 9}
f = {k:v for  k,v in d.items() if v > 5}
print('f', f)
# 没有任何参数时，打印出默认参数：
#
# $ python3 use_chainmap.py
# color=red
# user=guest
# 当传入命令行参数时，优先使用命令行参数：
#
# $ python3 use_chainmap.py -u bob
# color=red
# user=bob
# 同时传入命令行参数和环境变量，命令行参数的优先级较高：
#
# $ user=admin color=green python3 use_chainmap.py -u bob
# color=green
# user=bob


# Counter
# Counter是一个简单的计数器，例如，统计字符出现的个数：
from collections import Counter
c = Counter()

for ch in 'programming':
    c[ch] = c[ch] + 1

print(c)

# Counter实际上也是dict的一个子类，上面的结果可以看出，字符'g'、'm'、'r'各出现了两次，其他字符各出现了一次。


























