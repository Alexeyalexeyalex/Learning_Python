# 47.Сформировать список из N членов последовательности
# Для N=5: 1,-3,9,-27,81 (каждый член больше предыдущего в три раза, знак чередуется)
import math

N = 5
resultList = [int(math.pow(-3,i)) for i in range(0,N)]
print(resultList)