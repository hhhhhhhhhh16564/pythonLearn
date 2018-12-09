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
























