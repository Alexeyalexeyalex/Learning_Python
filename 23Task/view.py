# Вовод данных(1-8) с дисплея
def UserValue():
    value = int(input("\
Что вы хотите сделать?\n\
Ввести ученика (Имя Фамилия): 1\n\
Вывести данные на экран: 2\n\
Добавить предмет: 3\n\
Добавить оценку: 4\n\
Показ листа оценок конкретного ученика: 5\n\
Вывод средней оценки ученика по одному предмету: 6\n\
Вывод среднего балла по школе по конкретному предмету: 7\n\
Вывод количества учеников претендующих на золотую медаль (все оценки либо 4 либо 5): 8\n\
Выход: 0\n\
\n\
Ваш выбор: "))
    return value

# dict = {FIO:{predmet:[osenka]}}

# Вовод данных об ученике
def UserInformation():
    value = input("Введите данные ученика (имя,фамилию):\n")
    return value

# Вовод данных о предмете
def PredmetInformation():
    value = input("Введите данные предмета (Название):\n")
    return value

# Вывод данных одного ученика по фамилии и имени
def PrintUserList(fio,dictUsers):
    if fio not in dictUsers.keys():
        print("Пользователь не найден!")
    else:
        print(f"{fio}:")        
        for indx,value in dictUsers[fio].items():
            print(f"{indx}:{value}")

# Вывод данных всех учеников
def PrintLists(dictUsers):
    for indx,value in dictUsers.items():
        print(indx)
        for ind, val in value.items():
            print(f"{ind}:{val}")

def PrintUserOsenkiOnepredmet(fio,predmet,dictUsers,predmets):
    if fio not in dictUsers.keys():
        print("Пользователь не найден!")
    elif predmet not in predmets.keys():
        print("Предмет не найден!")
    else:
        osenkiList = dictUsers[fio][predmet]
        print(f"{fio} оценки по {predmet}:\n{osenkiList}")
        if len(osenkiList)>0:
            print(f'Средний балл = {sum(int(n) for n in osenkiList)/len(osenkiList)}')