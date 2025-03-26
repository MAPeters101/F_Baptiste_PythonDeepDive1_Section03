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




