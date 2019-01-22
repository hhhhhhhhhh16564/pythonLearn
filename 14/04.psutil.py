# 获取CPU信息
import psutil
# CPU逻辑数量
print(psutil.cpu_count())

# CPU物理核心  2说明是双核超线程, 4则是4核非超线程
print(psutil.cpu_count(logical=False))

# 统计CPU的用户／系统／空闲时间
print(psutil.cpu_times())
# scputimes(user=6948.37, nice=0.0, system=3588.36, idle=44233.16)
# 再实现类似top命令的CPU使用率，每秒刷新一次，累计10次：
for x in range(10):
    print(psutil.cpu_percent(interval=0.1, percpu=True))


# 获取内存信息
# 使用psutil获取物理内存和交换内存信息，分别使用

print(psutil.virtual_memory())
print(psutil.swap_memory())
# svmem(total=8589934592, available=1865269248, percent=78.3, used=4172673024, free=313872384, active=1786179584, inactive=1544478720, wired=2386493440)
# sswap(total=2147483648, used=1002962944, free=1144520704, percent=46.7, sin=22938415104, sout=147021824)
# 返回的是字节为单位的整数，可以看到，总内存大小是8589934592 = 8 GB，4172673024 =   GB，使用了78.3。
# 而交换区大小是2147483648

# 获取磁盘信息
# 可以通过psutil获取磁盘分区、磁盘使用率和磁盘IO信息：
# 磁盘分区信息
print(psutil.disk_partitions())
# [sdiskpart(device='/dev/disk1s1', mountpoint='/', fstype='apfs', opts='rw,local,rootfs,dovolfs,journaled,multilabel'), sdiskpart(device='/dev/disk1s4', mountpoint='/private/var/vm', fstype='apfs', opts='rw,noexec,local,dovolfs,dontbrowse,journaled,multilabel,noatime')]

# 磁盘使用情况
print(psutil.disk_usage('/'))
# sdiskusage(total=250685575168, used=229088387072, free=15529627648, percent=93.7)

# 磁盘IO
print(psutil.disk_io_counters())
# sdiskio(read_count=1151599, write_count=496496, read_bytes=29576871936, write_bytes=18278526976, read_time=604881, write_time=206316)


# 获取网络信息
print(psutil.net_io_counters()) # 获取网络读写字节／包的个数
print(psutil.net_if_addrs()) # 获取网络接口信息
print(psutil.net_if_stats()) # 获取网络接口状态


# 通过psutil可以获取到所有进程的详细信息：
print(psutil.pids())
p = psutil.Process(1185) # 获取指定进程ID=3776，其实就是当前Python交互环境
print(p.name())

# print(p.exe())  # 进程exe路径)

#具体查看  https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001511052957192bb91a56a2339485c8a8c79812b400d49000