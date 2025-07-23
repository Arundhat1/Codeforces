#791A
def bigBear():
    (Limak ,Bob) = map(int , list(input().strip()))
    year = 0
    while Limak == Bob or Limak < Bob:
        Limak *= 3
        Bob = Bob * 2
        year = year + 1
    print(year)
