
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



