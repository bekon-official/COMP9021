# Finds all triples of positive integers (i, j, k) such that
# i, j and k are two digit numbers, i < j < k,
# every digit occurs at most once in i, j and k,
# and the product of i, j and k is a 6-digit number
# consisting precisely of the digits that occur in i, j and k.
for i in range(10, 100):
    i_digits = {i // 10, i % 10}
    if len(i_digits)==1:
        continue
    for j in range(10, 100):
        if(j // 10 in i_digits or j % 10 in i_digits or j // 10==j % 10 or j<i):
            continue
        else:
            i_and_j_digits = i_digits.union((j // 10, j % 10))
            for k in range(10,100):
                if(k // 10 in i_and_j_digits or k % 10 in i_and_j_digits or k // 10==k % 10 or k<j):
                    continue
                else:
                    ijk=i*j*k
                    ijk_digits=set()
                    i_and_j_and_k_digits =i_and_j_digits.union((k // 10, k % 10))
                    for ij in str(ijk):
                        ijk_digits.add(int(ij))
                    if(ijk_digits==i_and_j_and_k_digits):
                        print(str(i)+" x "+str(j)+" x "+str(k)+" = "+str(ijk)+" is a solution.")
                    ijk_digits.clear()
                        

    
# Insert your code here
