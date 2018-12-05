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
c = Cat()
c.run()
