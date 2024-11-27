my_dict = {
    'Vasya': 1975,
    'Egor': 1999,
    'Masha': 2002
}
print("Dict:", my_dict)
existing_value = my_dict['Masha']
print("Existing value:", existing_value)
not_existing_value = my_dict.get('Ivan', None)
print("Not existing value:", not_existing_value)
my_dict['Kamila'] = 1981
my_dict['Artem'] = 1915
deleted_value = my_dict.pop('Egor', None)
print("Deleted value:", deleted_value)
print("Modified dictionary:", my_dict)
my_set = {1, 'Яблоко', 42.314, 1, 'Яблоко', (5, 6, 1.6)}
print("Set:", my_set)
my_set.add(13)
my_set.add('Апельсин')
my_set.pop()
print("Modified set:", my_set)