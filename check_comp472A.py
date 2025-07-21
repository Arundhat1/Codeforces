#472A
def check_comp(s):
    x = 2
    comp ='False'
    while x < s:
        if (s % x) == 0:
                comp = 'True'
        else:
                x = x + 1

    return comp
def Composit_add():
    n = int(input())
    for num in range(2,n):
        num1 = num
        num2 = (n - num)
        if check_comp(num1) == 'True' and check_comp(num2) == 'True':
            print(num1 , num2)
            break
