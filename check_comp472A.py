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
