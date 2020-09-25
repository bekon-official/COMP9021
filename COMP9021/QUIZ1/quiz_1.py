# COMP9021 20T3 - Rachid Hamadi
# Quiz 1 *** Due Friday Week 3 @ 10.00pm

# DO *NOT* WRITE YOUR NAME TO MAINTAIN ANONYMITY FOR PLAGIARISM DETECTION

import sys
from random import seed, randrange
from pprint import pprint
try:
    arg_for_seed, upper_bound = (abs(int(x)) + 1 for x in input('Enter two integers: ').split())
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
mapping = {}
for i in range(1, upper_bound):
    r = randrange(-upper_bound // 8, upper_bound)
    if r > 0:
        mapping[i] = r
print('\nThe generated mapping is:')
print('  ', mapping)
# sorted() can take as argument a list, a dictionary, a set...
keys = sorted(mapping.keys())
print('\nThe keys are, from smallest to largest: ')
print('  ', keys)

cycles = []
reversed_dict_per_length = {}

# INSERT YOUR CODE HERE
#CYCLES
cycles_temp=[]
target_temp=[]
temp_mapping=mapping
#wirte the key which is verified 
number_isverified=[]
for key,value in temp_mapping.items():
    #Iteration the dictionary
    # add first key and its value
    target_temp.append(key) 
    temp_value=value
    # if they are equal add it directly
    if key==value:
        target_temp=[key]
        cycles_temp.append(target_temp)
    elif key in number_isverified:
        target_temp=[]
        continue
    else:
        #Iteration until we get a repete number
        while temp_value not in target_temp and temp_value not in number_isverified:
            target_temp.append(temp_value)
            try:
                temp_value=temp_mapping[temp_value]
        #if we do not get a cycle,this attempt is fail
            except KeyError:
                break 
        #after exiting the while function if we found temp is the first key we try
        if temp_value==key:
                for i in range (0,len(target_temp)):
                    number_isverified.append(target_temp[i])
                cycles_temp.append(target_temp)
    target_temp=[]

# choose the distinct list
for elem in cycles_temp:
    if elem not in cycles:
        cycles.append(elem)

#REVERSED DICTIONARY
temp_dict={}
#get the original key into  list with origin value as the new key
for key,value in temp_mapping.items():
    if value not in temp_dict:
        temp_dict[value]=[key]
    else:
        temp_dict[value].append(key)
#sort it into a new dict by len of value list
for key,value in temp_dict.items():
    if len(value) not in reversed_dict_per_length:
        reversed_dict_per_length[len(value)]={key:value}
    else:
        reversed_dict_per_length[len(value)][key]=value


print('\nProperly ordered, the cycles given by the mapping are: ')
print('  ', cycles)
print('\nThe (triply ordered) reversed dictionary per lengths is: ')
pprint(reversed_dict_per_length)

