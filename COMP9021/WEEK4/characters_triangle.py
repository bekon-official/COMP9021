# Prompts the user for a strictly positive number N
# and outputs an equilateral triangle of height N.
# The top of the triangle (line 1) is labeled with the letter A.
# For all nonzero p < N, line p+1 of the triangle is labeled
# with letters that go up in alphabetical order modulo 26
# from the beginning of the line to the middle of the line,
# starting wth the letter that comes next in alphabetical order
# modulo 26 to the letter in the middle of line p,
# and then down in alphabetical order modulo 26
# from the middle of the line to the end of the line.


# Insert your code here
#print(ord("Z"))
while True:
    try:
        height = int(input('Enter a strictly positive integer: '))
        if height <= 0:
            raise ValueError
        break
    except ValueError:
        print('Incorrect input, try again.')
middle_code = ord('A')-1
end_code = middle_code
train=[]
for i in range(1, height+1):
    j=0
    while j<i:
        j+=1
        middle_code+=1
        end_code+=1
        if middle_code==91:
            middle_code=65
            end_code=65
        train.append(chr(middle_code))
    while j>1:
        end_code-=1
        if end_code==64:
            end_code=90
        train.append(chr(end_code))
        j-=1
    end_code=middle_code
    print(" "*(height-i)+str("".join(train)))
    train=[]  
    

