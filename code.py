import smtplib



def main_send():
    mails_list=['ayodhyankit@gmail.com']
    for i in mails_list:
        s = smtplib.SMTP('smtp.gmail.com', 587)


        s.starttls()

        s.login("cssgravity0@gmail.com", "password")

        message = "hello am here"

        s.sendmail("cssgravity0@gmail.com",i, message)


        s.quit()


print(main_send())
