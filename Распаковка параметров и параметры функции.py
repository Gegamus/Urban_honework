def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)
    print(a,c)
    print(a,b)

print_params()
print_params(b=25)
print_params(c=[1,2,3])


values_list = [1, "строка", True]
#values_dict = {'a': 1, 'b': 'строка', 'c': True}
res = print_params(*values_list)

values_list2 = ["one", 2]
print_params(*values_list2, 42)