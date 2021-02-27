import re
import socket
import telebot
import threading


bot = telebot.TeleBot('1285622549:AAHFdOKbWYXDRIxXcfPPoA6f3oCdkoeHUZ4')

# ip = socket.gethostbyname("zipta.ru")


@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    ip = ''

    def scan_port(ip, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        try:
            connect = sock.connect((ip, port))
            bot.send_message(message.from_user.id, f'Port : {port},  its open.')
            print(message.from_user.id, f'Port : {port},  its open.')
            connect.close()
        except:
            pass

    if message.text.lower() == ("привет"):
        bot.send_message(message.from_user.id, "Привет, могу помочь тебе просканировать открытые порты какого-нибудь веб-ресурса.\nНапиши адрес сайта, который хочешь просканировать")
        print(message.text)
    elif (message.text).isnumeric():
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши: привет.")
        print(message.text)
    elif (message.text).isalnum:
        try:
            socket.gethostbyname(message.text) # re.match('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', message.text):
            print(message.text)
            ip = socket.gethostbyname(message.text)
            for i in range(65535):
                potoc = threading.Thread(target=scan_port, args=(ip, i))
                potoc.start()
            bot.send_message(message.from_user.id, "Поиск закончен.")
            print("Поиск закончен.")
        except Exception as err:
            print(err)
            print(message.text)
            bot.send_message(message.from_user.id, "Я не понимаю. Введи адрес веб-сайта без http:// или https:// — Например, mail.ru или напиши: привет.")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши: привет.")
        print(message.text)


bot.polling(none_stop=True, interval=0)



