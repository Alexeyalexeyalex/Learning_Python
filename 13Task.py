# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов 
# исходной последовательности.


import CreateRandomList

count = int(input("Введите размерность списка: "))

userList = CreateRandomList.randomList(count)
resultList = []
for i in userList:
    countElements = userList.count(i)
    if countElements == 1:
        resultList.append(i)

print(f"{userList} -> {resultList}")
