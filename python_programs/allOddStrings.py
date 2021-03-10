from functools import reduce

def allOddStrings(l):
    return bool(reduce(lambda x,y: x%2 and y%2, map(lambda x: len(x),l)))

l = ["carrots","potatos","apple"]

print(allOddStrings(l))
