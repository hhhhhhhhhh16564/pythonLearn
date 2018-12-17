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

print('------------------------------------------------------------------------------------------------------------------------------------')
# __getattr__方法
# 拦截点号运算。当对未定义的属性名称和实例进行点号运算时，就会用属性名作为字符串调用这个方法。如果继承树可以找到该属性，则不调用此方法
# 实例instance通过instance.name访问属性name，只有当属性name没有在实例的__dict__或它构造类的__dict__或基类的__dict__中没有找到，
# 才会调用__getattr__。当属性name可以通过正常机制追溯到时，
# __getattr__是不会被调用的。如果在__getattr__(self, attr)存在通过self.attr访问属性，会出现无限递归错误。

class ClassA(object):

    def __init__(self, classname):
        self.classname = classname

    def __getattr__(self, attr):
        return('invoke __getattr__', attr)

insA = ClassA('ClassA')
print(insA.__dict__) # 实例insA已经有classname属性了
# {'classname': 'ClassA'}

print(insA.classname) # 不会调用__getattr__
# ClassA

print(insA.grade) # grade属性没有找到，调用__getattr__
# ('invoke __getattr__', 'grade')





print('*************************')


# __getattribute__(self, name)
# 实例instance通过instance.name访问属性name，__getattribute__方法一直会被调用，
# 无论属性name是否追溯到。如果类还定义了__getattr__方法，除非通过__getattribute__显式的调用它，或者__getattribute__方法出现AttributeError错误，否则__getattr__方法不会被调用了。
# 如果在__getattribute__(self, attr)方法下存在通过self.attr访问属性，会出现无限递归错误。
class ClassA(object):

    def __init__(self, classname):
        self.classname = classname

    def __getattr__(self, attr):
        return('invoke __getattr__', attr)

    def __getattribute__(self, attr):
        return('invoke __getattribute__', attr)


insA = ClassA('ClassA')
print(insA.__dict__)
# ('invoke __getattribute__', '__dict__')

print(insA.classname)
# ('invoke __getattribute__', 'classname')

print(insA.grade)
# ('invoke __getattribute__', 'grade')

# __setattr__方法
# 会拦截所有属性的的赋值语句。如果定义了这个方法，self.arrt = value 就会变成self,__setattr__("attr", value).这个需要注意。当在__setattr__方法内对属性进行赋值是，不可使用self.attr = value,因为他会再次调用self,__setattr__("attr", value),则会形成无穷递归循环，最后导致堆栈溢出异常。应该通过对属性字典做索引运算来赋值任何实例属性，也就是使用self.__dict__['name'] = value.
# 如果类自定义了__setattr__方法，当通过实例获取属性尝试赋值时，就会调用__setattr__。
# 常规的对实例属性赋值，被赋值的属性和值会存入实例属性字典__dict__中。
# 如下类自定义了__setattr__,对实例属性的赋值就会调用它。类定义中的self.attr也同样，所以在__setattr__下还有self.attr的赋值操作就会出现无线递归的调用__setattr__的情况。自己实现__setattr__有很大风险，一般情况都还是继承object类的__setattr__方法。

class ClassA(object):
    def __init__(self, classname):
        self.classname = classname

    def __setattr__(self, name, value):
        # self.name = value  # 如果还这样调用会出现无限递归的情况
        print('invoke __setattr__')

insA = ClassA('ClassA') # __init__中的self.classname调用__setattr__。
# invoke __setattr__

print(insA.__dict__)
# {}

insA.tag = 'insA'
# invoke __setattr__

print(insA.__dict__)
# {}
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


