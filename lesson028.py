def my_func():
    a = 24 * 60
    b = (1, 2) * 5
    c = 'abc' * 3
    d = 'ab' * 11
    e = 'the quick brown fox' * 5
    f = ['a', 'b'] * 3

print(my_func.__code__.co_consts)
print('-'*80)

def my_func(e):
    if e in [1,2,3]:
        pass

print(my_func.__code__.co_consts)
print('-'*80)





