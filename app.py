import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

## 'Less secure app access' has to be turned on on your GMAIL account

## Sender and Recipient emails
fromaddr = "sbaloyi@student.wethinkcode.co.za"
toaddr = "sambaloyi2017@gmail.com"

msg = MIMEMultipart()

#basic message headers
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Python Email"

#body of the email to the MIME message
body = "The very first python email body"
msg.attach(MIMEText(body, 'plain'))
filename = "NAME OF THE FILE WITH ITS EXTENSION"
attachment = open("C:/sandbox/send-email-python/picture.jpg", "rb")

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

msg.attach(part)

# log in to the server
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "PasswordGoesHere(that's not my password FYI)")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()