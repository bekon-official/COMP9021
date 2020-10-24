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
base_8_number=base_8_number[::-1]
move_dict={
    0: (0, 1), 1: (1, 1), 2: (1, 0), 3: (1, -1),
              4: (0, -1), 5: (-1, -1), 6: (-1, 0), 7: (-1, 1)
}
move_x=0
move_y=0
location_list=[(0,0)]
for i in base_8_number:
    i=int(i)
    move_x+=move_dict[i][0]
    move_y+=move_dict[i][1]
    if (move_x,move_y) in location_list:
        location_list.remove((move_x,move_y))
    else:
        location_list.append((move_x,move_y))
#print(location_list)
boundary_left=sorted(location_list)[0][0]
boundary_right=sorted(location_list)[-1][0]
boundary_upper=sorted(location_list,key=lambda u:u[1])[-1][1]
boundary_down=sorted(location_list,key=lambda u:u[1])[0][1]
'''print(boundary_left)
print(boundary_right)
print(boundary_upper)
print(boundary_down)
print(location_list)'''
for i in range(boundary_upper,boundary_down-1,-1):
    for j in range(boundary_left,boundary_right+1):
        if (j,i) in location_list:
            print(on,end="")
        else:
            print(off,end="")
    print()
