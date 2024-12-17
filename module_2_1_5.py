def get_password(n):
    password = ""
    for i in range(1, n+1):
        for j in range(i+1, n+1):  
            if n % (i + j) == 0: 
                password += str(i) + str(j)
    return password

n = int(input("Введите число от 3 до 20: "))
if 3 <= n <= 20:
    result = get_password(n)
    print(f"Пароль для числа {n}: {result}")
else:
    print("Число должно быть в диапазоне от 3 до 20!")
