A = int(input())
B = int(input())

# Вывод всех четных чисел на заданном отрезке
for num in range(A, B+1):
    if num % 2 == 0:
        print(num, end=' ')
        