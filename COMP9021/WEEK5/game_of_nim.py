from functools import reduce
from itertools import cycle
from operator import xor
from random import choice, randrange, seed
from time import sleep
import sys

# POSSIBLY DEFINE FUNCTIONS HERE

try:
    piles = [int(n) for n in input('Describe the piles: ').split()]
    if any(n < 0 for n in piles):
        raise ValueError
except ValueError:
    print('Incorrect description, giving up!')
sleep(0.01)
def display_map(piles):
    right_side=len(piles)-1
    for i in range(max(piles),0,-1):
        for j in range(0,len(piles)):
            if piles[j]>=i and j==len(piles)-1:
                print("_")
            elif piles[j]<i and j==len(piles)-1:
                print(" ")
            elif piles[j]>=i:
                print("_  ",end="")
            else:
                print("   ",end="")
def smart_move(piles,no_empty_location):
    the_nim_sum=nim_sum(piles)
    leftmost_1 = 1 << the_nim_sum.bit_length() - 1
    for location in no_empty_location:
        if leftmost_1 & piles[location]:
            update_file(piles, no_empty_location, location,
                         piles[location] ^ the_nim_sum
                        )
            break
def nim_sum(piles):
    return reduce(xor, piles)
def random_move(piles,no_empty_location):
    location=choice(no_empty_location)
    step=randrange(piles[location])
    update_file(piles,no_empty_location,location,step)
def update_file(files,no_empty_location,location,number):
    files[location]=number
    if number==0:
        no_empty_location.remove(location)

def change_to_binary(binary):
    binary_piles=list(binary)
    for i in range(0,len(binary_piles)):
        binary_piles[i]=str(bin(binary_piles[i]))
    length=max(len(j)-2 for j in binary_piles)
    for i in range(0,len(binary_piles)):
        binary_piles[i]=binary_piles[i][2:].rjust(length,'0')
    return binary_piles
def calculate_nim_sum(piles):
    result=""
    for i in range(0,len(str(piles[0]))):
        count=0
        for p in piles:
            p=str(p)
            if p[i]=="1":
                count+=1
        if count%2==0:
            result=result+"0"
        else:
            result=result+"1"
        count=0
    if int(result)==0:
        return 0
    else:
        return result


players=["First","Second"]
binary=change_to_binary(piles)
if nim_sum(piles):
    winner=players[0]
else:
    winner=players[1]
print(f'\n{winner} player will play smart and win!')
try:
    seed(int(input('Feed seed if desired: ')))
except ValueError:
    pass
sleep(0.01)
print('\nGame to be played:')
display_map(piles)
no_empty_location=[]
for i in range(0,len(piles)):
    if piles[i]!=0:
        no_empty_location.append(i)
players_turns = cycle(players)
while no_empty_location:
    player=next(players_turns)
    if player == winner:
        print(f'\n{player} player making smart move:')
        smart_move(piles, no_empty_location)
    else:
        print(f'\n{player} player making random move:')
        random_move(piles, no_empty_location)
    display_map(piles)


    



# INSERT YOUR CODE HERE
