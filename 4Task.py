# Задайте список из N элементов, 
# заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

n=int(input("Введите число для создания списка(-n:n): "))
with open('file.txt','w') as data:
    for i in range(-n,n+1):
        data.write(f'{str(i)}\n')

list = []
with open('file.txt','r') as data:
    for line in data:
        list.append(int(line))
print(f'Ваш список: {list}')

userValues = input('Введите значения через "," для перемножения: ').split(",")

result = 1
for i in userValues:
    result*=list[int(i)]
print(result)
