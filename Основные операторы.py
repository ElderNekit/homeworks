def generate_password(n):
    papyrus = "123456789"
    password = ""
    for i in range(len(papyrus)):
        for j in range(i + 1, len(papyrus)):
            a = int(papyrus[i])
            b = int(papyrus[j])
            pair_sum = a + b
            if pair_sum != 0 and n % pair_sum == 0:
                password += str(a) + str(b)
    return password
n1 = 9
n2 = 11
password1 = generate_password(n1)
password2 = generate_password(n2)
print(f"Пароль для {n1}: {password1}")
print(f"Пароль для {n2}: {password2}")
def generate_password(n):
    result = ""
    unique_pairs = []
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if j > i:
                if (i, j) not in unique_pairs:
                    result += str(i) + str(j)
                    unique_pairs.append((i, j))

    return result
n = int(input("Введите число n (от 3 до 20): "))
if 3 <= n <= 20:
    password = generate_password(n)
    print(f"Сгенерированный пароль для n = {n}: {password}")
else:
    print("Число должно быть в диапазоне от 3 до 20.")