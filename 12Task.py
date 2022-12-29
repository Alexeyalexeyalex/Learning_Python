# Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.

num = int(input("Введите число: "))
listOfNums = []
while num!= 1:
    if num%2 == 0:
        listOfNums.append(2)
        num/=2
        continue
    if num%3 == 0:
        listOfNums.append(3)
        num/=3
        continue
    if num%5 == 0:
        listOfNums.append(5)
        num/=5
        continue
    if num%7 == 0:
        listOfNums.append(7)
        num/=7
        continue

print(listOfNums)

