import datetime
import smtplib
import datetime as dt
import random
import pandas

MY_EMAIL = "Enter GMAIL address"
MY_PASSWORD = "Enter GMAIL Password"


def main():
    now = dt.datetime.now()
    today = (now.day, now.month)
    data_df = pandas.read_csv("birthdays.csv")
    # Dictionary comprehension
    #{key:value for index, data_row in dataframe} Iterrows return series for each row, we uses month and day as key(touple)
    birthday_dict = {(data_row['month'], data_row['day']): data_row for (index, data_row) in data_df.iterrows()}

    if (now.month, now.day) in birthday_dict:
        file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
        birthday_person = birthday_dict[today]
        with smtplib.SMTP("smtp.gmail.com") as connection:
            with open(file_path, "r") as file:
                content = file.read()
                content = content.replace("[NAME]", birthday_person["name"])
            # Encrypted
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=birthday_person["email"],
                                msg=f"Subject:Hello\n\n{content}")
            connection.close()


if __name__ == '__main__':
    main()
