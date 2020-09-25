import sys


try:
    N = int(input('Input an integer: '))
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

for i in range(2, N + 1):
    sum=0
    divisor=1
    while divisor<i:
        if i%divisor==0:
            sum=sum+divisor 
        divisor+=1
    if sum==i:
        print(str(i)+' is a perfect number.')
    sum=0
    # Replace pass above with your code to check whether i is perfect,
    # and print out that it is in case it is.
    # 1 divides i, so counts for one divisor.
    # It is enough to look at 2, ..., i // 2 as other potential divisors.


