from random import seed, randint
from math import sqrt
from statistics import mean, median, pstdev
from decimal import getcontext, Decimal

import sys
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
L = [randint(-50, 50) for _ in range(nb_of_elements)]
# Prints out the list.
print('\nThe list is:', L)
print()
sum=0
L.sort()
#calcuate the sum
for e in L:
    sum=sum+e
#calcuate the mean no function
meann=(sum/nb_of_elements)
print("The mean is "+str("%.2f"%meann)+".")
#calculate the median no function
if (len(L) % 2==1):
    mediann=L[int((len(L)-1)/2)]
else:
    mediann=(L[int(len(L)/2)]+L[int((len(L)/2)-1)])/2
print("The median is "+str("%.2f"%mediann)+".")
#calculate the standard deviation no function
variance_temp=0
for e in L:
    variance_temp = variance_temp+(e-meann)*(e-meann)
variance=variance_temp/nb_of_elements
standard_deviation=sqrt(variance)
print("The standard deviation is "+str("%.2f"%standard_deviation)+".")
print()


#try to use function
print('Confirming with functions from the statistics module:')
print("The mean is "+str("%.2f"%mean(L))+".")
print("The median is "+str("%.2f"%median(L))+".")
print("The standard deviation is "+str("%.2f"%pstdev(L))+".")

# Insert your code here
