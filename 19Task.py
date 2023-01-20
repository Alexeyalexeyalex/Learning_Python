# 45. Найти сумму чисел списка стоящих на нечетной позиции

import random as r
nums = []
quant = int(input("Введите количество: "))
for i in range(quant):
    nums.append(r.randint(1,10))
print(f"Ваши числа: {nums}")

nums = list(filter(lambda x: x[0]%2==0,enumerate(nums)))
print(f"Сумма чисел списка стоящих на нечетной позиции: {sum(i[1] for i in nums)}")

