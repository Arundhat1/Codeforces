#61A
def Shapur():
    first = (input())
    second = input()
    third = ''
    for dig in range(len(first)):
        if first[dig] == second[dig]:
            third = third + '0'
        else:
            third = third + '1'
    return third
