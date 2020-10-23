'''
Implements a function encode(a, b) and a function decode(n) for the one-to-one mapping
from the set of pairs of integers onto the set of natural numbers described as follows:

                      16  15  14  13  12
                      17  4   3   2   11
                      18  5   0   1   10
                      19  6   7   8   9
                      20  21  ...

That is, starting from the point (0,0) of the plane, we move to (1,0)
and then spiral counterclockwise.
'''

from math import sqrt


def encode(a,b):
    c=max(a,b,-a,-b)
    if a==c and b!=-c:
        return (2*c-1)*(2*c-1)+b+c-1
    elif b==c:
        return (2*c-1)*(2*c-1)+2*c-1+(c-a)
    elif -a==c:
        return (2*c-1)*(2*c-1)+4*c-1-b+c
    else:
        return (2*c+1)*(2*c+1)-(c+1-a)
    # Replace pass above with your code
def decode(n):
    c=0
    while n>(2*c-1)*(2*c-1):
        c=c+1
    if c>0:
        c=c-1
    if n>=(2*c-1)*(2*c-1) and ((2*c-1)*(2*c-1)+2*c-1)>=n:
        return (c,-c+1+n-(2*c-1)*(2*c-1))
    elif n>((2*c-1)*(2*c-1)+2*c-1) and n<=((2*c-1)*(2*c-1)+4*c-1):
        return (c-n+(2*c-1)*(2*c-1)+2*c-1,c)
    elif n>((2*c-1)*(2*c-1)+4*c-1) and n<(2*c+1)*(2*c+1)-2*c:
        return (-c,(2*c+1)*(2*c+1)-3*c-n-1)
    else:
        return (c+1+n-(2*c+1)*(2*c+1),-c)
    # Replace pass above with your code
#print(encode(0,-3))
