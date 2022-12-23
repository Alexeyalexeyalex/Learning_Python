# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

num = int(input("Введите число: "))
listUser = [0,1]
resultList = []
for i in range(2,num+1):
    listUser.append(listUser[i-1]+listUser[i-2])
for i in range(len(listUser)-1,0,-1):
    if i%2 == 0:
        resultList.append(listUser[i]*-1)
    else:
        resultList.append(listUser[i])
resultList+=listUser

print(resultList)
