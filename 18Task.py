# 44. Напишите программу, которая принимает на вход координаты двух точек и 
# находит расстояние между ними в 2D пространстве.

# Пример:

# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21
def initValues():
    return input("Введите коорденаты точки через запятую: ").split(",")

numsA = initValues()
numsB = initValues()
nums = list(zip(numsB,numsA))
resuktList = [(int(i[0])-int(i[1]))**2 for i in nums]

print(f"Расстояние между точками = {((resuktList[0]+resuktList[1])**0.5)}")