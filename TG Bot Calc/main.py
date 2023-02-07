import telebot, modul, io, time
from telebot import types

bot = telebot.TeleBot("5759160694:AAF0lwtd0MzznLr1YYpnAAtXDpdgJPO4OxU")


num1 = 0
num2 = 0
answer = ""

@bot.message_handler(commands=["start"])
def start(message):
    GetValue(message)
    
def resultCalc(message):
    modul.init(num1, num2)
    if answer == "+":
        result = modul.summ()
        
    elif answer == "-":
        result = modul.subtraction()
        
    elif answer == "*":
        result = modul.multipliction()
        
    elif answer == "/":
        result = modul.division()
        
    elif answer == "//" and type(num1)!=complex:
        result = modul.integer_division()
        
    elif answer == "%" and type(num1)!=complex:
        result = modul.remainder_of_division()
        
    else:
        bot.send_message(message.chat.id,"Данное действие невозможно!")
        bot.send_message(message.chat.id,f"Введите знак: ")
        bot.register_next_step_handler(message, GetSignUser) 
        return

        
    PrintResult(num1,num2,answer,result,message)
    logData(num1,num2,answer,result,message)
    GetValue(message)







def GetValue(message):
    global num1, num2
    num1 = 0
    num2 = 0
    bot.send_message(message.chat.id,"Вы будете работать с комплексными числами?(y,n) ")
    bot.register_next_step_handler(message, validateTypeNumber)

def validateTypeNumber(message):
    if message.text == 'y':
        GetValueComplex1(message)
    elif message.text == 'n':
        GetValueInt1(message)
    else:
        GetValue(message)






def GetValueComplex1(message):
    bot.send_message(message.chat.id,f"Введите первое число: ")
    bot.register_next_step_handler(message, GetValueComplex2)


def GetValueComplex2(message):
    global num1
    num1 = complex(message.text)
    bot.send_message(message.chat.id,f"Введите второе число: ")
    bot.register_next_step_handler(message, GetValueComplex)

def GetValueComplex(message):
    global num2
    num2 = complex(message.text)
    bot.send_message(message.chat.id,f"Введите знак: ")
    bot.register_next_step_handler(message, GetSignUser) 

def GetValueInt1(message):
    bot.send_message(message.chat.id,f"Введите первое число: ")
    bot.register_next_step_handler(message, GetValueInt2)


def GetValueInt2(message):
    global num1
    num1 = int(message.text)
    bot.send_message(message.chat.id,f"Введите второе число: ")
    bot.register_next_step_handler(message, GetValueInt)

def GetValueInt(message):
    global num2
    num2 = int(message.text)
    bot.send_message(message.chat.id,f"Введите знак: ")
    bot.register_next_step_handler(message, GetSignUser) 
  

def GetSignUser(message):
    global answer
    answer = message.text
    resultCalc(message)




def PrintResult(num1, num2, sign, result, message):
    bot.send_message(message.chat.id, f"{num1} {sign} {num2} = {result}")


def logData(num1, num2, sign, result, message):
    file = open('log.txt','a', encoding="utf-8")
    file.write(f'Пользователь: {message.from_user.first_name} Данные: {num1} {sign} {num2} = {result} Время: {time.strftime("%Y-%m-%d %H:%M")}\n')
    file.close()

bot.infinity_polling()

