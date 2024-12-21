def calculate_structure_sum(data):
    total_sum = 0

    def recursive_sum(element):
        nonlocal total_sum
        if isinstance(element, int):
            total_sum += element
        elif isinstance(element, str):
            total_sum += len(element)
        elif isinstance(element, list):
            for item in element:
                recursive_sum(item)
        elif isinstance(element, tuple):
            for item in element:
                recursive_sum(item)
        elif isinstance(element, dict):
            for key, value in element.items():
                recursive_sum(key)
                recursive_sum(value)
    for item in data:
        recursive_sum(item)
    return total_sum

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = calculate_structure_sum(data_structure)
print(result)