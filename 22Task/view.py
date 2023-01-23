
def UserValue():

    value = int(input("\
Что вы хотите сделать?\n\
Ввести данные: 1\n\
Вывести данные на экран: 2\n\
Отфильтровать по имени или по id: 3\n\
Вывести только имя и фамилию: 4\n\
\n\
Ваш выбор: "))

    return ValidateUserValue(value)

def ValidateUserValue(value):
    if value in (1,2,3,4):
        return value
    else:
        print("Неверный ВВОД!\n")
        UserValue()

def UserInformation():
    value = input("Введите данные сотрудника (id,имя,фамилию,номер телефона, комментрий):\n")
    value = value.split(" ")
    return value

def UsingFilter():
    value = int(input("\
Что вы хотите сделать?\n\
Отфильтровать по ID: 1\n\
Отфильтровать по фамилии: 2\n\
Ваш выбор: "))
    if value == 1 or value == 2:
        return value
