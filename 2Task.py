# Напишите программу, которая принимает на вход число N 
# и выдает набор произведений чисел от 1 до N.

# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

n = int(input("Введите число: "))
list = [1]
item = 1
for i in range(2,n+1):
    for j in range(i,1,-1):
        item *= j
    list.append(item)
    item = 1
print(list)

    