#和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
# true保留， false丢弃

#在一个list中，删掉偶数，只保留奇数，可以这么写：
def is_odd(n):
    return n % 2 == 0

print(list(filter(is_odd,[1,2,3,4,5,6])))

#去掉字符串首尾的空格 strip(）

#注意到filter()函数返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list。

#计算素数的一个方法是埃氏筛法，它的算法理解起来非常简单：

def odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

#定义一个筛选函数
def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)

for n in primes():
    if n < 1000:
        print(n)
    else:
        break


#第三十二行有点不太明白， 不是传一个函数名字吗，怎么还带参数