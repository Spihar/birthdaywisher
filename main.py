##################### Extra Hard Starting Project ######################
import datetime
import random
import smtplib
import pandas as pd
import pandas as pd
import datetime as dt
import csv

email = "patrick.nuvvu@gmail.com"
password = "rrcetpcbzhqsegmq"

# 1. Update the birthdays.csv
data = pd.read_csv("birthdays.csv")
dob = dt.datetime(year=2005, month=5, day=13)
year = dob.year
month = dob.month
day = dob.day

# data.loc[1] = ['harthik', 'harthik.cygnusx1@gmail.com', year, month, day]
'''print(data.head())
data.loc[0]=['Test','patrcik.nuvvu@yahoo.com',year,month,day]
data.to_csv('birthdays.csv')'''

# 2. Check if today matches a birthday in the birthdays.csv
today = dt.datetime.today()
t_month = today.month
t_day = today.day
if data.loc[0, 'month'] == t_month:
    if data.loc[0, 'day'] == t_day:
        birthday = True
    else:
        birthday = False

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
letter = random.choice(['letter_1.txt', 'letter_2.txt', 'letter_3.txt'])
if birthday:
    with open(f'./letter_templates/{letter}') as temp:
        d = temp.readlines()
        print(data.loc[0, 'name'])
        d[0] = d[0].replace('[NAME]', data.loc[0, 'name'])
        d[-1]=d[-1].replace('Angela','harthik')
        print(d[0])
    with open(f'./letter_templates/{letter}', 'w') as temp:
        for lines in d:
            temp.write(lines)
    message=''.join(d)
# 4. Send the letter generated in step 3 to that person's email address.
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=email,password=password)
    connection.sendmail(from_addr=email,
                        to_addrs="karthikchowdarymaddipatla1505@gmail.com",
                        msg=f'Subject:happy birthday\n\n{message}')

