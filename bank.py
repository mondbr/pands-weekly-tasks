# bank.py
# this program should:
#   - print the username and read in two money amounts
#   - add two amounts
#   - print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount 
# author : Monika Dabrowska


name = input ("Enter your username: ")
print ("Hello " + name)
a = input ("Enter amount1(in cent): ")
b = input ("Enter amount2(in cent): ")

# this it to prompt the user and read in two money amounts (in cent)

sum = int(a) + int(b)

# this add two amounts

import decimal
cents = sum
euro = decimal.Decimal(cents) / 100

#this is to take the sum of cents and convert it to represent money using decimal numbers such as 1.05.

print ("The sum of these is €",euro)

# print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount


# lines 20-22 https://stackoverflow.com/questions/8637628/how-to-use-python-string-formatting-to-convert-an-integer-representing-cents-to

