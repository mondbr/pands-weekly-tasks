# weekly task03
# accounts.py
# this program reads in a 10 character account number and outputs the account number with only the last 4 digits showing (and the first 6 digits replaced with Xs).
# author: Monika Dabrowska

accountno = input ("Please enter an 10 digit account number: ")
a = accountno[:5]

print(a.replace(a, "XXXXXX"+ accountno[6:10]))
# https://www.w3schools.com/python/trypython.asp?filename=demo_string_replace
