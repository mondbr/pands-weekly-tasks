# accounts_extra.py
# this program reads account number with at least 4 digits and outputs the account number with only the last 4 digits showing
# and replace all but the last four digits with 'X's.
# this is a modification to the other program: accounts.py

# author: Monika Dabrowska

# Taking input from the user
account_no = input ("Please enter an account number with at least 4 digits: ")


# Checking if the input contains at least for digits using "if"

if len(account_no) >= 4:

    # Replacing all but the last 4 digits with X
    hidden_digits = "x" * (len(account_no) -4) + account_no[-4:] 

        # "x" * (len(account_no) - the number of times that 'x' is repeated is equal to account no minus 4 last digits (source: chatGPT)
        # account_no[-4:] - adding last four digits to the result


    # Displying the result
    print(hidden_digits)

# If the number is not at least 4 digits
else: 
    print("Invalid account number. Please enter a valid account number with at least 4 digits")


