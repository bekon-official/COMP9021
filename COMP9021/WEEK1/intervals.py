from random import seed, randrange
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
L = [randrange(0, 20) for _ in range(nb_of_elements)]
# Prints out the list.
print('\nThe list is:', L)
print()
stock_number=[0]*4
for e in L:
    if(e<5):
        stock_number[0]+=1
    elif(e<10):
        stock_number[1]+=1
    elif(e<15):
        stock_number[2]+=1
    else:
        stock_number[3]+=1
for i in range(4):
    if stock_number[i] == 0:
        print('There is no element between '+str(5*i)+' and '+str(5*i+4)+'.')
    elif stock_number[i]==1:
        print('There is 1 element between '+str(5*i)+' and '+str(5*i+4)+'.')
    else :
        print('There are '+str(stock_number[i])+' elements between '+str(5*i)+' and '+str(5*i+4)+'.')


# Insert your code here
