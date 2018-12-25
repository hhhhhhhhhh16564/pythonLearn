
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time, sys, queue

from multiprocessing.managers import BaseManager

# 创建类似的QueueManager:
class QueueManager(BaseManager):
    pass

# 由于这个QueueManager只从网络上获取Queue，所以注册时只提供名字:

QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

# 连接到服务器，也就是运行task_master.py的机器:
sever_addr = '127.0.1'
print('Connect to server %s ...' % sever_addr)

# 端口和验证码注意保持与task_master.py设置的完全一致:
m = QueueManager(address=(sever_addr, 5000), authkey=b'abc')
#从网络连接
m.connect()

#获取Queue的对象
task = m.get_task_queue()
result = m.get_result_queue()

#从task队列取任务, 并把结果写入result队列
for i in  range(10):
    try:
        n = task.get(timeout=1)
        print('run task %d * %d ...' % (n, n))
        r = '%d * %d = %d' % (n,n, n*n)
        time.sleep(1)
        result.put(r)
    except Queue.Empty:
        print('task queue is empty.')

print('worker exit')
# 这个简单的Master/Worker模型有什么用？其实这就是一个简单但真正的分布式计算，把代码稍加改造，启动多个worker，
# 就可以把任务分布到几台甚至几十台机器上，比如把计算n*n的代码换成发送邮件，就实现了邮件队列的异步发送。
#
# Queue对象存储在哪？注意到task_worker.py中根本没有创建Queue的代码，所以，Queue对象存储在task_master.py进程中：

# 而Queue之所以能通过网络访问，就是通过QueueManager实现的。由于QueueManager管理的不止一个Queue，
# 所以，要给每个Queue的网络调用接口起个名字，比如get_task_queue。
#
# authkey有什么用？这是为了保证两台机器正常通信，不被其他机器恶意干扰。如果task_worker.py的authkey和task_master.py的authkey不一致，肯定连接不上。

