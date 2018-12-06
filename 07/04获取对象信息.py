# 当我们拿到一个对象的引用时，如何知道这个对象是什么类型、有哪些方法呢？
# 基本类型都可以用type()判断：
print(type(123))   #<class 'int'>
print(type('hhh')) #<class 'str'>
print(type(None))  #<class 'NoneType'>

# 如果一个变量指向函数或者类，也可以用type()判断：
print(type(abs)) #<class 'builtin_function_or_method'>
# 但是type()函数返回的是什么类型呢？它返回对应的Class类型。如果我们要在if语句中判断，就需要比较两个变量的type类型是否相同：
print(type(123) == type(456))  #True
print(type(123) == int)        #True
print(type('123') == str)      #True
print(type('abc') == type(123)) #

# 使用isinstance()
# 对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数。

# 能用type()判断的基本类型也可以用isinstance()判断：
# >>> isinstance('a', str)
# True
# >>> isinstance(123, int)
# True
# >>> isinstance(b'a', bytes)
# True

# 并且还可以判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是list或者tuple：
# >>> isinstance([1, 2, 3], (list, tuple))
# True
# >>> isinstance((1, 2, 3), (list, tuple))
# True

# 使用dir()
#它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：
print(dir('abc'))
# ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
# 类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。在Python中，如果你调用len()函数试图获取一个对象的长度，实际上，在len()函数内部，它自动去调用该对象的__len__()方法，所以，下面的代码是等价的

print(len('abc'))
print('abc'.__len__())

# 我们自己写的类，如果也想用len(myObj)的话，就自己写一个__len__()方法：

class MyDog(object):
    def __len__(self):
        return 100
print(len(MyDog()))  #100

# 仅仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态：

class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x

obj = MyObject()
# >>> hasattr(obj, 'x') # 有属性'x'吗？
# True
# >>> obj.x
# 9
# >>> hasattr(obj, 'y') # 有属性'y'吗？
# False
# >>> setattr(obj, 'y', 19) # 设置一个属性'y'
# >>> hasattr(obj, 'y') # 有属性'y'吗？
# True
# >>> getattr(obj, 'y') # 获取属性'y'
# 19
# >>> obj.y # 获取属性'y'
# 19
print(hasattr(obj, 'x'))
setattr(obj, 'y', 19)
print(hasattr(obj, 'y'))
#没有这个属性的话，返回默认值
print(getattr(obj, 'yz', 1000))

# 也可以获得对象的方法
print(hasattr(obj, 'power'))
#将获得的方法赋值
fn = getattr(obj, 'power')
print(fn())

# 小结
# 通过内置的一系列函数，我们可以对任意一个Python对象进行剖析，拿到其内部的数据。要注意的是，只有在不知道对象信息的时候，我们才会去获取对象信息。如果可以直接写：
# sum = obj.x + obj.y
# 就不要写：
#
# sum = getattr(obj, 'x') + getattr(obj, 'y')

# def readImage(fp):
#     if hasattr(fp, 'read'):
#         return readData(fp)
#     return None



