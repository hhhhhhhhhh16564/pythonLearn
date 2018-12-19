# Unix/Linux操作系统提供了一个fork()系统调用，它非常特殊。普通的函数调用，
# 调用一次，返回一次，但是fork()调用一次，返回两次，因为操作系统自动把当前进程（称为父进程）复制了一份（称为子进程），
# 然后，分别在父进程和子进程内返回。
# 子进程永远返回0，而父进程返回子进程的ID。这样做的理由是，一个父进程可以fork出很多子进程，
# 所以，父进程要记下每个子进程的ID，而子进程只需要调用getppid()就可以拿到父进程的ID。
#
# Python的os模块封装了常见的系统调用，其中就包括fork，可以在Python程序中轻松创建子进程：
import os
#拿到本进程的ID os.getpid()
#拿到父进程的ID os.getppid()
print('Process (%s) start...' % os.getpid())
# Only works on Unix/Linux/Mac:
pid = 1
# pid = os.fork()
print('**********')
if pid == 0:
    print('I am child process (%s) and my parent is %s' % (os.getpid(), os.getppid()))
else:
    print('I (%s) just create a child process(%s)' % (os.getpid(), pid))

#因为两个进程，所以下边的代码会打印两便
print('hhhh %s' % os.getpid())

# Process (6752) start...
# # I (6752) just create a child process(6753)
# # hhhh 6752
# # I am child process (6753) and my parent is 6752
# # hhhh 6753

# 由于Windows没有fork调用，上面的代码在Windows上无法运行。
# 有了fork调用，一个进程在接到新任务时就可以复制出一个子进程来处理新任务，
# 常见的Apache服务器就是由父进程监听端口，每当有新的http请求时，就fork出子进程来处理新的http请求。
# multiprocessing
# 由于Python是跨平台的，自然也应该提供一个跨平台的多进程支持。multiprocessing模块就是跨平台版本的多进程模块。

# multiprocessing模块提供了一个Process类来代表一个进程对象，下面的例子演示了启动一个子进程并等待其结束：
print('\n\n\n\n\n')
from multiprocessing import Process
import os

# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)' % (name, os.getpid()))



if __name__ =='__main__':
    print('parent process %s' % os.getpid())
    p = Process(target=run_proc, args=('test', ))
    print('child process will start.')
    p.start()
    p.join()
    print('Child process end.')
#运行结果
# parent process 8520
# child process will start.
# Run child process test (8521)
# Child process end.
#

# 创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例，用start()方法启动，这样创建进程比fork()还要简单。

# join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。

#如果要启动大量的子进程，可以用进程池的方式批量创建子进程：

from  multiprocessing import Pool
import  os, time, random

#random.random()用于生成一个0到1的随机浮点数 0 <= n <= 1.0
print('\n\n\n\n\n------------------')
def long_time_task(name):
    print('Run task %s (%s)...' %(name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task % run %0.2f seconds.' % (name, (end-start)))

if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in  range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocess done...')
    p.close()
    p.join()
    print('All subprocesses done.')

# 对Pool对象调用join()方法会等待所有子进程执行完毕，
# 调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了。

# task 0，1，2，3是立刻执行的，而task 4要等待前面某个task完成后才执行，
# 这是因为Pool的默认大小是4，因此，最多同时执行4个进程。这是Pool有意设计的限制，并不是操作系统的限制。


# 子进程

# subprocess模块可以让我们非常方便地启动一个子进程，然后控制其输入和输出。
#
# 下面的例子演示了如何在Python代码中运行命令nslookup www.python.org，这和命令行直接运行的效果是一样的：
print('\n\n\n\n\n^^^^^^^^^^^^^^^^^^')

import subprocess

print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit Code:', r)

# 如果子进程还需要输入，则可以通过communicate()方法输入：
print('\n\n\n\n\n*************')
import  subprocess
print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('utf-8'))
print('Exit code;', p.returncode)


# 上面的代码相当于在命令行执行命令nslookup，然后手动输入：
#
# set q=mx
# python.org
# exit


















