a = {100: ['max', 'mustermann', 3100]}, {101:["lisa","wimmer",3305]}
b = (1.0, 3, [4, "four"], {"one": 7.1}, (True, ))
c = "test"
d = (False)


print(a[-1][101])
print(len(a), isinstance(a, dict))

print(d, isinstance(d, bool))
print(c, isinstance(c,str))

print(len(b[2]))
print(b[-1][0], isinstance(b[-1],tuple))