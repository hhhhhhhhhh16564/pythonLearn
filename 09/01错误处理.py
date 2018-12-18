try:
    print('try....')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally....')
print('END')
# 当我
# 们认为某些代码可能会出错时，就可以用try来运行这段代码，如果执行出错，则后续代码不会继续执行，
# 而是直接跳转至错误处理代码，即except语句块，执行完except后，如果有finally语句块，则执行finally语句块，至此，执行完毕。
# int()函数可能会抛出ValueError，所以我们用一个except捕获ValueError，用另一个except捕获ZeroDivisionError。
# 此外，如果没有错误发生，可以在except语句块后面加一个else，当没有错误发生时，会自动执行else语句：
try:
    print('try...')
    r = 10/ int('2')
    print('result:', r)
except ValueError as e:
    print('valueError', e)
except ZeroDivisionError as e:
    print('ZerodivisionError', e)
else:
    print('no error!')
finally:
    print('finally....')
print('END')

# Python的错误其实也是class，所有的错误类型都继承自BaseException，
# 所以在使用except时需要注意的是，它不但捕获该类型的错误，还把其子类也“一网打尽”。比如：
try:
    abs(8)
except ValueError as e:
    print('ValueError')
except UnicodeError as e:
    print('UnicodeError')
# Python所有的错误都是从BaseException类派生的，常见的错误类型和继承关系看这里：

# https://docs.python.org/3/library/exceptions.html#exception-hierarchy

# 使用try...except捕获错误还有一个巨大的好处，就是可以跨越多层调用

# 如果错误没有被捕获，它就会一直往上抛，最后被Python解释器捕获，打印一个错误信息，然后程序退出

# Python内置的logging模块可以非常容易地记录错误信息：
import logging
def foo(s):
    return 10 / int(s)
def bar(s):
    return foo(s) * 2
def main():
    try:
        bar(0)
    except Exception as e:
        logging.exception(e)
# main()
print('END')
# 同样是出错，但程序打印完错误信息后会继续执行，并正常退出：
# 通过配置，logging还可以把错误记录到日志文件里，方便事后排查。

# 抛出错误
class FooError(ValueError):
    pass
def foo(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value: %s' %s)
    return 10 / n
# foo('0')


def foo(s):
    n = int(s)
    if n==0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise

# bar()
# 在bar()函数中，我们明明已经捕获了错误，但是，打印一个ValueError!后，又把错误通过raise语句抛出去了，这不有病么？
# 由于当前函数不知道应该怎么处理该错误，所以，最恰当的方式是继续往上抛，让顶层调用者去处理

# raise语句如果不带参数，就会把当前错误原样抛出。此外，在except中raise一个Error，还可以把一种类型的错误转化成另一种类型

from functools import reduce

def str2num(s):
    return float(s)

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

main()

#字符串转化为数组

s = '1 + 2 + 3 + 4'
print(s.split('+'))

#数组转换为字符串
L = ['1 ', ' 2 ', ' 3 ', ' 4']
s = ','.join(L)
print(s)
