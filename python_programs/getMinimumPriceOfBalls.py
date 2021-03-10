# was a chellange on Clash of Code
# shortest Mode
#
# Problem was to get the minimum Price of Balls
# where b is the amount of black balls wanted and w is the amount of white balls wanted
# x and y are the costs of black and white balls
# and z is the amount it would cost to transfer a ball from white to balck and vice versa
#
# example input: 1 3 5 7 9
# example input: 5 5 9 1 1

I=input
b,w,x,y,z=map(int,I().split())
I(b*((z+y<x)*(y+z) or x)+w*((z+x<y)*(x+z) or y))
