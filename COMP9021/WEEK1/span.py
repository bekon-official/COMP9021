from random import seed, randint
import sys
#input a seed generator
try:
    ackno_for_seed = int(input('Input a seed for the random number generator: '))
except ValueError:
    print('This is not a integer,please try again')
    sys.exit() 
#input the number you need to generate
try:
    nb_of_elements = int(input('How many elements do you want to generate? '))
except ValueError:
    print('This is not a integer,please try again.')
    sys.exit()
if nb_of_elements <= 0:
    print('This is a negative number or zero,please try again.')
    sys.exit()
# seed for the number
seed(ackno_for_seed)
# use the randint fuction to get random number
L = [randint(0, 99) for _ in range(nb_of_elements)]
# Prints out the list.
print('\nThe list is:', L)
max_element = 0
min_element = 100
for e in L:
    if e > max_element:
        max_element = e
    if e < min_element:
        min_element = e
print("\nThe maximum difference between largest and smallest values in this list is:",max_element-min_element)
print('Confirming with builtin operations:', max(L)-min(L))
# Insert your code here
