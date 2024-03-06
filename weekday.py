# weekday.py
# program that outputs whether or not today is a weekday
# author: Monika Dabrowska




print ("Is today weekday?")

# Get the current day of the week (Monday is 0, Sunday is 6)
import datetime  # https://www.w3schools.com/python/python_datetime.asp

current_day = datetime.datetime.today().weekday()   # https://www.shecodes.io/athena/10185-how-to-check-what-day-of-the-week-it-is-in-python

# Check if it is a weekday or weekend

if current_day < 5: # Monday to Friday
    print ("Yes, unfotunately today is a weekday :(")

else: # 5th, 6th days - weekend
    print ("It is a weekend, yay! :) ")

