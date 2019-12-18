import datetime
from datetime import datetime, timedelta, date

today = datetime.now()


def date_input():
    year = str(input(" Please enter the year you were born "))
    month = str(input(" Please enter the month you were born "))
    day = str(input(" Please enter the day you were born "))
    birth = day + " " + month + " " + year
    print(birth)
    validate_date(birth)


def validate_date(fulldate):
    try:
        birthday = datetime.strptime(fulldate, "%d-%m-%Y")
        print("you're born in" + birthday.year)

        if birthday.year > today.year:
            print("that's impossible!")

        else:
            countdown = birthday - today

        print("You came to this world " + countdown + " days ago. Congratz!")

    except ValueError:
        print("please, try again")


if __name__ == "__main__":
    date_input()
