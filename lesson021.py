my_list = [1,2,3]
print(type(my_list))
print(hex(id(my_list)))
my_list.append(4)
print(my_list)
print(hex(id(my_list)))
print('-'*80)

my_list_1 = [1,2,3]
print(hex(id(my_list_1)))

my_list_1 = my_list_1 + [4]
print(hex(id(my_list_1)))
print('-'*80)

my_dict = dict(key1=1, key2='a')
print(my_dict)
print(hex(id(my_dict)))
my_dict['key3'] = 10.5
print(hex(id(my_dict)))
print('-'*80)

t = (1, 2, 3)
print(hex(id(t)))
print(t[0])
print(hex(id(t[0])))
print(t[1])
print(hex(id(t[1])))
print(t[2])
print(hex(id(t[2])))
print('-'*80)

t = ([1,2], [3,4])
print(hex(id(t)))
print(t[0])
print(hex(id(t[0])))
print()
t[0].append(3)
print(t)
print(hex(id(t)))
print(t[0])
print(hex(id(t[0])))



