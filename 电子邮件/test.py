import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr

# 发件人信息
from_addr = '18476026398@163.com'  # 你的163邮箱地址
password = 'LMCRGJNTOXFUMNOH'  # 使用你的163邮箱授权码
smtp_server = 'smtp.163.com'     # 163邮箱的SMTP服务器地址

# 收件人信息
to_addr = '2339576844@qq.com'

# 邮件内容
subject = '发送一新篇文章'
article = """
这是文章的标题呢

这是文章的正文部分。你可以根据实际情况在这里写完整的文章内容。
例如：Python是一种广泛使用的编程语言，因其简单易学和强大的功能而受到欢迎。
Python提供了丰富的库来处理各种任务，包括发送电子邮件。

这是文章的结尾部分。
"""

# 创建MIMEText对象，设置邮件正文为文章内容
msg = MIMEText(article, 'plain', 'utf-8')
msg['From'] = formataddr(["发件人名称从163", from_addr])  # 可自定义发件人名称
msg['To'] = formataddr(["收件人名称这是qq", to_addr])  # 可自定义收件人名称
msg['Subject'] = Header(subject, 'utf-8')  # 设置邮件主题
print(type(msg))

try:
    # 连接到SMTP服务器
    server = smtplib.SMTP(smtp_server, 25)  # 163邮箱使用的是25端口
    server.login(from_addr, password)  # 登录SMTP服务器
    server.sendmail(from_addr, [to_addr], msg.as_string())  # 发送邮件
    print("邮件发送成功")
except Exception as e:
    print(f"邮件发送失败: {e}")
finally:
    server.quit()
