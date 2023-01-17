# 40. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Модуль сжатия:
# Для чисел:
# Входные данные:
# 111112222334445
# Выходные данные:
# 5142233415
# Также должно работать и для букв:
# Входные данные:
# AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE
# Выходные данные:
# 6A1F2D7C1A17E
# (5 - количество единиц, далее сама единица, 4 - количество двоек, далее сама двойка и т.д)
# Модуль восстановления работет в обратную сторону - из строки выходных данных, 
# получить строку входных данных.
def Choise(choiseValue):
    if choiseValue.lower() == "r":
        result = ""
        Rle(str(input("Введите строку для сжатия: \n")),result)

    elif choiseValue.lower() == "u":
        Unrle()
    else:
        print("Команда не распознана, повторите ввод")
        Choise(str(input("Выберите что нужно сделать Сжать строку(R) Восстановить данные(U) \n")))

def Rle(userValues,result):
    numbers = ""
    i=0
    while userValues[i] == userValues[0]:
        numbers += userValues[i]
        if i<len(userValues)-1:
            i+=1
        else:
            break
    result += str(len(numbers)) + str(numbers[0])
    userValues = userValues[len(numbers):]
    if len(userValues) > 0:
        Rle(userValues,result)
    else:
        print(result)


def Unrle():
    userValues = str(input("Введите строку для восстановления: \n"))
    result = ""
    while True:
        result += str(userValues[1]) * int(userValues[0])
        if len(userValues) == 2:
            break
        else:
            userValues = userValues[2:]
    print(f"Результат: \n{result}")


Choise(str(input("Выберите что нужно сделать Сжать строку(R) Восстановить данные(U) \n")))

