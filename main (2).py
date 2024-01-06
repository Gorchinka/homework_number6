# Ввод количества чисел N
N = int(input())

# Ввод N целых чисел
numbers = [int(input()) for _ in range(N)]

# Подсчет чисел, равных нулю
zero_count = numbers.count(0)

# Вывод результата
print(zero_count) 

