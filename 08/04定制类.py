# __len__()方法我们也知道是为了能让class作用于len()函数。
# __str__

class Student(object):
    def __init__(self, name):
        self.name = name
print(Student('xiaoming'))     #<__main__.Student object at 0x104bdb2e8>
class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Studetn object (name: %s)' % self.name
print(Student('xiaoming'))   #Studetn object (name: xiaoming)
# 但是细心的朋友会发现直接敲变量不用print，打印出来的实例还是不好看：
# 这是因为直接显示变量调用的不是__str__()，而是__repr__()，两者的区别是__str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的。
#解决办法是再定义一个__repr__()。但是通常__str__()和__repr__()代码都是一样的，所以，有个偷懒的写法：

class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name=%s)' % self.name
    __repr__ = __str__

# __iter__

# 如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。

# 我们以斐波那契数列为例，写一个Fib类，可以作用于for循环：

class Fib():
    def __init__(self):
        self.a, self.b = 0, 1
    def __iter__(self):
        return self
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b

        if self.a > 10000:
            raise  StopIteration()
        return self.a
for n in Fib():
    print(n)

# Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是不行，比如，取第5个元素：
#要表现得像list那样按照下标取出元素，需要实现__getitem__()方法：

class Fib(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in  range(n):
            a, b = b, a+b
        return a

f = Fib()
print(f[0], f[1], f[2], f[3], f[100])


#但是list有个神奇的切片方法
print(list(range(100))[5:10])
#但是f报错是__getiteM
class Fib(object):
    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        #n是切片
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
        return L


f = Fib()
print(f[5:10])

print(f[100:110])
#_实现_getitem__方法可以直接for循环

for n in f:
    if n > 1000:
        break;
    print(n)

print(f[:10:2])   #[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

#但是没有对step参数作处理 也没有对负数作处理，


# 此外，如果把对象看成dict，__getitem__()的参数也可能是一个可以作key的object，例如str。
#
# 与之对应的是__setitem__()方法，把对象视作list或dict来对集合赋值。最后，还有一个__delitem__()方法，用于删除某个元素。

# __getattr__
#正常情况下，当我们调用类的方法或属性时，如果不存在，就会报错。比如定义Student类：
class Student(object):

    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, attr):
        if attr=='score':
            return 99


# 当调用不存在的属性时，比如score，Python解释器会试图调用__getattr__(self, 'score')来尝试获得属性，这样，我们就有机会返回score的值：

s = Student()
s.name = 'miixao'
print(s.score)

# 返回函数也是完全可以的：

class Student(object):
    def __getattr__(self, attr):
        if attr == 'age':
            return lambda : 25

s = Student()
print(s.age())

# 注意，只有在没有找到属性的情况下，才调用__getattr__，已有的属性，比如name，不会在__getattr__中查找。

# 此外，注意到任意调用如s.abc都会返回None，这是因为我们定义的__getattr__默认返回就是None。要让class只响应特定的几个属性，我们就要按照约定，抛出AttributeError的错误：

class Student(object):
    def __getattr__(self, attr):
        if attr == 'age':
            return lambda : 25
        raise AttributeError('no found')
s = Student()
# print(s.age1())



#这实际上可以把一个类的所有属性和方法调用全部动态化处理了，不需要任何特殊手段。

# 这种完全动态调用的特性有什么实际作用呢？作用就是，可以针对完全动态的情况作调用。
#
# 举个例子：
#
# 现在很多网站都搞REST API，比如新浪微博、豆瓣啥的，调用API的URL类似：
#
# http://api.server/user/friends
# http://api.server/user/timeline/list

class Chain(object):
    def __init__(self, path= ''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))
    def __str__(self):
        return self._path
    __repr__ = __str__

print(Chain('http://api.server/user').usr.timeline)

# __call__

# 一个对象实例可以有自己的属性和方法，当我们调用实例方法时，我们用instance.method()来调用。能不能直接在实例本身上调用呢？在Python中，答案是肯定的。
#
# 任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用。请看示例：

class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s' % self.name)
s = Student('Michael')
s()



# __call__()还可以定义参数。对实例进行直接调用就好比对一个函数进行调用一样，所以你完全可以把对象看成函数，把函数看成对象，因为这两者之间本来就没啥根本的区别

# 如果你把对象看成函数，那么函数本身其实也可以在运行期动态创建出来，因为类的实例都是运行期创建出来的，这么一来，我们就模糊了对象和函数的界限。
# 那么，怎么判断一个变量是对象还是函数呢？其实，更多的时候，我们需要判断一个对象是否能被调用，能被调用的对象就是一个Callable对象，比如函数和我们上面定义的带有__call__()的类实例

print(callable(Student('')))  #True

print(callable(max))          #True

print(callable([1,2]))        #False

# 通过callable()函数，我们就可以判断一个对象是否是“可调用”对象。

















