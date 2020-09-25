# Decodes all multiplications of the form
#
#                        *  *  *
#                   x       *  *
#                     ----------
#                     *  *  *  *
#                     *  *  *
#                     ----------
#                     *  *  *  *
#
# such that the sum of all digits in all 4 columns is constant.


# Insert your code here.
def getSum(num):
    if num // 10 == 0:
        return num
    return num % 10 + getSum(num // 10)
def get_two_number(number):
    print("A solution with all columns adding up to {}:".format(number))
    for x in range(100, 1000):
        for y in range(10, 100):
            first_line=x * (y % 10)
            second_line=10 * x * (y//10)
            if x%10+y%10+2*(first_line%10) == int(number):
                if x//10-10*(x//100)+y//10+2*(first_line//10)-20*(first_line//100)+2*(second_line//10)-20*(second_line//100)==number:
                    if x//100+2*(first_line//100)-20*(first_line//1000)+2*(second_line//100)-20*(second_line//1000)==number:
                        if 2*(first_line//1000+second_line//1000)==number:
                            return x,y
            else:
                continue



def display(x,y):
    newx=" ".join(str(x))
    print(newx.rjust(12," "))
    newy=" ".join(str(y))
    print("     x"+newy.rjust(6," "))
    print("     -------")
    first_mul=x * (y % 10)
    second_mul=x*(y//10)
    sum=first_mul+10*second_mul
    newfm=" ".join(str(first_mul))
    print(newfm.rjust(12," "))
    newsm=" ".join(str(second_mul))
    print(newsm.rjust(10," "))
    print("     -------")
    newsum=" ".join(str(sum))
    print(newsum.rjust(12," "))

display(*get_two_number(10))
print()
display(*get_two_number(18))
