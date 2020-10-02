# Finds all sequences of consecutive prime 5-digit numbers,
# say (a, b, c, d, e, f), such that
# b = a + 2, c = b + 4, d = c + 6, e = d + 8, and f = e + 10.
from math import sqrt
from itertools import chain

# Insert your code here

def sieve_of_primes_up_to(n):
    primes_sieve = [True] * (n + 1)
    for p in range(2, round(sqrt(n)) + 1):
        if primes_sieve[p]:
            for i in range(p * p, n + 1, p):
                primes_sieve[i] = False
    return primes_sieve
primes=sieve_of_primes_up_to(99999)
def is_prime(n,i):
    if primes[n]==False:
        return False
    for k in range (1,i):
        if primes[n+k]==True:
            return False 
    else:
        return True
print('The solutions are:\n')
solutions=[]
condition=False
for number in range(10000,99969):
    if primes[number+30]==False:
            condition=True
    mid_number=number
    for i in range(2,12,2):
        if is_prime(mid_number,i)==False:
            condition=True
        mid_number=mid_number+i
    if condition==False:
        solutions.append(number)
    condition=False
for solution in solutions:
    mid_number=solution
    mid=[]
    count=0
    for i in range(2,14,2):
        mid.append(mid_number)
        mid_number=mid_number+i
    for e in mid:
        print(e, end='')
        count += 1
        if count% 6!=0:
            print(end=" ")
        else:
            print()


# Write a loop that generates all odd numbers a between 10_000 and 99_999 and tests whether
# for all i = 0, 2, 4, ..., 30, i is in good_leaps iff a + i is prime.
