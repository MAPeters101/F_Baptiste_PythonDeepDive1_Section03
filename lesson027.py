a = 'hello'
b = "hello"
print(hex(id(a)))
print(hex(id(b)))
print(a is b)
print()

a = 'hello world'
b = "hello world"
print(hex(id(a)))
print(hex(id(b)))
print(a is b)
print()

a = '_this_is_a_long_string_that_could_be_used_as_an_identifier'
b = '_this_is_a_long_string_that_could_be_used_as_an_identifier'
print(hex(id(a)))
print(hex(id(b)))
print(a is b)
print()

a = ' this is a long string that could be used as an identifier'
b = ' this is a long string that could be used as an identifier'
print(hex(id(a)))
print(hex(id(b)))
print(a is b)
print()


print('-'*80)



