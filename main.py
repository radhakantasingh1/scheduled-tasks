# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.


import datetime
import pandas
import random
import smtplib
import os

# import os and use it to get the Github repository secrets
my_email = os.environ.get("MY_EMAIL")
my_password = os.environ.get("MY_PASSWORD")

#reading birthday data
birthday_data=pandas.read_csv("birthdays.csv")

#today date
now=datetime.datetime.now()
today_month=now.month
today_date=now.day

today_birthdays=birthday_data[(birthday_data["month"]==today_month) & (birthday_data["day"]==today_date)]
print(today_birthdays)
for item in today_birthdays.iterrows():
    # selecting a ramdom letter content
    letter_no = random.randint(1, 3)
    with open(f"letter_templates/letter_{letter_no}.txt", "r") as file:
        mail = file.read()
    mail=mail.replace("[NAME]",item[1]["name"])
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=item[1]["email"],
            msg=f"Subject:Happy Birthday\n\n{mail}")
