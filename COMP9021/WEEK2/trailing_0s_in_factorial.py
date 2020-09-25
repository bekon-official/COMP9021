# Prompts the user to input an integer N at least equal to 10 and computes N!
# in three different ways.


import sys
from math import factorial
import time

# Insert your code here
def first_computation(x):
     nb_of_trailing_0s = 0
     while (x%10)==0:
         x=x//10
         nb_of_trailing_0s+=1
     return nb_of_trailing_0s
def second_computation(x):
    i=1
    while x[-i]=='0' and i<len(x):
        i=i+1
    return i-1
def third_computation(x):
    nb_of_trailing_0s=0
    factor_calculate_now=x
    temp=factor_calculate_now
    while factor_calculate_now>1:
        if temp%5==0:
            temp=temp//5
            nb_of_trailing_0s+=1
        else:
            factor_calculate_now-=1
            temp=factor_calculate_now
    return nb_of_trailing_0s


try:
    the_input = int(input('Input a nonnegative integer: '))
    if the_input < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

# time.sleep( 0.1 ) I use this to debug
the_input_factorial = factorial(the_input)


print(f'Computing the number of trailing 0s in {the_input}! by dividing by 10 for long enough:',
first_computation(the_input_factorial))


print(f'Computing the number of trailing 0s in {the_input}! by converting it into a string:',
second_computation(str(the_input_factorial)))

    
print(f'Computing the number of trailing 0s in {the_input}! the smart way:',
third_computation(the_input))
