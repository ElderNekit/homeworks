immutable_var = (1, 2, 'a', 'b')
print("Immutable tuple:", immutable_var)
try:
    immutable_var[0] = 10
except TypeError as e:
    print("Ошибка:", e)
    print("Невозможно изменить элементы кортежа, так как кортежи являются неизменяемыми объектами в Python.")
mutable_list = [1, 2, 'a', 'b']
mutable_list[0] = 10
mutable_list.append('Modified')
print("Mutable list:", mutable_list)