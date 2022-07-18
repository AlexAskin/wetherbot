import pyowm
from pyowm.utils import config
from pyowm.utils import timestamps

import telebot


# ---------- FREE API KEY examples -------------

owm = pyowm.OWM('2bfec5f6ecaec790e64257f01aab3311')
mgr = owm.weather_manager()


# ---------- TELEGRAM KEYS ---------------------
bot = telebot.TeleBot("5161523716:AAGz6rSYV-UYVxhYxLynnHRfRgB0mQY2YaI", parse_mode=None)
# You can set parse_mode by default. HTML or MARKDOWN


@bot.message_handler(content_types=['text'])
def send_echo(message):
    #bot.reply_to(message, message.text)

    #user_choice = message.text

    message.text

    if message.text == '0':
        user_choice = 'в Тель-Авиве сейчас:' 
    
        city_1 = 'Tel Aviv'
        city_2 = ',IL'
        city = city_1+city_2
        
    elif message.text == '2':
        user_choice = 'в Питере cейчас:'

        city_1 = 'Saint Petersburg'
        city_2 = ',Rus'
        city = city_1+city_2
        
    elif message.text == '1':
        user_choice = 'Погода в Выборге:'

        city_1 = 'Viborg'
        city_2 = ',Rus'
        city = city_1+city_2
        
    elif message.text == '3':
        user_choice = 'в Киеве сейчас:'

        city_1 = 'Kyiv'
        city_2 = ',Ukraine'
        city = city_1+city_2
        
    elif message.text == '4':
        user_choice = 'в Берлине сейчас:'

        city_1 = 'Berlin'
        city_2 = ',Germany'
        city = city_1+city_2

    elif message.text == '5':
        user_choice = 'в Париже во Франции сейчас:'

        city_1 = 'Paris'
        city_2 = ',France'
        city = city_1+city_2
        
    elif message.text == '6':
        user_choice = 'над Лондоном сейчас:'

        city_1 = 'London'
        city_2 = ',GB'
        city = city_1+city_2
        
    elif message.text == '7':
        user_choice = 'в Нью-Йорке сейчас:' 

        city_1 = 'New York'
        city_2 = ',USA'
        city = city_1+city_2
        
    elif message.text == '8':
        user_choice = 'в Москве сейчас:' 

        city_1 = 'Moscow'
        city_2 = ',Rus'
        city = city_1+city_2
        
    elif message.text == '9':
        user_choice = 'в Черногории сейчас:' 

        city_1 = 'Bar'
        city_2 = ',Montenegro'
        city = city_1+city_2
        
    else:
        
        user_choice1 = 'Выберите город, в котором вы хотите узнать погоду:\
        \n0 -Тель-Авив\
        \n1 -Выборг\
        \n2 -Санкт-Петербург\
        \n3 -Киев\
        \n4 -Берлин\
        \n5 -Париж\
        \n6 -Лондон\
        \n7 -Нью-Йорк\
        \n8 -Москва\
        \n9 -Бар, Черногория\
        \n\nНапример в Бат-Яме сейчас:'

        bot.send_message(message.chat.id, user_choice1)

        
        user_choice = ''
        
        city_1 = 'Bat Yam'
        city_2 = ',IL'
        city = city_1+city_2

        

    
    observation = mgr.weather_at_place(city)
    
    w = observation.weather
    temp_all = w.temperature('celsius')
    temp_medium = w.temperature('celsius')['temp']
    sky = w.detailed_status

    #answer = (city_1+':',str(temp_medium)+ 'C,',str(sky),w,'\n')
    #answer = (str(city_1+':'))
    #answer += (str(temp_medium))
    #answer += (str(sky))
    #answer += ('\n')
    answer = (str(user_choice)+'\n'+city_1+': '+ str(temp_medium) + 'C, ' + str(sky) + '\n')# + str(user_choice))
    #print(w)
        

    
    bot.send_message(message.chat.id, answer)



    
bot.polling(none_stop = True)












