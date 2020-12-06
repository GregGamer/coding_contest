"""
5 3
10 2 5
7 1 0
9 9 9
1 23 12
6 5 9
1
"""

n,m = map(int, input().split())
athlets = [input().split() for _ in range(n)]
k = int(input())

print(athlets.sort(key=lambda x: int(x[k])))
# print("\n".join(sorted(athlets, key=lambda x: x[k-1])))

