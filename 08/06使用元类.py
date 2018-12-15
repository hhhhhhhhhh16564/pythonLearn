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

from  enum import  Enum , unique

@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Set = 6

# @unique装饰器可以帮助我们检查保证没有重复值。
day1 = Weekday.Mon
print(Weekday.Mon)   #Weekday.Mon
print(Weekday['Tue']) #Weekday.Tue
print(Weekday.Thu.value) # 4

print(day1 == Weekday.Mon) #True

print(Weekday(1)) #Weekday.Mon

for name, member in Weekday.__members__.items():
    print(name, '==>', member)


# 见，既可以用成员名称引用枚举常量，又可以直接根据value的值获得枚举常量。
class Gender(Enum):
    Male = 0
    Female = 1

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
bart = Student('Bart', Gender.Male)










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

from  enum import  Enum , unique

@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Set = 6

# @unique装饰器可以帮助我们检查保证没有重复值。
day1 = Weekday.Mon
print(Weekday.Mon)   #Weekday.Mon
print(Weekday['Tue']) #Weekday.Tue
print(Weekday.Thu.value) # 4

print(day1 == Weekday.Mon) #True

print(Weekday(1)) #Weekday.Mon

for name, member in Weekday.__members__.items():
    print(name, '==>', member)


# 见，既可以用成员名称引用枚举常量，又可以直接根据value的值获得枚举常量。
class Gender(Enum):
    Male = 0
    Female = 1

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
bart = Student('Bart', Gender.Male)










