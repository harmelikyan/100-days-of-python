# import smtplib
#
# email = "tt2689933@gmail.com"
# password = "99714171h"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=email, password=password)
#     connection.sendmail(from_addr=email, to_addrs="harmelikyan@yahoo.com",
#                         msg="Subject:es inch es anum\n\nPrivet aziz")


import smtplib
import datetime as dt
import  random

now = dt.datetime.now()
today_day  = now.weekday()

email = "tt2689933@gmail.com"
password = "99714171h"

with open("quotes.txt", "r") as quotes:
    content = quotes.readlines()

random_email = random.choice(content)

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=email, password=password)
    if today_day == 0:
        connection.sendmail(from_addr=email, to_addrs="harmelikyan@yahoo.com",
                            msg=f"Subject:Motivational email\n\n{random_email}")

