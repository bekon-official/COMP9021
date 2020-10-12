# COMP9021 20T3 - Rachid Hamadi
# Quiz 3 *** Due Friday Week 5 @ 10.00pm

# DO *NOT* WRITE YOUR NAME TO MAINTAIN ANONYMITY FOR PLAGIARISM DETECTION

# Prompts the user for an arity (a natural number) n and a word.
# Call symbol a word consisting of nothing but alphabetic characters
# and underscores.
# Checks that the word is valid, in that it satisfies the following
# inductive definition:
# - a symbol, with spaces allowed at both ends, is a valid word;
# - a word of the form s(w_1,...,w_n) with s denoting a symbol and
#   w_1, ..., w_n denoting valid words, with spaces allowed at both ends and
#   around parentheses and commas, is a valid word.


import sys
from time import sleep

def is_valid(word, arity):
    return False
    # REPLACE THE RETURN STATEMENT ABOVE WITH YOUR CODE

try:
    arity = int(input('Input an arity : '))
    if arity < 0:
        raise ValueError
except ValueError:
    print('Incorrect arity, giving up...')
    sys.exit()
sleep(0.001)
word = input('Input a word: ')
sleep(0.001)
word=word.replace(' ','')
word=list(word)
#check whether it have illegal symbol
def only_have_word(series):
    for s in series:
        if s.isalpha()==False and s!="(" and s!=")" and s!="_" and s!=",":
            return False
    return True
#check the special case:the function only have a pair of ()
def check_first(st,arity):
    for i in range(0,len(st)):
        if st[i]=="," :
            if st[i+1]=="," or st[i+1]=="(" or st[i+1]==")":
                return False
    if st.count(",")+1==arity:
        #print("?")
        return True
    else:
        #print(str(9)+'tunnel') 
        return False
    
def is_valid(st,arity):
    check=0
    i=0
    #check if it have a function name before "(" or ")"
    if st[0]==")" or st[0]=="(":
        return False
    # those two line check whether it is special case
    if st.count("(")==1 and st.count(")")==1:
        return check_first(st,arity)
    while i in range(0,len(st)):
        if st.count("(")==1 and st.count(")")==1:
            return check_first(st,arity)
    # if we found a ")" get its cloest "("
        elif st[i]==")":
            #print("?")
            check+=1
            lower=i
            try:
                while st[lower]!="(":
                    lower-=1
            except IndexError:
                return False
    # it would always be special case
            if check_first(st[lower-1:i],arity)==False:
                return False
            #print(lower,i)
    # change things inside () to be "t"
            for j in range(lower,i+1):
                st[j]="t"
            i=lower-1
        elif st[i]==",":
            if st[i+1]=="," or st[i+1]=="(" or st[i+1]==")":
                return False
            else:
                check+=1
                i+=1
        else:
            #print("?2")
            i+=1
        # those two line check whether it is special case
    #print(check)
    #print(st)
   # those two line check whether it is special case
    if st.count("(")==1 and st.count(")")==1:
        return check_first(st,arity)
    if check==arity:
        return True
    else:
        #print(str(3)+'tunnel') 
        return False
if(only_have_word(word))==False:
    print('The word is invalid.')
else:
    if is_valid(word,arity):
        print('The word is valid.')
    else:
        print('The word is invalid.')



