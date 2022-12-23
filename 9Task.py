# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

num = int(input("Введите число: "))
binary = ""
i = num
while i>0:
    binary = str(i%2) + binary
    i//= 2

print(f"{num} - {binary}")
