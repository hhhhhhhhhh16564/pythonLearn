#Python的functools模块提供了很多有用的功能，其中一个就是偏函数（Partial function）。要注意，这里的偏函数和数学意义上的偏函数不一样。
# int()函数可以把字符串转换为整数，当仅传入字符串时，int()函数默认按十进制转换：
# 但int()函数还提供额外的base参数，默认值为10。如果传入base参数，就可以做N进制的转换：
print(int('123456', base=8))

# 假设要转换大量的二进制字符串，每次都传入int(x, base=2)非常麻烦，于是，我们想到，可以定义一个int2()的函数，默认把base=2传进去：
def int2(x, base=2):
    return int(x, base)

print(int2('111111'))

# functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2()，可以直接使用下面的代码创建一个新的函数
import functools
int3 = functools.partial(int, base=3)

print(int3('12'))

# 注意到上面的新的int3函数，仅仅是把base参数重新设定默认值为3，但也可以在函数调用时传入其他值：
print(int3('122', base=10))

# 最后，创建偏函数时，实际上可以接收函数对象、*args和**kw这3个参数，当传入：
# int2 = functools.partial(int, base=2)
# 实际上固定了int()函数的关键字参数base，也就是：
# 相当于：
#
# kw = { 'base': 2 }
# int('10010', **kw)


# 当传入：
#
# max2 = functools.partial(max, 10)
# 实际上会把10作为*args的一部分自动加到左边，也就是：
#
# max2(5, 6, 7)

# 相当于：
#
# args = (10, 5, 6, 7)
# max(*args)
# 当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，这个新函数可以固定住原函数的部分参数，从而在调用时更简单。