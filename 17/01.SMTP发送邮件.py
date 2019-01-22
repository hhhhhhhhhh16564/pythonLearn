# SMTP是发送邮件的协议，Python内置对SMTP的支持，可以发送纯文本邮件、HTML邮件以及带附件的邮件。
#
# Python对SMTP支持有smtplib和email两个模块，email负责构造邮件，smtplib负责发送邮件。

from email.mime.text import MIMEText

msg = MIMEText('hello, send by python...', 'plain', 'utf-8')
# 注意到构造MIMEText对象时，第一个参数就是邮件正文，第二个参数是MIME的subtype，传入'plain'表示纯文本，
# 最终的MIME就是'text/plain'，最后一定要用utf-8编码保证多语言兼容性。

# 然后，通过SMTP发出去：

# from_addr = input('fromEmail:')
# password = input('password:')
#
# #输入收件人地址：
# to_addr = input('toEmail:')

# 输入SMTP服务器地址:
# stmp_server = input('SMTP server:')

from_addr = 'ybyljhhhhh@163.com'
password = '123456789abcde'
stmp_server = 'smtp.163.com'
to_addr = '1934779569@qq.com'

import  smtplib
# SMTP协议默认端口是25
server = smtplib.SMTP(stmp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()

# 我们用set_debuglevel(1)就可以打印出和SMTP服务器交互的所有信息。
# SMTP协议就是简单的文本命令和响应。login()方法用来登录SMTP服务器，sendmail()方法就是发邮件，由于可以一次发给多个人，所以传入一个list，邮件正文是一个str，as_string()把MIMEText对象变成str。





















