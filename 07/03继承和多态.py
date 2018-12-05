# 在OOP程序设计中，当我们定义一个class的时候，可以从某个现有的class继承，新的class称为子类（Subclass），而被继承的class称为基类、父类或超类（Base class、Super class）。

#比如，我们已经编写了一个名为Animal的class，有一个run()方法可以直接打印：
# 当我们需要编写Dog和Cat类时，就可以直接从Animal类继承：
class Animal(object):
    def run(self):
        print('Animal is running...')
class Dog(Animal):
    pass

class Cat(Animal):
    pass
c = Cat()
c.run()

# 继承的第二个好处需要我们对代码做一点改进。你看到了，无论是Dog还是Cat，它们run()的时候，显示的都是Animal is running...，符合逻辑的做法是分别显示Dog is running...和Cat is running...，因此，对Dog和Cat类改进如下：

class Cat(object):
    def run(self):
        print('Cat is running...')

class Dog(object):
    def run(self):
        print('Dog is running...')
c = Cat()
c.run()
#要理解什么是多态，我们首先要对数据类型再作一点说明。当我们定义一个class的时候，我们实际上就定义了一种数据类型。我们定义的数据类型和Python自带的数据类型，比如str、list、dict没什么两样：

# 判断一个变量是否是某个类型可以用isinstance()判断：
c = Dog()
# isinstance 类似于oc 的iskindof
#C的真正类型和它的父类都会返回ture
print(isinstance(c, Animal))
print(isinstance(c, Dog))

def run_twice(animal):
    animal.run()
    animal.run()
run_twice(Cat())
run_twice(Dog())

#对于一个变量，我们只需要知道它是Animal类型，无需确切地知道它的子类型，就可以放心地调用run()方法，而具体调用的run()方法是作用在Animal、Dog、Cat还是Tortoise对象上，由运行时该对象的确切类型决定，这就是多态真正的威力：调用方只管调用，不管细节，而当我们新增一种Animal的子类时，只要确保run()方法编写正确，不用管原来的代码是如何调用的。这就是著名的“开闭”原则：

# 对于静态语言（例如Java）来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，否则，将无法调用run()方法。
#
# 对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了：
# 这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。

















