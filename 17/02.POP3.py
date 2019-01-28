# 收取邮件就是编写一个MUA作为客户端，从MDA把邮件获取到用户的电脑或者手机上。收取邮件最常用的协议是POP协议，目前版本号是3，俗称POP3。
#
# Python内置一个poplib模块，实现了POP3协议，可以直接用来收邮件。
#
# 注意到POP3协议收取的不是一个已经可以阅读的邮件本身，而是邮件的原始文本，这和SMTP协议很像，SMTP发送的也是经过编码后的一大段文本。
#
# 要把POP3收取的文本变成可以阅读的邮件，还需要用email模块提供的各种类来解析原始文本，变成可阅读的邮件对象。
#
# 所以，收取邮件分两步：
#
# 第一步：用poplib把邮件的原始文本下载到本地；
#
# 第二部：用email解析原始文本，还原为邮件对象。

# 通过POP3下载邮件
from  email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr

import poplib
#输入邮件地址，口令和POP3服务器地址
email = 'ybyljhhhhh@163.com'
password = '123456789abcde'
pop3_server = 'pop.163.com'

#连接到pop3服务器
server = poplib.POP3(pop3_server)

#打开或关闭测试信息
server.set_debuglevel(0)

#可选： 打印POP3服务器的欢迎文字
print(server.getwelcome().decode('utf-8'))

#身份认证:
server.user(email)
server.pass_(password)

#start()返回邮件数量和占用空间
print('Message: %s. Size: %s' % server.stat())

#list() 返回所有邮件的编号
resp, mails, octers = server.list()

#可以查看返回的列表类似 类似[b'1 82923', b'2 2184', ...
print(mails)

#获取最新一封邮件， 注意索引号从1开始
index = len(mails)

resp, lines, octets = server.retr(index)

# lines存储了邮件的原始文本的每一行,
# 可以获得整个邮件的原始文本:

msg_content = b'\r\n'.join(lines).decode('utf-8')

#稍后解析出邮件：
msg = Parser().parsestr(msg_content)


# 可以根据邮件索引号直接从服务器删除邮件:
# server.dele(index)

#关闭连接:
server.quit()
# 用POP3获取邮件其实很简单，要获取所有邮件，只需要循环使用retr()把每一封邮件内容拿到即可。真正麻烦的是把邮件的原始内容解析为可以阅读的邮件对象。

# 解析邮件
# 解析邮件的过程和上一节构造邮件正好相反，因此，先导入必要的模块：
##########################//////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# 只需要一行代码就可以把邮件内容解析为Message对象：
# msg = Parser().parsestr(msg_content)
# 但是这个Message对象本身可能是一个MIMEMultipart对象，即包含嵌套的其他MIMEBase对象，嵌套可能还不止一层。
# 所以我们要递归地打印出Message对象的层次结构：


# 邮件的Subject或者Email中包含的名字都是经过编码后的str，要正常显示，就必须decode：

def decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value


def print_into(msg, indent = 0):
    if indent == 0:
        for header in ['From', 'To', 'Subject']:
            value = msg.get(header, '')
            if value:
                if header == 'Subject':
                    value = decode_str(value)






























