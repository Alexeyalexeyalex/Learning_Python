# Вычислить число c заданной точностью d

# Пример:

# - при $d = 0.001, π = 3.141.$    
# $10^{-1} ≤ d ≤10^{-10}$

import math
pi = math.pi
num = int(input("Введите количество чисел после запятой: "))
list = str(pi).split(".")

print(f"{list[0]}.{list[1][:num]}")
