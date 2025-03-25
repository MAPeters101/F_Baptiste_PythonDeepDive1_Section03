import sys
a = [1,2,3]
print(id(a))
print(sys.getrefcount(a))
print('-'*80)

import ctypes
def ref_count(address: int):
    return ctypes.c_long.from_address(address).value

print(ref_count(id(a)))
print(ctypes.c_long.from_address(id(a)).value)
print('-'*80)

b = a
print(hex(id(a)))
print(hex(id(b)))
print(ref_count(id(a)))

c = a
print(ref_count(id(a)))

c = 10
print(ref_count(id(a)))

b = None
print(hex(id(b)))
print(ref_count(id(a)))
print('-'*80)

a_id = id(a)
a = None
print(ref_count(a_id))



