my_string = input("Что хотите узнать?: ")
print("Количество символов в введённом тексте:", len(my_string))
print("Строка в верхнем регистре:", my_string.upper())
print("Строка в нижнем регистре:", my_string.lower())
my_string_no_spaces = my_string.replace(" ", "")
print("Строка без пробелов:", my_string_no_spaces)
print("Первый символ строки:", my_string[0])
print("Последний символ строки:", my_string[-1])