# Prompts the user for a string w of lowercase letters and outputs the
# longest sequence of consecutive letters that occur in w,
# but with possibly other letters in between, starting as close
# as possible to the beginning of w.


import sys
word = input('Please input a string of lowercase letters: ')
if not all(c.islower() for c in word):
    print('Incorrect input.')
    sys.exit()
def check_exists(current_start,word):
    for i in range(current_start+1,len(word)):
        if word[current_start]+1==word[i]:
            return i
    return False
word = [ord(c) for c in word]

longest_length = 0
start = 0
current_start = 0
current_end=0
current_long=1
while current_end < len(word):
    if check_exists(current_end,word):
        #print(str(current_end)+"@")
        current_end=check_exists(current_end,word)
        current_long+=1
    else:
        #print(current_long)
        #print("%")
        if longest_length<current_long:
            longest_length=current_long
            start=current_start
        current_end+=1
        current_start=current_end
        current_long=1
if longest_length<current_long:
            longest_length=current_long
            start=current_start

#print(start)
#print(longest_length)

    # Replace pass above with your code
print('The solution is:', ''.join(chr(word[start] + i)
                                      for i in range(longest_length) ))
