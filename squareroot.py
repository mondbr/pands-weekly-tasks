# squareroot.py
# program that takes a positive floating-point number as input and outputs an approximation of its square root.
# this program does not to use the built in functions
# author: Monika Dabrowska
# TBC

# Newton method 'better  =   1 / 2  *  ( approx  +  n / approx )'

num=float(input("Please enter a positive number"))

def sqrt(num):

    guess = num / 2.0
    while True:
        new_guess = 0.5 * (guess + num / guess)
        
    
