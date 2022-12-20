# Реализуйте алгоритм перемешивания списка.
import random
lenList = int(input("Введите длинну списка: "))
userList = []
for i in range(lenList):
    userList.append(random.randint(-10,10))
print(f'Список: {userList} ')
random.shuffle(userList)
print(f'Перемешанный список: {userList}')
