#32B
#def Broze():
def reverseusingrecursion(word):
    ans = ""
    if len(word) == 1:
        ans = ans + word
        return ans
    elif len(word) > 1:
        ans = word[-1] + reverseusingrecursion(word[ :-1])
        return ans
