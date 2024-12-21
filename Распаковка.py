def print_params(a=1, b='строка', c=True):
    """Функция выводит переданные параметры."""
    print(a, b, c)
print("Вызов 1:")
print_params()
print("\nВызов 2:")
print_params(10)
print("\nВызов 3:")
print_params(25, 'другая строка')
print("\nВызов 4:")
print_params(b=25)
print("\nВызов 5:")
print_params(c=[1, 2, 3])
values_list = [3.14, 'пример строки', False]
values_dict = {'a': 42, 'b': 'словарь', 'c': None}
print("\nВызов 6 (распаковка из списка):")
print_params(*values_list)
print("\nВызов 7 (распаковка из словаря):")
print_params(**values_dict)
values_list_2 = [54.32, 'Строка']
print("\nВызов 8 (распаковка с дополнительным параметром):")
print_params(*values_list_2, 42)