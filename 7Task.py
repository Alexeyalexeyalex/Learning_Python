# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import CreateRandomList
countList = int(input("Введите длинну списка: "))

userList = CreateRandomList.randomList(countList)
sumList = []
for i in range(len(userList)//2+len(userList)%2):
    sumList.append(userList[i]*userList[-i-1])

print(f'{userList} - {sumList}')

