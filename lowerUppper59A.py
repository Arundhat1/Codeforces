#59A
def lowerUpper():
    s = input()
    lower = 0
    upper = 0
    for cha in s:
        if ord(cha) in range(97,123):
            lower += 1
        elif ord(cha) in range(65,91):
            upper += 1
    if lower >=  upper :
        return s.lower()
    elif upper >lower:
        return s.upper()
