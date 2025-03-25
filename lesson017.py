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


