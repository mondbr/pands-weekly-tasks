# squareroot.py
# program that takes a positive floating-point number as input and outputs an approximation of its square root.
# this program does not to use the built in functions
# author: Monika Dabrowska
# TBC

# Newton method 'better  =   1 / 2  *  ( approx  +  n / approx )'


def newtonSqrt(n):
    approx = 0.5 * n
    better = 0.5 * (approx + n/approx)

    while better != approx:
        approx = better
        better = 0.5 * (approx + n/approx)
        return approx
while True:
    n=float(input("Please enter a positive number"))

print(newtonSqrt(n))
        
    
