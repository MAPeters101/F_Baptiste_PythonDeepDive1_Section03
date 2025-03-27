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

import sys
a = sys.intern('hello world')
b = sys.intern('hello world')
c = 'hello world'
print(hex(id(a)))
print(hex(id(b)))
print(hex(id(c)))
print(a is b)
print(a == b)
print(a is c)
print(a == c)
print('-'*80)

def compare_using_equals(n):
    a = 'a long string that is not interned' * 200
    b = 'a long string that is not interned' * 200
    print(hex(id(a)))
    print(hex(id(b)))
    print(a is b)
    for i in range(n):
        if a == b:
            pass

def compare_using_interning(n):
    a = sys.intern('a long string that is not interned' * 200)
    b = sys.intern('a long string that is not interned' * 200)
    print(hex(id(a)))
    print(hex(id(b)))
    print(a is b)
    for i in range(n):
        if a is b:
            pass

import time
start = time.perf_counter()
compare_using_equals(10000000)
end = time.perf_counter()
print('equality', end-start)

start = time.perf_counter()
compare_using_interning(10000000)
end = time.perf_counter()
print('equality', end-start)



