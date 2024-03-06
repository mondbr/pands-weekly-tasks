# collatz.py
# weekly task 04
# asks the user to input any positive integer and outputs the successive values of the following calculation:
# at each step calculate the next value by taking the current value and, if it is even, divide it by two
# if it is odd, multiply it by three and add one
# program ends if the current value is one

# author: Monika Dabrowska

# I start with setting up a definition
    # using def function - create/define a function:
def collatz(number): 
        # def - function
        # collatz - name of the function
        # number - value (variable we use for the function)

    # body of the function:
    if number % 2 == 0:
        return number // 2 # the result is returned using 'return' statement
        # If the number entered by the user is even, then this number is divided by 2
    
    else:
        return number * 3 + 1 # the result is returned using 'return' statement
        # if the number is odd, then this number is multiplied by 3 and added +1 
    
# Ask the user to input any positive integer
    # I need to check if user entered correct value (positive integer higher than 0)

while True: # creates an infinite loop. The loop continues until a valid input is provided.
    
    user_input = (input("Please enter a positive integer: ")) # variable - asking user to enter a number

    if user_input.isdigit(): # checking if entry is a digit
        number = int(user_input) # if it is digit, checking if is an integer
         
        if number > 0: # checking if integer is higher than 0
            break # 'break' exit the infinite loop if positive integer is entered
        else:
            print("Wrong number. Please enter a positive integer.") # if the number is negative this information is prompted
    else: # checking if entry is not a digit
        print("Invalid input. Please enter a positive integer.") # if user enters a string or float this information is prompted


# Display Collatz sequence while all conditions are met
        
print(f"Collatz sequence: {number}",  end=" ") # display the output in one line


# Output successive values until the current value is 1
while number != 1:
    number = collatz(number)
    print(number, end=" ") # display the output in one line



# https://www.w3schools.com/python/ref_keyword_def.asp
# https://www.w3schools.com/python/python_try_except.asp
# https://www.youtube.com/watch?v=lAp_5qTdOhM
