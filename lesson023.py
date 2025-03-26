
a = "hello"
b = a
print(hex(id(a)))
print(hex(id(b)))

a = "hello"
b = "hello"
print(hex(id(a)))
print(hex(id(b)))
print()

b = "hello world"
print(hex(id(a)))
print(hex(id(b)))
print('-'*80)

a = [1,2,3]
b = a
print(hex(id(a)))
print(hex(id(b)))
print()

b.append(100)
print(hex(id(a)))
print(hex(id(b)))
print(a)
print(b)
print()
print('-'*80)





