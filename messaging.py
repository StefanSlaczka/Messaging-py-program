#to use this program, you need to have a google account that is verified with a phone mnumber
#do not spam messages to other people

import smtplib 
from email.message import EmailMessage

def email_alert(to):
    text = "Hello Myslef."
    msg = EmailMessage()
    msg.set_content(text)
    msg["to"] = to

    user = "*******@gmail.com" #put your email here
    msg["from"] = user
    password = "********" #put your 2 verfied password here

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    server.quit()

if __name__ == '__main__':
    email_alert("123-456-7890") # Replace with the person you want to send your messager
# ex:
# 123-456-7890.vtext.com (verizon) or you can use your a email if you provider
