import view, model

def Start():
    userInformation = {}
    predmets ={}
    while True:
        value = view.UserValue()
        if value == 1:
            fio = view.UserInformation()
            model.ImportUser(fio,userInformation,predmets)
            print("Вы добавили ученика")
        elif value == 0:
            return
        elif value == 2:
            view.PrintLists(userInformation)
            print(userInformation)
        elif value == 3:
            predmet = view.PredmetInformation()
            model.ImportPredmet(predmet,predmets,userInformation)
            print("Вы добавили предмет")
        elif value == 4:
            fio = view.UserInformation()
            predmet = view.PredmetInformation()
            model.AddOsenka(fio,predmet,userInformation,predmets)
            
        elif value == 5:
            fio = view.UserInformation()
            view.PrintUserList(fio,userInformation)
        elif value == 6:
            fio = view.UserInformation()
            predmet = view.PredmetInformation()
            view.PrintUserOsenkiOnepredmet(fio,predmet,userInformation,predmets)
        elif value == 100:
            model.ImportHundredUsers(userInformation,predmets)
        else:
            print("Неправильный ввод!")


    