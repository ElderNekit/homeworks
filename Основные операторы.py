def find_pairs(n):
    pairs = []
    for i in range(1, n):
        for j in range(i+1, n+1):
            if i + j == n:
                pairs.append((i, j))
    return pairs

def generate_password(n):
    pairs = find_pairs(n)
    password = ""
    for pair in pairs:
        password += str(pair[0]) + str(pair[1])
    return password

n = int(input("Введите число от 3 до 20: "))
while n < 3 or n > 20:
    n = int(input("Введите число от 3 до 20: "))

result = generate_password(n)
print(f"Пароль для числа {n}: {result}")
