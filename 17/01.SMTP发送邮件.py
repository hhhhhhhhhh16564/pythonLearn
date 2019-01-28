# SMTP是发送邮件的协议，Python内置对SMTP的支持，可以发送纯文本邮件、HTML邮件以及带附件的邮件。
#
# Python对SMTP支持有smtplib和email两个模块，email负责构造邮件，smtplib负责发送邮件。
import  smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr, formataddr


def textEmail():
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
    to_addr = '2313567416@qq.com'
    subject = '放假通知'
    content = '老夫聊发少年狂，左牵黄，右擎苍，锦帽貂裘，千骑卷平冈。为报倾城随太守，亲射虎，看孙郎。' \
              '酒酣胸胆尚开张。鬓微霜，又何妨！持节云中，何日遣冯唐？会挽雕弓如满月，西北望，射天狼。'

    msg = MIMEText(content, 'plain', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    # msg['From'] = Header('hhhhhh', 'utf-8')
    # msg['To'] = Header('bbbbb', 'utf-8')
    msg['From'] = from_addr
    msg['To'] = to_addr


    # SMTP协议默认端口是25
    server = smtplib.SMTP(stmp_server, 25)
    server.set_debuglevel(0)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()



    # 我们用set_debuglevel(1)就可以打印出和SMTP服务器交互的所有信息。
    # SMTP协议就是简单的文本命令和响应。login()方法用来登录SMTP服务器，sendmail()方法就是发邮件，由于可以一次发给多个人，所以传入一个list，邮件正文是一个str，as_string()把MIMEText对象变成str。

# textEmail()


def textEmail1():
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

    def _format_addr(s):
        name, addr = parseaddr(s)
        return formataddr((Header(name, 'utf-8').encode(), addr))


    from_addr = 'ybyljhhhhh@163.com'
    password = '123456789abcde'
    stmp_server = 'smtp.163.com'
    to_addr = '2313567416@qq.com'
    subject = '放假通知'
    content = '老夫聊发少年狂，左牵黄，右擎苍，锦帽貂裘，千骑卷平冈。为报倾城随太守，亲射虎，看孙郎。' \
              '酒酣胸胆尚开张。鬓微霜，又何妨！持节云中，何日遣冯唐？会挽雕弓如满月，西北望，射天狼。'
    # 我们编写了一个函数_format_addr()
    # 来格式化一个邮件地址。注意不能简单地传入name < addr @ example.com >，因为如果包含中文，需要通过Header对象进行编码。
    #
    # msg['To']
    # 接收的是字符串而不是list，如果有多个邮件地址，用, 分隔即可。
    #
    # 再发送一遍邮件，就可以在收件人邮箱中看到正确的标题、发件人和收件人：
    msg = MIMEText(content, 'plain', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = _format_addr('python爱好者 <%s>' % from_addr)
    msg['To'] = _format_addr('管理员ABC <%s>' % to_addr)


    # SMTP协议默认端口是25
    server = smtplib.SMTP(stmp_server, 25)
    server.set_debuglevel(0)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()

    # 我们用set_debuglevel(1)就可以打印出和SMTP服务器交互的所有信息。
    # SMTP协议就是简单的文本命令和响应。login()方法用来登录SMTP服务器，sendmail()方法就是发邮件，
    # 由于可以一次发给多个人，所以传入一个list，邮件正文是一个str，as_string()把MIMEText对象变成str。

# textEmail1()



#发送HTML邮件
# 如果我们要发送HTML邮件，而不是普通的纯文本文件怎么办？方法很简单，在构造MIMEText对象时，把HTML字符串传进去，再把第二个参数由plain变为html就可以了：
def HTMLEmail():
    def _format_addr(s):
        name, addr = parseaddr(s)
        return formataddr((Header(name, 'utf-8').encode(), addr))


    from_addr = 'ybyljhhhhh@163.com'
    password = '123456789abcde'
    stmp_server = 'smtp.163.com'
    to_addr = '2313567416@qq.com'
    subject = '放假通知'
    content = '<html><body><h1>Hello</h1>' + \
              '<p>send by <a href="http://www.python.org">Python</a>...</p>' + \
              '</body></html>'
    # 我们编写了一个函数_format_addr()
    # 来格式化一个邮件地址。注意不能简单地传入name < addr @ example.com >，因为如果包含中文，需要通过Header对象进行编码。
    #
    # msg['To']
    # 接收的是字符串而不是list，如果有多个邮件地址，用, 分隔即可。
    #
    # 再发送一遍邮件，就可以在收件人邮箱中看到正确的标题、发件人和收件人：
    msg = MIMEText(content, 'html', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = _format_addr('python爱好者 <%s>' % from_addr)
    msg['To'] = _format_addr('管理员ABC <%s>' % to_addr)


    # SMTP协议默认端口是25
    server = smtplib.SMTP(stmp_server, 25)
    server.set_debuglevel(0)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()


# HTMLEmail()


# 发送附件
# 如果Email中要加上附件怎么办？带附件的邮件可以看做包含若干部分的邮件：
# 文本和各个附件本身，所以，可以构造一个MIMEMultipart对象代表邮件本身，
# 然后往里面加上一个MIMEText作为邮件正文，再继续往里面加上表示附件的MIMEBase对象即可：
# 邮件对象

from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
def attachEmail():
    def _format_addr(s):
        name, addr = parseaddr(s)
        return formataddr((Header(name, 'utf-8').encode(), addr))


    from_addr = 'ybyljhhhhh@163.com'
    password = '123456789abcde'
    stmp_server = 'smtp.163.com'
    to_addr = '2313567416@qq.com'
    subject = '来自你大爷的问候......'
    content = '唧唧复唧唧，木兰当户织。不闻机杼声，惟闻女叹息。' \
              '问女何所思，问女何所忆。女亦无所思，女亦无所忆。' \
              '昨夜见军帖，可汗大点兵，军书十二卷，卷卷有爷名。' \
              '阿爷无大儿，木兰无长兄，愿为市鞍马，从此替爷征。' \
              '东市买骏马，西市买鞍鞯，南市买辔头，北市买长鞭。' \
              '旦辞爷娘去，暮宿黄河边，不闻爷娘唤女声，但闻黄河流水鸣溅溅。' \
              '旦辞黄河去，暮至黑山头，不闻爷娘唤女声，但闻燕山胡骑鸣啾啾'

    msg = MIMEMultipart()
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = _format_addr('python爱好者 <%s>' % from_addr)
    msg['To'] = _format_addr('管理员ABC <%s>' % to_addr)

    #邮件正文是MIMEText:
    text = MIMEText(content, 'plain', 'utf-8')
    msg.attach(text)

    with open('./011.jpg', 'rb') as f:
        #设置附件的MIME和文件名, 这里是png类型
        mime = MIMEBase('image', 'jpg', filename = '011.jpg')
        #加上必要的头信息:
        mime.add_header('Content-Disposition', 'attachment', filename = '011.jpg')
        mime.add_header('Content-ID', '<0>')
        mime.add_header('X-Attachment-Id', '0')
        #把附件内容读进来
        mime.set_payload(f.read())
        #用Base64编码:
        encoders.encode_base64(mime)
        #添加到MiMEMultipart:
        msg.attach(mime)

    # SMTP协议默认端口是25
    server = smtplib.SMTP(stmp_server, 25)
    server.set_debuglevel(0)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()

# attachEmail()

# 发送图片
# 如果要把一个图片嵌入到邮件正文中怎么做？直接在HTML邮件中链接图片地址行不行？
# 答案是，大部分邮件服务商都会自动屏蔽带有外链的图片，因为不知道这些链接是否指向恶意网站。
#
# 要把图片嵌入到邮件正文中，我们只需按照发送附件的方式，先把邮件作为附件添加进去，
# 然后，在HTML中通过引用src="cid:0"就可以把附件作为图片嵌入了。如果有多个图片，给它们依次编号，然后引用不同的cid:x即可。
# 把上面代码加入MIMEMultipart的MIMEText从plain改为html，然后在适当的位置引用图片：

def attachImage():
    def _format_addr(s):
        name, addr = parseaddr(s)
        return formataddr((Header(name, 'utf-8').encode(), addr))


    from_addr = 'ybyljhhhhh@163.com'
    password = '123456789abcde'
    stmp_server = 'smtp.163.com'
    to_addr = '2313567416@qq.com'
    subject = '来自你大爷的问候......'
    content = '<html><body><h1>Hello</h1>' \
              +'<p><img src="cid:1"></p>' \
              + '</body></html>'

    msg = MIMEMultipart()
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = _format_addr('python爱好者 <%s>' % from_addr)
    msg['To'] = _format_addr('管理员ABC <%s>' % to_addr)
    #邮件正文是MIMEText:
    text = MIMEText(content, 'html', 'utf-8')
    msg.attach(text)
    with open('./011.jpg', 'rb') as f:
        #设置附件的MIME和文件名, 这里是png类型
        mime = MIMEBase('image', 'jpg', filename = '011.jpg')
        #加上必要的头信息:
        mime.add_header('Content-Disposition', 'attachment', filename = '011.jpg')
        mime.add_header('Content-ID', '<1>')
        mime.add_header('X-Attachment-Id', '1')
        #把附件内容读进来
        mime.set_payload(f.read())
        #用Base64编码:
        encoders.encode_base64(mime)
        #添加到MiMEMultipart:
        msg.attach(mime)

    # SMTP协议默认端口是25
    server = smtplib.SMTP(stmp_server, 25)
    server.set_debuglevel(0)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()

# attachImage()

# 同时支持HTML和Plain格式
# 如果我们发送HTML邮件，收件人通过浏览器或者Outlook之类的软件是可以正常浏览邮件内容的，
# 但是，如果收件人使用的设备太古老，查看不了HTML邮件怎么办？

# 办法是在发送HTML的同时再附加一个纯文本，如果收件人无法查看HTML格式的邮件，就可以自动降级查看纯文本邮件。
# 利用MIMEMultipart就可以组合一个HTML和Plain，要注意指定subtype是alternative：
# alternative

def htmlPlainEmail():
    def _format_addr(s):
        name, addr = parseaddr(s)
        return formataddr((Header(name, 'utf-8').encode(), addr))

    from_addr = 'ybyljhhhhh@163.com'
    password = '123456789abcde'
    stmp_server = 'smtp.163.com'
    to_addr = '2313567416@qq.com'
    subject = '来自你大爷的问候......'
    content = '<html><body><h1>Hello</h1>' \
              + '<p>😁哈哈哈哈😝😝</p>' \
              + '</body></html>'

    msg = MIMEMultipart()
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = _format_addr('python爱好者 <%s>' % from_addr)
    msg['To'] = _format_addr('管理员ABC <%s>' % to_addr)
    # 邮件正文是MIMEText:
    text = MIMEText(content, 'html', 'utf-8')
    msg.attach(text)

    text1 = MIMEText('咔咔咔咔咔咔', 'plain', 'utf-8')
    msg.attach(text1)

    # SMTP协议默认端口是25
    server = smtplib.SMTP(stmp_server, 25)
    server.set_debuglevel(0)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()

# htmlPlainEmail()

# 加密SMTP
# 使用标准的25端口连接SMTP服务器时，使用的是明文传输，发送邮件的整个过程可能会被窃听。
# 要更安全地发送邮件，可以加密SMTP会话，实际上就是先创建SSL安全连接，然后再使用SMTP协议发送邮件。
# 某些邮件服务商，例如Gmail，提供的SMTP服务必须要加密传输。我们来看看如何通过Gmail提供的安全SMTP发送邮件。
# 必须知道，Gmail的SMTP端口是587，因此，修改代码如下：

def safeEmail():
    def _format_addr(s):
        name, addr = parseaddr(s)
        return formataddr((Header(name, 'utf-8').encode(), addr))

    from_addr = 'ybyljhhhhh@163.com'
    password = '123456789abcde'
    smtp_server = 'smtp.163.com'
    smtp_port = 25

    to_addr = '2313567416@qq.com'
    subject = '来自你大爷的问候......'
    content = '<html><body><h1>Hello</h1>' \
              + '<p>😁哈哈哈哈😝😝</p>' \
              + '</body></html>'

    msg = MIMEMultipart()
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = _format_addr('python爱好者 <%s>' % from_addr)
    msg['To'] = _format_addr('管理员ABC <%s>' % to_addr)
    # 邮件正文是MIMEText:
    text = MIMEText(content, 'html', 'utf-8')
    msg.attach(text)

    text1 = MIMEText('咔咔咔咔咔咔', 'plain', 'utf-8')
    msg.attach(text1)

    # SMTP协议默认端口是25
    server = smtplib.SMTP(smtp_server, smtp_port )
    server.starttls()
    server.set_debuglevel(0)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()

safeEmail()

# 使用Python的smtplib发送邮件十分简单，只要掌握了各种邮件类型的构造方法，正确设置好邮件头，就可以顺利发出。
# 构造一个邮件对象就是一个Messag对象，如果构造一个MIMEText对象，就表示一个文本邮件对象，如果构造一个MIMEImage对象，
# 就表示一个作为附件的图片，要把多个对象组合起来，就用MIMEMultipart对象，而MIMEBase可以表示任何对象。它们的继承关系如下：
# Message
# +- MIMEBase
#    +- MIMEMultipart
#    +- MIMENonMultipart
#       +- MIMEMessage
#       +- MIMEText
#       +- MIMEImage



# parseaddr(address)
# 解析地址 - 它应该是一些包含地址的字段的值，例如 To 或 Cc - 到其组成的 realname 和 电子邮件地址 部分。
# 返回该信息的元组，除非解析失败，在这种情况下返回一个2元组的 ('', '')。
#
# email.utils.formataddr(pair, charset='utf-8')
# parseaddr() 的逆，这需要一个形式为 (realname, email_address) 的2元组，
