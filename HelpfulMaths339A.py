#339A
def HelpfulMaths():
    s = input()
    digits = list(s.split("+")).sort(key = int)
    return ("+").join(digits)

def WordCapitalisation():
    sen = input()
    return sen[0].upper() + sen[1 : ]
