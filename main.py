
import datetime as dt
import pandas
import random
import smtplib
today=dt.datetime.now()
today_tuple=(today.month, today.day)

data=pandas.read_csv("birthdays.csv")

EMAIL="piusleealt1@gmail.com"
PASSWORD="06232000"


bday_dict={(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if (today_tuple in bday_dict):

    person=bday_dict[today_tuple]

    file_path=f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents=letter_file.read()
        contents=contents.replace("[NAME]", person["name"])
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(from_addr=EMAIL, to_addrs=person["email"],
                            msg=f"Subject: Happy birthday\n\n {contents}")




