# weekday.py
# program that outputs whether or not today is a weekday
# author: Monika Dabrowska




print ("Is today a weekday?")

# Get the current day of the week (Monday is 0, Sunday is 6)
import datetime     # https://www.w3schools.com/python/python_datetime.asp
                    # provides classes for working with dates and times.

current_day = datetime.datetime.today().weekday()   # https://www.shecodes.io/athena/10185-how-to-check-what-day-of-the-week-it-is-in-python
                                                    # datetime.datetime.today() gets the current date and time.
                                                    # weekday() is a method that returns the day of the week as an integer, where Monday is 0 and Sunday is 6.
                                                    # current_day will be an integer representing the current day of the week. (Monday is 0, Sunday is 6)


# Check if it is a weekday or weekend

if current_day < 5: # Monday to Friday
    print ("Yes, unfotunately today is a weekday :(")

else: # 5th, 6th days - weekend
    print ("It is a weekend, yay! :) ")

