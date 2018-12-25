from  datetime import  datetime
print(datetime.now())        #2018-12-24 16:43:38.660556
print(type(datetime.now()))  #<class 'datetime.datetime'>

# 注意到datetime是模块，datetime模块还包含一个datetime类，通过from datetime import datetime导入的才是datetime这个类。
# 如果仅导入import datetime，则必须引用全名datetime.datetime。
# datetime.now()返回当前日期和时间，其类型是datetime。

# 获取指定日期和时间
# 要指定某个日期和时间，我们直接用参数构造一个datetime：
dt = datetime(2015,4,19,20)  # 用指定日期时间创建datetime
print(dt)

# 在计算机中，时间实际上是用数字表示的。我们把1970年1月1日 00:00:00 UTC+00:00时区的时刻称为epoch time，
# 记为0（1970年以前的时间timestamp为负数），当前时间就是相对于epoch time的秒数，称为timestamp

#时间转换为时间戳
dt = datetime(2012, 4, 19, 20)
print(dt.timestamp())

# 注意Python的timestamp是一个浮点数。如果有小数位，小数位表示毫秒数。
# #
# # 某些编程语言（如Java和JavaScript）的timestamp使用整数表示毫秒数，这种情况下只需要把timestamp除以1000就得到Python的浮点表示方法。

# 本地时间是指当前操作系统设定的时区。例如北京时区是东8区，则本地时间：
# 2015-04-19 12:20:00
# 实际上就是UTC+8:00时区的时间：
# 2015-04-19 12:20:00 UTC+8:00


# 而此刻的格林威治标准时间与北京时间差了8小时，也就是UTC+0:00时区的时间应该是：
# 2015-04-19 04:20:00 UTC+0:00


# timestamp也可以直接被转换到UTC标准时区的时间：
print('---------------')
t = 1429417200.0
print(datetime.fromtimestamp(t)) # 本地时间

print(datetime.utcfromtimestamp(t))  # UTC时间


# str转换为datetime

# datetime.strptime)
cday = datetime.strptime('2015-6-1 19:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)
# 字符串'%Y-%m-%d %H:%M:%S'规定了日期和时间部分的格式。




# datetime转换为str
# strftime()

now = datetime.now()
print(now.strftime('%Y-%m-%d %H:%M:%S %a, %b %d'))

# datetime加减
# 对日期和时间进行加减实际上就是把datetime往后或往前计算，得到新的datetime。加减可以直接用+和-运算符，不过需要导入timedelta这个类：

from datetime import datetime, timedelta, timezone


new = datetime.now()
print(now)

print(now+timedelta(hours=10))

print(now+timedelta(days=4,seconds=10))
# 可见，使用timedelta你可以很容易地算出前几天和后几天的时刻。

#时区转换

# 我们可以先通过utcnow()拿到当前的UTC时间，再转换为任意时区的时间：
# 拿到UTC时间，并强制设置时区为UTC+0:00:
utc_dt  = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)
# astimezone()将转换时区为北京时间:
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)

# astimezone()将转换时区为东京时间:
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt)
# astimezone()将bj_dt转换时区为东京时间:
tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt2)

# 区转换的关键在于，拿到一个datetime时，要获知其正确的时区，然后强制设置时区，作为基准时间。
#
# 利用带时区的datetime，通过astimezone()方法，可以转换到任意时区。
#
# 注：不是必须从UTC+0:00时区转换到其他时区，任何带时区的datetime都可以正确转换，例如上述bj_dt到tokyo_dt的转换。

import re
def to_timestamp(dt_str, tz_str):
    hour = int(re.split(r'UTC|:', tz_str)[1])
    zone = timezone(timedelta(hours=hour))
    dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S').replace(tzinfo=zone)
    return dt.timestamp()


t = to_timestamp('2015-5-31 16:10:30', 'UTC+09:00')
print(t, '----')