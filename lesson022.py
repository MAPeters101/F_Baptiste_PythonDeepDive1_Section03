
def process(s):
    print('Initial s # = {0}'.format(hex(id(s))))
    s = s + ' world'
    print('Final s # = {0}'.format(hex(id(s))))

my_var = 'hello'
print('my_var # = {0}'.format(hex(id(my_var))))
process(my_var)
print('After function call: my_var # = {0}'.format(hex(id(my_var))))
print(my_var)
print('-'*80)

def modify_list(lst):
    print('Initial lst # = {0}'.format(hex(id(lst))))
    lst.append(100)
    print('Final lst # = {0}'.format(hex(id(lst))))

my_list = [1,2,3]
print('my_list # = {0}'.format(hex(id(my_list))))
modify_list(my_list)
print('After function call: my_list # = {0}'.format(hex(id(my_list))))
print(my_list)
print('-'*80)

def modify_tuple(t):
    print('Initial t # = {0}'.format(hex(id(t))))
    t[0].append(100)
    print('Final lst # = {0}'.format(hex(id(t))))

my_tuple = ([1,2], 'a')
print('my_tuple # = {0}'.format(hex(id(my_tuple))))
modify_tuple(my_tuple)
print('After function call: my_tuple # = {0}'.format(hex(id(my_tuple))))
print(my_tuple)




