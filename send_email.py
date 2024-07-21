import smtplib
import ssl

host = "smtp.gmail.com"
port = 465


username = "jaedanparsons@gmail.com"
password = "ntqxepzrkmuolnrq"
password_with_spaces = "ntqx epzr kmuo lnrq"

receiver = "jaedanparsons@gmail.com"

context = ssl.create_default_context()

message = """\
Subject: Hi!
How are you?
Bye!
"""


with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)