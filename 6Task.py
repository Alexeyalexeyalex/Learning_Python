# Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import CreateRandomList
countList = int(input("Введите длинну списка: "))

userList = CreateRandomList.randomList(countList)
oddNum = []
summa = 0
for i in range(1,len(userList),2):
    oddNum.append(userList[i])
    summa += userList[i]

print(f"{userList} -> на нечётных позициях элементы {oddNum} ответ: {summa}")
