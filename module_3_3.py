def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print("Часть 1:")
print_params()
print_params(b=25)
print_params(c=[1, 2, 3])
print_params(10, 'Hello', False)

print("\nЧасть 2:")
values_list = [42, 'Python', False]
values_dict = {'a': 3.14, 'b': 'Data', 'c': True}

print_params(*values_list)
print_params(**values_dict)

print("\nЧасть 3:")
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)