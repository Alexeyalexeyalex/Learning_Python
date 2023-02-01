import telebot, random as r
from telebot import types

bot = telebot.TeleBot("5759160694:AAF0lwtd0MzznLr1YYpnAAtXDpdgJPO4OxU")

candys = 221
userID = 1
botOrUser = None
max_sweet = 28

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id,f"С кем вы хотите играть?")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)#создание клавиатуры
    but1 = types.KeyboardButton("Игрок против игрока")#создание кнопок
    but2 = types.KeyboardButton("Игрок против бота")
    markup.add(but1)#добавление кнопок
    markup.add(but2)#добавление кнопок
    bot.send_message(message.chat.id,"Выбери ниже", reply_markup=markup)
    bot.register_next_step_handler(message, validateStart)

def validateStart(message):
    if message.text == 'Игрок против игрока':
        pvpPlay(message)
    elif message.text == 'Игрок против бота':
        pvePlay(message)
    else:
        start(message)


#PVE ИГРА

def pvePlay(message):
    global botOrUser
    botOrUser = r.choice(["user","bot"])
    if botOrUser == 'user':
        bot.send_message(message.chat.id,"Вы ходите первым")
        userTurn(message)
    else:
        bot.send_message(message.chat.id,"Бот ходит первым")
        botTurn(message)


def validateTurn(message):
    global botOrUser, candys
    if candys >0:
        if botOrUser == 'user':
            userTurn(message)
        else:
            botTurn(message)
    else:
        botOrUser = 'user' if  botOrUser=='bot' else 'bot'
        bot.send_message(message.chat.id,f"Победил {botOrUser}!")
        candys = 221
        start(message)


def botTurn(message):
    global candys, botOrUser
    # choise = r.randint(1,28)
    if candys <= max_sweet:
        choise = candys
    elif candys % max_sweet == 0:
        choise = 28
    else:
        choise = candys - max_sweet * (candys // max_sweet) -1
    choise = 1 if choise == 0 else choise
    bot.send_message(message.chat.id,f"Осталось {candys} конфет")
    bot.send_message(message.chat.id,f"Бот берет {choise} конфет")
    candys -= choise
    botOrUser = "user"
    validateTurn(message)

def userTurn(message):
    global candys, botOrUser
    bot.send_message(message.chat.id,f"Осталось {candys} конфет")
    getCandyCountPve(message)
    
    

def getCandyCountPve(message):
    bot.send_message(message.chat.id,"Введите число от 1 до 28")
    bot.register_next_step_handler(message, ValidateCandysCountPve)

def ValidateCandysCountPve(message):
    global candys,botOrUser
    if int(message.text)>0 and int(message.text)<29:
         candys -= int(message.text)
         botOrUser = "bot"
         validateTurn(message)
    else:
        getCandyCountPve(message)



#PVP ИГРА

def pvpPlay(message):
    bot.send_message(message.chat.id,f"Всего конфет {candys}\n Ходит игрок {userID}")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)#создание клавиатуры
    but1 = types.KeyboardButton("Взять конфету")#создание кнопок
    but2 = types.KeyboardButton("Заново")
    markup.add(but1)#добавление кнопок
    markup.add(but2)#добавление кнопок
    bot.send_message(message.chat.id,"Выбери ниже", reply_markup=markup)
    bot.register_next_step_handler(message, controller)

# @bot.message_handler(content_types=["text"])#вызов функции если тип сообщения - текст
def controller(message):
    if message.text.lower() == "заново":
        global candys, userID
        candys = 221
        userID = 1
        start(message)
    elif message.text.lower() == "взять конфету":
        getCandyCountPvp(message)
    else:
        pvpPlay(message)

def getCandyCountPvp(message):
    bot.send_message(message.chat.id,"Число от 1 до 28")
    bot.register_next_step_handler(message, ValidateCandysCount)

def getCandy(candyValue):
    global candys
    candys -= int(candyValue.text)
    Validate(candyValue)

def Validate(message):
    global candys,userID
    if candys<=0:
        bot.send_message(message.chat.id,f"Победил игрок {userID}!")
        candys = 221
        userID = 1
        start(message)
        return
    if userID == 1:
        userID = 2
    else:
        userID = 1
    pvpPlay(message)
    
def ValidateCandysCount(message):
    if int(message.text)<1 or int(message.text)>28:
         getCandyCountPvp(message)
    else:
        getCandy(message)


bot.infinity_polling()