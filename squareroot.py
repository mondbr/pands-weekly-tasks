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
        return None # the number cannot be negative  (I know this is not ideal, but I am not sure how differently put this condition)
    
    # I  am starting the loop with my guess: X = N:

    guess = x 
    
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
print(f"The square root of {number} is approx. {result:.2f}.") # %:.2f is a function to print only 2 decimal places https://pythonguides.com/python-print-2-decimal-places/

    