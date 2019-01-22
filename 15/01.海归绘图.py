# 导入turtle包的所有内容:
from turtle import *

# 设置笔刷宽度:
def square():
    width(4)
    # 前进:
    forward(200)
    # 右转90度:
    right(90)

    # 笔刷颜色:
    pencolor('red')
    forward(100)
    right(90)

    pencolor('green')
    forward(200)
    right(90)

    pencolor('blue')
    forward(100)
    right(90)

    # 调用done()使得窗口等待被关闭，否则将立刻关闭窗口:
    done()

# 1.forward() | fd():向前移动指定的距离。参数：一个数字（integer or float)）
# turtle.forward(25)

# 2.backward() | bk() | back():向后移动指定的距离。参数：一个数字（integer or float)）。
# turtle.backward(30)

# 3.right() | rt():以角度单位向右转动。参数：一个数字（integer or float)）。单位默认为度数，可以通过degrees()和radians()进行设置。
# turtle.right(45)


# 4.left() | lt():以角度单位向右转动。参数：一个数字（integer or float)）。单位默认为度数，可以通过degrees()和radians()进行设置。
# turtle.left(45)


# 5.setx():设置第一个坐标的值即X方向。参数：一个数字（integer or float)）。
# turtle.setx(10)

# 6.sety():设置第二个坐标的值即Y方向。参数：一个数字（integer or float)）。
# turtle.sety(10)



# bob.fd(100) #向前走
# bob.bk(100) #向后走
#
# bob.lt(90) #向左转
# bob.rt(90) #向右转
#
# bob.pu() #(pen up)抬笔
# bob.pd() #(pen down)落笔
# 1）turtle.pensize()：设置线条的粗细；
# 2）turtle.speed()：设置绘制的速度，1-10，1最慢，10最快；
# 4）turtle.circle(50,steps=3)：circle函数在之前用到过，是画一个半径为radius的圆，这里是扩展，steps表示在半径为50的圆内的内置steps多边形；
# turtle.goto(x,y)	将画笔移动到坐标为x,y的位置
# turtle.penup()	移动时不绘制图形,提起笔，用于另起一个地方绘制时用
# turtle.pendown()	移动时绘制图形,缺省时也为绘制


# square()

# 从程序代码可以看出，海龟绘图就是指挥海龟前进、转向，海龟移动的轨迹就是绘制的线条。要绘制一个长方形，只需要让海龟前进、右转90度，反复4次。
# 调用width()函数可以设置笔刷宽度，调用pencolor()函数可以设置颜色。更多操作请参考turtle库的说明

# 绘图完成后，记得调用done()函数，让窗口进入消息循环，等待被关闭。否则，由于Python进程会立刻结束，将导致窗口被立刻关闭。
# turtle包本身只是一个绘图库，但是配合Python代码，就可以绘制各种复杂的图形。例如，通过循环绘制5个五角星：

# 1)、逆时针旋转angle度  turtle.seth(angle)

# • turtle.setup(width,height,startx,starty)
# 　　-setup() 设置窗体的位置和大小
# 　　相对于桌面的起始点的坐标以及窗口的宽度高度，若不写窗口的起始点，则默认在桌面的正中心
# 　　窗体的坐标原点默认在窗口的中心
# • 绝对坐标
# 　　○ turtle.goto(100,100):指从当前的点指向括号内所给坐标
# • 海龟坐标，把当前点当做坐标，有前方向，后方向，左方向，右方向
# 　　○ turtle.fd(d):指沿着海龟的前方向运行
# 　　○ turtle.bk(d):指沿着海龟的反方向运行
# 　　○ turtle.circle(r,angle):指沿着海龟左侧的某一点做圆运动
# • 绝对角度
# 　　○ turtle.seth(angle):只改变海龟的行进方向（角度按逆时针），但不行进，angle为绝对度数
# • 海龟角度
# 　　○ turtle.left(angle)
# 　　○ turtle.right(angle)

from turtle import *

# 设置色彩模式是RGB:
colormode(255)

lt(90)

lv = 14
l = 120
s = 45

width(lv)

# 初始化RGB颜色:
r = 0
g = 0
b = 0
pencolor(r, g, b)

penup()
bk(l)
pendown()
fd(l)

def draw_tree(l, level):
    global r, g, b
    # save the current pen width
    w = width()

    # narrow the pen width
    width(w * 3.0 / 4.0)
    # set color:
    r = r + 1
    g = g + 2
    b = b + 3
    pencolor(r % 200, g % 200, b % 200)

    l = 3.0 / 4.0 * l

    lt(s)
    fd(l)

    if level < lv:
        draw_tree(l, level + 1)
    bk(l)
    rt(2 * s)
    fd(l)

    if level < lv:
        draw_tree(l, level + 1)
    bk(l)
    lt(s)

    # restore the previous pen width
    width(w)

speed("fastest")

draw_tree(l, 4)

done()






























