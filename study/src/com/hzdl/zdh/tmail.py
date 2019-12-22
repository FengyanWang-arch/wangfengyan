#coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
_user="1453025309@qq.com"
_pwd="qmbhesxgyurqgiha"
_to="1453025309@qq.com"
msg=MIMEMultipart()
msg["Subject"]="测试一下"
msg["From"]=_user
msg["To"]=_to
part=MIMEText("你好")
msg.attach(part)

part=MIMEApplication(open('D:\\ceshi.xls','rb').read())
part.add_header('Content-Disposition','attachment',filename='ceshi.xls')
msg.attach(part)

part=MIMEApplication(open('D:\\liying.jpg','rb').read())
part.add_header('Content-Disposition','attachment',filename='liying.jpg')
msg.attach(part)

part=MIMEApplication(open('D:\\ceshi.pdf','rb').read())
part.add_header('Content-Disposition','attachment',filename='ceshi.pdf')
msg.attach(part)

part=MIMEApplication(open('D:\\ceshi.mp4','rb').read())
part.add_header('Content-Disposition','attachment',filename='ceshi.mp4')
msg.attach(part)

#part=MIMEText('<html>,<h1>你好！</h1></html>','html','utf-8')
#msg.attach(part)
try:
    s=smtplib.SMTP_SSL("smtp.qq.com",465)
    s.login(_user,_pwd)
    s.sendmail(_user,_to,msg.as_string())
    s.quit()
    print("完美！")
except smtplib.SMTPException as e:
    print("失败！")