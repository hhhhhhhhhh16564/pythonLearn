# -*- coding: utf-8 -*-
import argparse
################################################

# parser = argparse.ArgumentParser()
# parser.add_argument('integer', type=int, help='display an interer')
# args = parser.parse_args()
#
# print(args.integer)


#终端运行
# python3 02.0可选参数.py
# usage: 02.0可选参数.py [-h] interger
# # 02.0可选参数.py: error: the following arguments are required: interger

# python3 02.0可选参数.py  abcd
# usage: 02.0可选参数.py [-h] interger
# 02.0可选参数.py: error: argument interger: invalid int value: 'abcd'

# python3 02.0可选参数.py  -h
# usage: 02.0可选参数.py [-h] interger
#
# positional arguments:
#   interger    display an interer
#
# optional arguments:
#   -h, --help  show this help message and exit


#   python3 02.0可选参数.py  10
# 10



################################################
# 定位参数
# 上面的示例，其实就展示了定位参数的使用，我们再来看一个例子 - 计算一个数的平方：
parser = argparse.ArgumentParser()
# parser.add_argument('square', help='display square of given number', type=int)
# args = parser.parse_args()
# print(args.square * args.square)
#
# python3 02.0可选参数.py  10
# 100

################################################################################################################################################

# 可选参数
# 现在看下可选参数的用法，所谓可选参数，也就是命令行参数是可选的，废话少说，看下面例子：


parser = argparse.ArgumentParser()

parser.add_argument("--square", help="display a square of a given number", type=int)
parser.add_argument("--cubic", help="display a cubic of a given number", type=int)

args = parser.parse_args()

if args.square:
    print(args.square ** 2)

if args.cubic:
    print(args.cubic ** 3)

# python3 02.0可选参数.py  -h
# usage: 02.0可选参数.py [-h] [--square SQUARE] [--cubic CUBIC]
#
# optional arguments:
#   -h, --help       show this help message and exit
#   --square SQUARE  display a square of a given number
#   --cubic CUBIC    display a cubic of a given number



# python3 02.0可选参数.py  --square 8
# 64

# python3 02.0可选参数.py  --square 8 --cubic 9
# 64
# 729

# python3 02.0可选参数.py  4
# usage: 02.0可选参数.py [-h] [--square SQUARE] [--cubic CUBIC]
# 02.0可选参数.py: error: unrecognized arguments: 4





# default - 不指定参数时的默认值。
# type - 命令行参数应该被转换成的类型。
# required - 可选参数是否可以省略 (仅针对可选参数)。






