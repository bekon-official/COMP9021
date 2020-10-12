# Prompts the user for a number N and prints out the first N + 1 lines of Pascal triangle.



# Insert you code here            
while True:
    try:
        N = int(input('Enter a natural number: '))
        if N < 0:
            raise ValueError
        break
    except ValueError:
        print('Incorrect input, try again')

pascal_triangle = [[1] * (n + 1) for n in range(N + 1)]
for n in range(2, N + 1):
    for i in range(1,n):
        pascal_triangle[n][i]=pascal_triangle[n-1][i-1]+pascal_triangle[n-1][i]
    # Insert your code to compute Pascal triangle
    #pascal_triangle[n]=
width = len(str(pascal_triangle[N][N // 2]))
space=" "*width
for n in range(0, N + 1):
    #for i in range(0,len(pascal_triangle[n])):
    for i in range(0,len(pascal_triangle[n])):
        pascal_triangle[n][i]=str(pascal_triangle[n][i]).rjust(width)
    #print(type(pascal_triangle[n][0]))
    pascal_triangle[n]=space.join(pascal_triangle[n])
longest=len(pascal_triangle[N])
for n in range(0, N + 1):
    print(pascal_triangle[n].center(longest).rstrip())


# Insert your code to display Pascal triangle
