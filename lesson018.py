import ctypes
import gc

def ref_count(address):
    return ctypes.c_long.from_address(address).value

def object_by_id(object_id):
    #print(gc.get_objects())
    for obj in gc.get_objects():
        #print(obj, hex(id(obj)), hex(object_id))
        if id(obj) == object_id:
            return "Object exists"
    return "Not Found"

class A:
    def __init__(self):
        self.b = B(self)
        print('A: self: {0}, b: {1}'.format(hex(id(self)), hex(id(self.b))))

class B:
    def __init__(self, a):
        self.a = a
        print('B: self: {0}, a: {1}'.format(hex(id(self)), hex(id(self.a))))

gc.disable()
my_var = A()
print(hex(id(my_var)))
print(hex(id(my_var.b)))
print(hex(id(my_var.b.a)))
print('-'*80)

a_id = id(my_var)
b_id = id(my_var.b)
print(hex(a_id))
print(hex(b_id))
print('-'*80)

print(ref_count(a_id))
print(ref_count(b_id))
print(object_by_id(a_id))
print(object_by_id(b_id))
print('-'*80)

my_var = None
print(ref_count(a_id))
print(ref_count(b_id))
print(object_by_id(a_id))
print(object_by_id(b_id))
print('-'*80)

gc.collect()
print(object_by_id(a_id))
print(object_by_id(b_id))
print(ref_count(a_id))
print(ref_count(b_id))
from time import sleep
sleep(2)
print(ref_count(a_id))
print(ref_count(b_id))
sleep(2)
print(ref_count(a_id))
print(ref_count(b_id))
print('-'*80)







