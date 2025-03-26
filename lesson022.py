
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

