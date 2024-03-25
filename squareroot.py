# squareroot.py
# program that takes a positive floating-point number as input and outputs an approximation of its square root.
# this program does not to use the built in functions
# author: Monika Dabrowska
# TBC

# Newton method 'better  =   1 / 2  *  ( approx  +  n / approx )'


def sqrt(number):

    approx = 0.5 * number
    more_accurate = 0.5 * (approx + number/approx)



    while better != approx:
        approx = better
        better = 0.5 * (approx + n/approx)
        return approx
while True:
    n=float(input("Please enter a positive number"))

    print(newtonSqrt(n))
'''
number = float(input("Enter a positive number: "))  
approx
'''
