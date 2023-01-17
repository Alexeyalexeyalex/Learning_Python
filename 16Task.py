# 39(1). Создайте программу для игры с конфетами человек против человека. 
# Реализовать игру игрока против игрока в терминале. 
# Игроки ходят друг за другом, вписывая желаемое количество конфет. 
# Первый ход определяется жеребьёвкой. 
# В конце вывести игрока, который победил

# Условие задачи: На столе лежит 221 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
#  Все конфеты оппонента достаются сделавшему последний ход. 

# В качестве дополнительного усложнения можно:
#         a) Добавьте игру против бота ( где бот берет рандомное количество конфет от 0 до 28)

#         b) Подумайте как наделить бота ""интеллектом"" 
#         (есть алгоритм, позволяющий выяснить какое количесвто конфет необходимо брать, 
#         чтобы гарантированно победить, соответственно внедрить этот алгоритм боту )





def userVsUser(candyCount):

    playerNumber = 1
    i = 1
    while candyCount>0:
        print(f"Количество конфет: {candyCount}")
        playerCandy = int(input(f"Игрок {playerNumber} введите количество конфет от 1 до 28: "))
        if playerCandy>28 or playerCandy<1:
            print("Введите количество конфет из диапазона!")
            continue
        elif playerCandy > candyCount:
            print("Введенное число больше оставшихся конфет, введите меньше")
            continue
        
        candyCount -= playerCandy
        if candyCount == 0:
            print(f"Игрок {playerNumber} Победил!")
            break
        playerNumber+=i
        i*=-1

def userVsBot(candyCount):

    while candyCount>0:
        print(f"Количество конфет: {candyCount}")
        playerCandy = int(input(f"Игрок введите количество конфет от 1 до 28: "))
        if playerCandy>28 or playerCandy<1:
            print("Введите количество конфет из диапазона!")
            continue
        elif playerCandy > candyCount:
            print("Введенное число больше оставшихся конфет, введите меньше")
            continue
        
        candyCount -= playerCandy
        if candyCount == 0:
            print(f"Игрок Победил!")
            break
        else:
            if candyCount < 29:
                print(f"Бот берет {candyCount} конфет")
                candyCount-=candyCount
            elif candyCount % 28 != 0:
                print(f"Бот берет {candyCount % 28} конфет")
                candyCount-=candyCount % 28
            else:
                print(f"Бот берет 28 конфет")
                candyCount-= 28 
            if candyCount == 0:
                print(f"Бот Победил!")
                break

userVsBot(221)



