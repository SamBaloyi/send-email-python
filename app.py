import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

## 'Less secure app access' has to be turned on on your GMAIL account

## Sender and Recipient emails

print("\t\tLOGIN")
fromaddr = input("Enter your email: ")
passwd = input("Enter your password: (password will not be saved): ")
toaddr = input("Enter recipient email: ")
subject = input("Enter subject of email: ")

msg = MIMEMultipart()

#basic message headers
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = subject

#body of the email to the MIME message
body = input("Enter body of email: ")
msg.attach(MIMEText(body, 'plain'))
attachment = input("Enter path of file you wish to attach.\n(Press Enter if you" 
+ " wish to send email without attachment)")
if len(attachment) > 0:
	attachment = open(attachment, "rb")

filename = attachment.split("/")[-1]

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

msg.attach(part)

# log in to the server
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, passwd)
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
