# 如果要把上面的两种分类都包含进来，我们就得设计更多的层次：
#
# 哺乳类：能跑的哺乳类，能飞的哺乳类；
# 鸟类：能跑的鸟类，能飞的鸟类。
# 如果要再增加“宠物类”和“非宠物类”，这么搞下去，类的数量会呈指数增长，很明显这样设计是不行的。

#正确的做法是采用多重继承。首先，主要的类层次仍按照哺乳类和鸟类设计：
class Animal(object):
    pass

# 大类:
class Mammal(Animal):
    pass

class Bird(Animal):
    pass

# 各种动物:
class Dog(Mammal):
    pass

class Bat(Mammal):
    pass

class Parrot(Bird):
    pass

class Ostrich(Bird):
    pass

# 现在，我们要给动物再加上Runnable和Flyable的功能，只需要先定义好Runnable和Flyable的类：
class Runnable(object):
    def run(self):
        print('Running...')

class Flyable(object):
    def fly(self):
        print('Flying...')

class Dog(Mammal, Runnable):
    pass

# 通过多重继承，一个子类就可以同时获得多个父类的所有功能
# MixIn
# 在设计类的继承关系时，通常，主线都是单一继承下来的，例如，Ostrich继承自Bird。但是，如果需要“混入”额外的功能，通过多重继承就可以实现，比如，让Ostrich除了继承自Bird外，再同时继承Runnable。这种设计通常称之为MixIn

# 为了更好地看出继承关系，我们把Runnable和Flyable改为RunnableMixIn和FlyableMixIn。类似的，你还可以定义出肉食动物CarnivorousMixIn和植食动物HerbivoresMixIn，让某个动物同时拥有好几个MixIn：

# class Dog(Mammal, RunnableMixIn, CarnivorousMixIn):
#     pass

# MixIn的目的就是给一个类增加多个功能，这样，在设计类的时候，我们优先考虑通过多重继承来组合多个MixIn的功能，而不是设计多层次的复杂的继承关系。

# Python自带的很多库也使用了MixIn。举个例子，Python自带了TCPServer和UDPServer这两类网络服务，而要同时服务多个用户就必须使用多进程或多线程模型，这两种模型由ForkingMixIn和ThreadingMixIn提供。通过组合，我们就可以创造出合适的服务来。

# 比如，编写一个多进程模式的TCP服务，定义如下：
# class MyTCPServer(TCPServer, ForkingMixIn):
#     pass

# 编写一个多线程模式的UDP服务，定义如下：
#
# class MyUDPServer(UDPServer, ThreadingMixIn):
#     pass

# 小结
# 由于Python允许使用多重继承，因此，MixIn就是一种常见的设计。
#
# 只允许单一继承的语言（如Java）不能使用MixIn的设计。

# 关于多重继承,其实,只要了解拓扑排序,就能很清楚的指导多重继承的查询顺序了,从入度为0的位置起,剪掉入度为0相关边,然后接着找下一个入度为0的位置,如此往复到最后,遇到有多个入度为0的时候,按最左原则取就行了,大体上就是这样了

# https://kevinguo.me/2018/01/19/python-topological-sorting/


# 在图论中，拓扑排序(Topological Sorting) 是一个 有向无环图(DAG,Directed Acyclic Graph) 的所有顶点的线性序列。且该序列必须满足下面两个条件：
#
# 每个顶点出现且只出现一次。
# 若存在一条从顶点A到顶点B的路径，那么在序列中顶点A出现在顶点B的前面。

# 从DAG途中选择一个没有前驱(即入度为0)的顶点并输出
# 从图中删除该顶点和所有以它为起点的有向边。
# 重复1和2直到当前DAG图为空或当前途中不存在无前驱的顶点为止。后一种情况说明有向图中必然存在环
class A(object):
    def foo(self):
        print('A foo')
    def bar(self):
        print('A bar')

class B(object):
    def foo(self):
        print('B foo')
    def bar(self):
        print('B bar')

class C1(A):
    pass

class C2(B):
    def bar(self):
        print('C2-bar')

class D(C1,C2):
    pass

if __name__ == '__main__':
    print(D.__mro__)
    d=D()
    d.foo()
    d.bar()

# D  c1  A  c2  B

# (<class '__main__.D'>, <class '__main__.C1'>, <class '__main__.A'>, <class '__main__.C2'>, <class '__main__.B'>, <class 'object'>)
# A foo
# A bar