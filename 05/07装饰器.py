#由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数
#函数对象有一个__name__属性，可以拿到函数的名字：
def now():
    print('2015-8-8')
f = now;
f()
print(now.__name__)
print(f.__name__)

#假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。

def log(func):
    def wrapper(*args, **kw):
        print('call %s ():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print('2015-3-35')
now()

def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s call %s ()' % (text, func.__name__))
            return func(*args, **kw)
        return  wrapper
    return decorator

@log('execute')
def now():
    print('2015-3-35')
now()

# 和两层嵌套的decorator相比，3层嵌套的效果是这样的：
# now = log('execute')(now)

# 以上两种decorator的定义都没有问题，但还差最后一步。因为我们讲了函数也是对象，它有__name__等属性，但你去看经过decorator装饰之后的函数，它们的__name__已经从原来的'now'变成了'wrapper'：
#因为返回的那个wrapper()函数名字就是'wrapper'，所以，需要把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错。

#需要编写wrapper.__name__ = func.__name__这样的代码，Python内置的functools.wraps就是干这个事的，所以，一个完整的decorator的写法如下：


import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

#或者针对带参数的decorator：

import functools

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
# import functools是导入functools模块。模块的概念稍候讲解。现在，只需记住在定义wrapper()的前面加上@functools.wraps(func)即可。


#练习 函数执行的时间
import  time, functools
def calculateTime(text):
    def decorator(func):
        @functools.wraps(func)
        def wraaper(*args, **kw):
            print(text, func.__name__)
            start = time.time()
            r = func(*args, **kw)
            end = time.time()
            print('函数执行时间是 %f' % (end-start))
            return r
        return wraaper
    return  decorator

@calculateTime('hhh')
def ongrunning():
    for i in  range(1, 1000):
        t = i * i

    print('-end--')


ongrunning()


