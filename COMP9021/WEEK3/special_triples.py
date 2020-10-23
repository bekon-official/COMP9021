# Finds all triples of consecutive positive three-digit integers
# each of which is the sum of two squares.
def nb_of_consecutive_squares(n):
    count=0
    try:
        while(sums_of_two_squares[count+n-1]!=None):
            count+=1
    except:
        pass
    return count
    # Replace pass above with your code

# The largest number whose square is a 3-digit number.
max = 31
# For all n in [100, 999], if n is found to be of the form a^2 + b^2
# then sums_of_two_squares[n] will be set to (a, b).
# Note that there might be other decompositions of n into a sum of 2 squares;
# we just recall the first decomposition we find.
# Also note that we waste the 100 first elements of the array;
# we can afford it and this choice makes the program simpler.
sums_of_two_squares = [None] * 1_000
for a in range(0,max+1):
    for b in range(0,max+1):
        result=a*a+b*b
        if result>1000:
            continue
        if sums_of_two_squares[result-1]==None:
            sums_of_two_squares[result-1]=(a,b)
        else:
            if a<sums_of_two_squares[result-1][0]:
                sums_of_two_squares[result-1]=(a,b)
            else:
                if a==sums_of_two_squares[result-1][0] and b<sums_of_two_squares[result-1][1]:
                    sums_of_two_squares[result-1]=(a,b)
# Insert your code here so that sums_of_two_squares[n] = (a, b) for some a, b with a^2 + b^2 == n
# in case such a pair (a, b) indeed exists.

for n in range(100, 1_000):
    i = nb_of_consecutive_squares(n)
    if(i>=3):
        print(f'({n}, {n+1}, {n+2}) (equal to ({sums_of_two_squares[n-1][0]}^2+{sums_of_two_squares[n-1][1]}^2, {sums_of_two_squares[n][0]}^2+{sums_of_two_squares[n][1]}^2, {sums_of_two_squares[n+1][0]}^2+{sums_of_two_squares[n+1][1]}^2)) is a solution.')
    # Insert your code here to depending on i, either print a solution
    # or look for another potential solution.
# Insert you code here
