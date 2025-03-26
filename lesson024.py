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
print('-'*80)

