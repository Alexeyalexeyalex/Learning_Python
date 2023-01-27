import copy, random as r

usersNames = ['Иван','Сергей','Константин','Василий','Алексей','Григорий','Михаил','Павел','Андрей','Акакий']
usersSecondNames = ['Иванов','Петров','Сидоров','Рябоконь','Баранов','Сахаров','Симушин','Гавин','Андержанов','Голоухов','Гусев','Григорьев']
predmetNames = ['Математика','Физика','Алгебра','Гнометрия','Музыка','Литература','Информатика']


# Создание нового предмета
def ImportPredmet(predmet,dictPredmet,dictUsers):
    dictPredmet[predmet] = []
    for index,value in dictUsers.items():
        value[predmet] = []


        
    

# Создание нового ученика
def ImportUser(user,dictUsers,predmets):
    dictUsers[user]=copy.deepcopy(predmets)

 # Скрытая функция для создания 100 учеников
def ImportHundredUsers(dictUsers,predmets):
    for i in range(100):
        firstName = usersNames[r.randint(0,len(usersNames)-1)]
        secondName = usersSecondNames[r.randint(0,len(usersSecondNames)-1)]
        name = f'{firstName}  {secondName}'
        ImportUser(name,dictUsers,predmets)
        predmetName = predmetNames[r.randint(0,len(predmetNames)-1)]
        ImportPredmet(predmetName,predmets,dictUsers)


    
# Присвоение оценки определенному ученику и определенному предмету
def AddOsenka(fio,predmet,dictUsers,predmets):
    if fio not in dictUsers.keys():
        print("Пользователь не найден!")
    elif predmet not in predmets.keys():
        print("Предмет не найден!")
    else:
        osenka = input("Введите оценку:\n")
        dictUsers[fio][predmet].append(osenka)
        print("Вы добавили оценку")
        


    




