X = int(input())

# Получение списка натуральных делителей числа X
devisors = [i for i in range(1, X + 1) if X % i == 0]

# Вывод количества натуральных делителей числа X
print(len(devisors))
