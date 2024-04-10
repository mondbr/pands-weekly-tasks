# squareroot.py
# program that takes a positive floating-point number as input and outputs an approximation of its square root.
# this program does not to use the built in functions
# author: Monika Dabrowska
#
#
# Newton method: for any number N, the square root is 0.5 * (X + N / X)
# How Newton method works:  https://www.youtube.com/watch?v=FpOEx6zFf1o
#
#
#
# I am starting with creating my own function:

def sqrt(x):
        #  This is to approximate the square root of a positive float number using Newton's method.
            # Arg: x float: positive float number
            # Returns : float -  Approximation of the square root of x
    
    if x < 0:
        print ("This is a negative number, we need a positive number.") # number entered must be positive, so I am adding a check if the number is a positive number. 

        x = abs(x) # Using abs() module to transform negative number into a positive number.
        print (f"Let me fix this negative number to be positive: {x}") 
    
    # I  am starting the loop with my guess: X = N:

    guess = x  # variable 'guess' is a guess that first iteration equals to the number entered that we want to root
    

    # in while loop we are checking condition of convergence
    while True:
        # Calculate the next guess using Newton's method 0.5 * (X + N / X)
        next_guess = 0.5 * (guess + x / guess)

        # Check for convergence
        if abs(next_guess - guess) < 0.001: # Absolute value of the difference between iterations to be small 0.001 
            
            return next_guess # the condition above is met
        
        guess = next_guess  # updating the current guess to be the value of the next guess, 
                            # which is a better approximation of the square root of x according to Newton's method. 
                            # This process continues until the desired level of precision is achieved (0.001)

# Taking input from the user
number = float(input("Please enter a positive number: "))

# Calculating the square root using my sqrt function above
result = sqrt(number)

# Printing the result
print(f"The square root of {number} is approx. {round(result,1)}.") # adding round to show only 1 decimal place. 

# the alternative to rounding is 
# %:.2f is a function to print only 2 decimal places https://pythonguides.com/python-print-2-decimal-places/

    