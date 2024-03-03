# bank.py
# this program should:
#   - print the username and read in two money amounts
#   - add two amounts
#   - print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount 
# author : Monika Dabrowska

# this it to prompt the user and read in two money amounts (in cent)
name = input ("Enter your username: ")
print ("Hello " + name)
a = input ("Enter amount1(in cent): ")
b = input ("Enter amount2(in cent): ")

# add two amounts
sum = int(a) + int(b)

#take the sum of cents and convert it to represent money using decimal numbers such as 1.05.
import decimal
cents = sum
euro = decimal.Decimal(cents) / 100

# print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount
print (f"The sum of these is €{float(euro)}")




# lines 18-20 https://stackoverflow.com/questions/8637628/how-to-use-python-string-formatting-to-convert-an-integer-representing-cents-to

