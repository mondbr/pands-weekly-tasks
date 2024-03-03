# weekly task03
# accounts.py
# this program reads in a 10 character account number and outputs the account number with only the last 4 digits showing (and the first 6 digits replaced with Xs).
# author: Monika Dabrowska


# takes input from the user: 
account_no = input ("Please enter an 10 digit account number: ")

# checking if the input is 10 characters long: 
if len(account_no) == 10:

    # Replacing the first 6 digits with a sequence of symbols
    a = account_no[:6]
    
    # dysplying the result
    print(a.replace(a, "XXXXXX"+ account_no[6:10])) 

# if input is not 10 characters long, program displays this message
else: 
    print("Invalid account number. Please enter exaclty 10 digits") 

#replace information:
    # https://www.w3schools.com/python/trypython.asp?filename=demo_string_replace
    
# conditions information:
    # https://www.w3schools.com/Python/python_conditions.asp
