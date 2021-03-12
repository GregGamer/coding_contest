#print(*sorted(list(map(int,input().split()))))
import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

a = int(input())
b = int(input())
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
c = (a**2+b**2)**0.5
print(c)
if c.is_integer():
    print(int(c))
    exit()

print("IMPOSSIBLE")
