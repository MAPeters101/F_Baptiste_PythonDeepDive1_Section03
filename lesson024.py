a = 10
b = 10
print(hex(id(a)))
print(hex(id(b)))
print("a is b:", a is b)
print("a == b:", a == b)
print()

a = 1000
b = 1000
print(hex(id(a)))
print(hex(id(b)))
print("a is b:", a is b)
print("a == b:", a == b)
print('-'*80)

a = [1,2,3]
b = [1,2,3]
print(hex(id(a)))
print(hex(id(b)))
print("a is b:", a is b)
print("a == b:", a == b)
print('='*80)

a = 10
b = 10.0
print(hex(id(a)))
print(hex(id(b)))
print("a is b:", a is b)
print("a == b:", a == b)
print('-'*80)

a = 10 + 0j
b = 10.0
print(hex(id(a)))
print(hex(id(b)))
print("a is b:", a is b)
print("a == b:", a == b)
print('-'*80)

print(hex(id(None)))
a = None
b = None
c = None
print(hex(id(a)))
print(hex(id(b)))
print(hex(id(c)))
print("a is b:", a is b)
print("a is c:", a is c)
print("a is None:", a is None)
print("b is None:", b is None)
print("c is None:", c is None)
print("a == b:", a == b)
print("a == c:", a == c)
print('-'*80)







