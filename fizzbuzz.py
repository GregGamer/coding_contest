'''just fiizbuzz'''
print("\n".join([(i%3==0)*"Fizz"+(i%5==0)*"Buzz"or str(i) for i in range(1,101)]))
