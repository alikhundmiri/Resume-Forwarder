#!/usr/bin/python
# -*- coding: latin-1 -*-
import sys
import smtplib;
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders

total_to = sys.argv[1]

for current_to in range (2, int(total_to)+2):
	toaddr = sys.argv[current_to]
	fromaddr = "your email address here"
    
	msg = MIMEMultipart()
    
	msg['From'] = fromaddr
	msg['To'] = toaddr
	msg['Subject'] = "The Subject of the Email"
	body = "The body of the email. remember to use '\n' instead of using the enter on the keyboard for new line \n like this!"
    
	msg.attach(MIMEText(body, 'plain'))

	filename = "file name. myresume.pdf"
	attachment = open("file location here /myresume.pdf", "rb")

	part = MIMEBase('application', "octet-stream")
	part.set_payload((attachment).read())
	encoders.encode_base64(part)
	part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
	msg.attach(part)

	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(fromaddr, "your password here")
	text = msg.as_string()
	server.sendmail(fromaddr, toaddr, text)
	print("Email sent!" + " FROM: " + fromaddr + " TO " + toaddr)
print("sent " + total_to + " email(s)")
server.quit()
