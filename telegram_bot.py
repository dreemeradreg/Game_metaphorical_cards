#! /usr/bin/env python
# -*- coding: utf-8 -*-

# *****************************
# pip install pyTelegramBotAPI
# *****************************

import sys
import os


import telebot
from telebot import types
bot = telebot.TeleBot('твой id token') # мой 


@bot.message_handler(commands=['start'])
def welcome(message):
	markup_buttons_on_start = types.ReplyKeyboardMarkup(resize_keyboard=True)
	button_get_code = types.KeyboardButton("Получить код")
	button_contacts = types.KeyboardButton("Получить картинку")
	
	
	markup_buttons_on_start.add(button_get_code, button_contacts)
	bot.send_message(message.chat.id, 
			"Добро пожаловать, {0.first_name}!\nЯ - {1.first_name}, бот созданный для игры.".format(message.from_user, bot.get_me()),
			reply_markup=markup_buttons_on_start
			)

@bot.message_handler(content_types=['text'])
def main(message):
	if message.chat.type == 'private':
		if message.text == "Получить код":
			bot.send_message(message.chat.id,"Ваш код для игры: " +str(message.chat.id))

		elif message.text == "Получить картинку":
			a = os.listdir('user/')
			if str(message.chat.id)+'.txt' in a:
				with open('user/'+str(message.chat.id)+'.txt', 'r') as text_card_in_game:
					a = text_card_in_game.read().split("\n")
					text_card_in_game.close()
				if str(a[0]) == "":
					pass
				else:
					img = open(a[0], 'rb')
					bot.send_photo(message.chat.id, img,"картинка ")
					with open('user/'+str(message.chat.id)+'.txt', 'w') as text_card_in_game:
						text_card_in_game.write("")
						text_card_in_game.close()
			

if __name__ == '__main__':
	print("бот работает")
	bot.polling(none_stop=True, interval=0)
