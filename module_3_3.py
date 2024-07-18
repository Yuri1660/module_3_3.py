def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()

print_params(b = 25)
print_params(c = [1,2,3])

values_list = [2, 'Ivan', False]

values_dict = {'a': 5, 'b': 'Иван' , 'c': 10.15}

print_params(*values_list)
print_params(**values_dict)

values_list2 = ['Anton', 50.33]

print_params(*values_list2, 42)