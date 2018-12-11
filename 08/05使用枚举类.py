# 当我们需要定义常量时，一个办法是用大写变量通过整数来定义，例如月份：
# JAN = 1
# 好处是简单，缺点是类型是int，并且仍然是变量。
# 更好的方法是为这样的枚举类型定义一个class类型，然后，每个常量都是class的一个唯一实例。Python提供了Enum类来实现这个功能：

from  enum import Enum

Month = Enum('Month',('Jan', 'Feb', 'Mar'))
# 这样我们就获得了Month类型的枚举类，可以直接使用Month.Jan来引用一个常量，或者枚举它的所有成员：
for name, member in Month.__members__.items():
    print(name, member, member.value)

# Jan Month.Jan 1
# Feb Month.Feb 2
# Mar Month.Mar 3
# value属性则是自动赋给成员的int常量，默认从1开始计数。
# 如果需要更精确地控制枚举类型，可以从Enum派生出自定义类：