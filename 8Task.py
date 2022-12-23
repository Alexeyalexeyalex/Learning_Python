# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
import random as r
num = int(input("Введите длинну: "))
listUser = []
for i in range(num):
    listUser.append(round(r.uniform(0,100),2))

    

max = 0
min = 1
for i in listUser:
    if i-(i//1)>max:
        max = i-(i//1)
    if i-(i//1)<min:
        min = i-(i//1)
dif = max-min


print(f'{listUser} => {round(dif,2)}')

