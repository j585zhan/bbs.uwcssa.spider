import smtplib
from getpass import getpass
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

gmail_user = raw_input('Enter your gmail account name: ') + '@gmail.com'
gmail_password = getpass('Enter your password for ' + gmail_user + ': ')

sent_from = gmail_user
to = gmail_user
email_text = 'test'

report_file = open('result.html')
html = report_file.read()
txt = MIMEText(html, 'html')

msg = MIMEMultipart('alternative')
msg['Subject'] = "Link"

msg.attach(txt)

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()
server.login(gmail_user, gmail_password)
server.sendmail(sent_from, to, msg.as_string())
server.close()

print "SEND"
