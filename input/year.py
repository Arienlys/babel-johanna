# year

import datetime
from datetime import datetime, timedelta, date

today = datetime.now()


def date_input():
    """
    
    """
    try:
        year = int(input(" Please enter the year you were born "))
        month = int(input(" Please enter the month you were born "))
        day = int(input(" Please enter the day you were born "))

    except:
        print("what you tried to put isn't what expected. Please try again")
        date_input()

    ye = validate_year(year)

    date_time_obj = datetime(ye, month, day)
    validate_date(date_time_obj)


def validate_year(valyear):
    todayyear = today.year
    if isinstance(valyear, str):
        valyear = int(valyear)

    if valyear < 100:
        todayyear -= 2000
        if valyear <= todayyear:
            valyear += 2000
        else:
            valyear += 1900

    return valyear


def validate_date(fulldate):
    print("you're born in " + str(fulldate.year))

    if fulldate.year > today.year:
        print("that's impossible!")

    else:
        countdown = today - fulldate
        age = int(countdown.days / 365.25)

    print("meaning")
    print("You came to this world " + str(countdown.days) + " days ago. Congratz!")
    print("you are actually " + str(age) + " years old")


if __name__ == "__main__":
    date_input()
