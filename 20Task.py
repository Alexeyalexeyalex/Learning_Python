# 46. Найти произведение пар чисел списка(парой считаем первый и последний, второй предпоследний и тд)

import random as r
nums = []
quant = int(input("Введите количество: "))
for i in range(quant):
    nums.append(r.randint(1,10))
print(f"Ваши числа: {nums}")
resultList = []

while len(nums)>2:
    sum = 0
    for indx, value in enumerate(nums):
        if indx == 0 or indx == len(nums)-1:
            sum += nums.pop(indx)
        print(sum)
    print(nums)
    resultList.append(sum)
if len(nums) == 1:
    resultList.append(nums.pop(0))
else:
    resultList.append(nums[0]+nums[1])

print(resultList)
        



