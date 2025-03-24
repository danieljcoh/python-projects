from datetime import date, datetime, time

# TODO
# - expand to see the age between two different dates, born the first

def notes():
    today = date.today()
    print("today is: ", today)
    print("today is: ", today.day)
    print("today is: ", today.month)
    print("today is: ", today.year)

    print(today.strftime("%A %dth of %B %Y"))

    next_year = today.replace(year = today.year + 1)
    difference = abs(next_year - today)
    print(type(difference))
    print("only {} days until next year".format(difference.days))

    NikolaTesla = date(1856, 7, 10)
    print(NikolaTesla)
    print(NikolaTesla.weekday())


    now = datetime.now()
    print("It's the {}th minute of the {}nd hour, of the {}th day of the {}th month!".format(
        now.minute,
        now.hour,
        now.day,
        now.month
    ))

    # year-month-day hour-minute-sec-microsec(000)-timezone(+04:00)
    cher = datetime.fromisoformat("1986-04-26 01:23:40:000+04:00")
    print("The nuclear disaster in Chernobyl occurred on: ", cher)

    print(cher.strftime("The Cerhnobyl disaster occured on %A %B %dth, %Y at %X MSD(%Z)"))
    print("MSD is actually: ", cher.tzinfo)


    # TIME
    my_time = time(15, 33, 8)
    my_time = time.fromisoformat("15:33:08-07:00")
    print(my_time)
    print(my_time.strftime("%I:%M %p"))


    # Create a datetime object
    my_birthdate = date(2022, 5, 22)
    my_birthday_time = datetime.combine(my_birthdate, my_time)
    print(my_birthday_time)

def main():
    print("Enter a birthday to see how old you are: ")
    year = int(input("Input a year: "))
    month = int(input("Input a month number (1-12): "))
    day = int(input("Input a day number (1 - 31): "))

    user_birthday = date(year, month, day)
    today = date.today()
    age = today.year - year
    if month <= today.month:
        if day <= today.day:
            print(f"You are {age} years old!") 
        else:
            print(f"You are {age - 1} years old!")
    else:
        print(f"You are {age - 1} years old!")
    



    


if __name__ == "__main__":
    main()