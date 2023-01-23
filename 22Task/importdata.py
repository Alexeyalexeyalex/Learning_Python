
def ImportValues():
    with open('DATA.txt', 'r',encoding='utf-8') as file:
        value = file.readlines()
        print("ID   Имя    Фамилия      Номер телефона     Комментарий")
        for i in value:
            print(i, end="")

def ImportFio():
    with open('DATA.txt', 'r',encoding='utf-8') as file:
        value = file.readlines()
        print("Имя    Фамилия")
        for i in value:
            list = i.split(" ")
            for j in list[1:3]:
                print(j, end=" ")
            print()

def ImportFilter(id):
    with open('DATA.txt', 'r',encoding='utf-8') as file:
        value = file.readlines()
        list =[]
        print("ID   Имя    Фамилия      Номер телефона     Комментарий")
        for i in value:
            list.append(i.split(" "))
        if id == 0:
            list = sorted(list, key = lambda x: int(x[id]))
        else:
            list = sorted(list, key = lambda x: x[id])
        
        for k in list:
            for j in k:
                print(j, end=" ")
            
