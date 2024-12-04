# This is a simple calculation program
# created to demonstrate version control.
from libadd import *
from libmult import *
a = 13
b = 5
print(plus(a,b))
print(mult(a,b))
print(multx(a,b,2))

def mult(a, b):
    return a * b

print("Multiplication result:", mult(4, 7))
