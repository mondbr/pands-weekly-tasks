# weekday.py
# program that outputs whether or not today is a weekday
# author: Monika Dabrowska



import datetime                             # https://www.w3schools.com/python/python_datetime.asp
x = datetime.datetime.now()

print ("Today is "+ x.strftime("%A"))       # https://www.w3schools.com/python/trypython.asp?filename=demo_datetime_strftime_a2
