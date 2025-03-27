a = 10
b = 10
print(hex(id(a)))
print(hex(id(b)))
print(a is b)
print()

a = -5
b = -5
print(hex(id(a)))
print(hex(id(b)))
print(a is b)
print()

a = 256
b = 256
print(hex(id(a)))
print(hex(id(b)))
print(a is b)
print()

a = 257
b = 257
print(hex(id(a)))
print(hex(id(b)))
print(a is b)
print('-'*80)

a = 10
b = int(10)
c = int('10')
d = int('1010', 2)
print(a)
print(b)
print(c)
print(d)
print(hex(int(a)))
print(hex(int(b)))
print(hex(int(c)))
print(hex(int(d)))

