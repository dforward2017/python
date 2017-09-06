#/usr/bin/python
# _*_ coding:utf-8 _*_ 
import smtplib
from email.MIMEMultipart import MIMEMultipart     
from email.MIMEText import MIMEText
#这两个模块可以格式化邮件内容
 
#mail_server='smtp.exmail.qq.com'
mail_server='smtp.qq.com'
mail_server_port=465
 
mail_user='×××××××××@qq.com'
mail_password='bxrqbbrjgbwtbffa' #首先发送方的smtp服务需要打开,现在发送的时候需要授权码（密码）
 
from_addr='×××××××××@qq.com'
to_addr='@126.com'
subject_header='Subject: nothint intersting'
 
 
 
body='This is a not-very-interesting email.'
 
 
m=MIMEMultipart()                      #格式化邮件内容
m["To"]=to_addr
m["From"]=from_addr
m["Subject"]=subject_header
m.attach(MIMEText(body))
 
 
s=smtplib.SMTP_SSL(mail_server,mail_server_port) #通过SMTP SSL 465端口连接
s.set_debuglevel(1)
s.login(mail_user,mail_password)
#s.starttls()
s.sendmail(from_addr,to_addr,m.as_string())         
s.quit()
