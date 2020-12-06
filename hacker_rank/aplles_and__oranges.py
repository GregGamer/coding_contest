"""
7 11
5 15
3 2
-2 2 1
5 -6
"""

if __name__ == "__main__":
    s,t = map(int, input().split())
    a,b = map(int, input().split())
    m,n = map(int, input().split())
    apples = list(map(int, input().split()))
    oranges = list(map(int, input().split()))

    print(len([x for x in apples if x + a in range(s,t+1)]))
    print(len([x for x in oranges if x + b in range(s,t+1)]))
    