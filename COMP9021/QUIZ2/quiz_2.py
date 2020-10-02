# COMP9021 20T3 - Rachid Hamadi
# Quiz 2 *** Due Friday Week 4 @ 10.00pm

# DO *NOT* WRITE YOUR NAME TO MAINTAIN ANONYMITY FOR PLAGIARISM DETECTION


# Reading the number written in base 8 from right to left,
# keeping the leading 0's, if any:
# 0: move N     1: move NE    2: move E     3: move SE
# 4: move S     5: move SW    6: move W     7: move NW
#
# We start from a position that is the unique position
# where the switch is on.
#
# Moving to a position switches on to off, off to on there.

import sys
from time import sleep
on = '\u26aa'
off = '\u26ab'
code = input('Enter a non-strictly negative integer: ').strip()
sleep(0.01)
try:
    if code[0] == '-':
        raise ValueError
    int(code)
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
nb_of_leading_zeroes = 0
for i in range(len(code) - 1):
    if code[i] == '0':
        nb_of_leading_zeroes += 1
    else:
        break
print("Keeping leading 0's, if any, in base 8,", code, 'reads as',
      '0' * nb_of_leading_zeroes + f'{int(code):o}.'
     )
print()
# INSERT YOUR CODE HERE
base_8_number=str('0' * nb_of_leading_zeroes) + str(f'{int(code):o}')
#switch method
def switch(a,b):
    if (a,b) in list_of_switch[0]:
        list_of_switch[0].remove((a,b))
        list_of_switch[1].append((a,b))
    elif (a,b) in list_of_switch[1]:
        list_of_switch[0].remove((a,b))
        list_of_switch[1].append((a,b))
    else:
        list_of_switch[0].append((a,b))
# set a list, assume map[0] contain true point,map[1] contain false
list_of_switch=[[],[]]
list_of_switch[0].append((0,0))
a=0
b=0
#set a cursor to scan the number from right to left
cursor=len(base_8_number)-1
while(cursor>=0):
    if base_8_number[cursor]=='0':
        a+=1
    elif base_8_number[cursor]=='1':
        a+=1
        b-=1
    elif base_8_number[cursor]=='2':
        b=b-1
    elif base_8_number[cursor]=='3':
        a-=1
        b-=1     
    elif base_8_number[cursor]=='4':
        a-=1
    elif base_8_number[cursor]=='5':
        a-=1
        b+=1
    elif base_8_number[cursor]=='6':
        b+=1
    else:
        a+=1
        b+=1
    switch(a,b)
    cursor=cursor-1
#print(list_of_switch)
#get the border that we what to print(all the line that contain True)
max_width_left=-100
max_width_right=100
max_length_up=-100
max_length_down=100
for i in list_of_switch[0]:
    if(i[1]>max_width_left):
        max_width_left=i[1]
    if(i[1]<max_width_right):
        max_width_right=i[1]
    if(i[0]>max_length_up):
        max_length_up=i[0]
    if(i[0]<max_length_down):
        max_length_down=i[0]
#print(max_width_left,max_width_right,max_length_up
#,max_length_down)
target_column=max_width_left
target_line=max_length_up
#print from left to right, up to down
while target_line>=max_length_down:
    if target_column>=max_width_right:
        if (target_line,target_column) in list_of_switch[0]:
            print(on,end="")
            target_column-=1
        else:
            print(off,end="")
            target_column-=1
    else:
        print()
        target_column=max_width_left
        target_line-=1        

