# Задана натуральная степень k. Сформировать случайным образом список 
# коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен 
# степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random

k = int(input("Введите степень: "))
result = ''
for i in range(k,0-1,-1):
    num = random.randint(0,100)
    if num ==0:
        continue
    if i == 0:
        result += str(num)
        continue
    if i == 1:
        result += str(num)+"*x"+" + "
        continue
    result += str(num)+"*x**"+str(i)+" + "
with open('Result2.txt','w') as data:
    data.write(result)

print(result)
    

