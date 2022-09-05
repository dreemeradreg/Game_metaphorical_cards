#! /usr/bin/env python
# -*- coding: utf-8 -*-

import random
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
import os 
from tkinter import messagebox as mb

name_gamer_global = []
code_gamer = []
collor_gamer = []

mass = []
mass_cach = []

def Get_mi_random_img():
	img_cards = os.listdir("колода/")
	len_cards = len(img_cards)
	global mass
	i = 0
	while i < len_cards:
		mest = random.randint(0, len(img_cards)-1)
		masst_poz = img_cards[mest]
		mass.append(masst_poz)
		del img_cards[mest]
		i+=1
	return mass

def Get_button(root, image_button_shirt):
	button_img_nombers = Get_mi_random_img()
	x = 340
	y = 10
	while_itiration = 0
	for button_nombers in button_img_nombers:
		if while_itiration == 63:
			break
		if x + 100 > 1340:
			x = 340
			y += 140
		miclass = windows_form_button(root, image_button_shirt, x, y, button_nombers)
		x+=110
		while_itiration +=1

class windows_button():
	"""docstring for windows_button"""
	def __init__(self, xi, src, position_x, position_y):
		super().__init__()
		
		self.src = src
		coma = lambda x=xi: self.no_image_logic(xi)
		self.button_shirt_no_image_logic = Button(
				text="отправить "+str(xi), 
				background="#555",		# фоновый цвет кнопки
				foreground="#ccc",		# цвет текста
				padx="5",				# отступ от границ до содержимого по горизонтали
				pady="10",				# отступ от границ до содержимого по вертикали
				font="16",		
				command=coma)
		self.button_shirt_no_image_logic.place(x=position_x, y=position_y)
	
	def no_image_logic(self, operation):
		try:
			with open('user/'+str(operation)+".txt", 'w') as text_card_in_game:
				text_card_in_game.write(str(self.src))
				text_card_in_game.close()
		except:
			pass

class windows_form_button():
	global code_gamer
	def __init__(self, root, image_button_shirt, x, y, button_nombers):
		super().__init__()
		self.root = root

		com = lambda x=button_nombers: self.logicalc(x)
		self.button_shirt = Button(root, 
			image=image_button_shirt,
			command=com)
		self.button_shirt.place(x=x, y=y)

	def logicalc(self, operation):
		self.canvas_rite_window = Canvas(self.root, width=500, height=697)
		self.canvas_rite_window.place(x=1350,y=300)
		
		def yes_image_logic():
			try:
				self.img_window = Image.open(str(src))

				width = 500
				ratio = (width / float(self.img_window.size[0]))
				height = int((float(self.img_window.size[1]) * float(ratio)))

				self.imag_window = self.img_window.resize((width, height), Image.ANTIALIAS)
				self.image_window = ImageTk.PhotoImage(self.imag_window)
				self.canvas_rite_window = Canvas(self.root, width=width, height=height)
				self.canvas_rite_window.place(x=1350,y=300)
				self.canvas_rite_window.create_image(0, 0, anchor="nw", image=self.image_window)
			except:
				pass
			
		global mass 
		global mass_cach
		
		if str(operation) in mass_cach:
			a = mass[64:]
			if len(set(a)-set(mass_cach)) != 0:
				for mass_plus in a:
					if str(mass_plus) not in mass_cach:
						src = 'колода/'+str(mass_plus)
						mass_cach.append(str(mass_plus))
						if len(set(a)-set(mass_cach)) == 0:
							if (self.button_shirt['state'] == tk.NORMAL):
								self.button_shirt['state'] = tk.DISABLED
						break
			else:
				if len(set(a)-set(mass_cach)) == 0:
					print(len(set(a)-set(mass_cach)))
					if (self.button_shirt['state'] == tk.NORMAL):
						self.button_shirt['state'] = tk.DISABLED
		else:
			a = mass[64:]
			if len(set(a)-set(mass_cach)) == 0:
				if (self.button_shirt['state'] == tk.NORMAL):
					self.button_shirt['state'] = tk.DISABLED

			mass_cach.append(str(operation))
			
			src = 'колода/'+str(operation)


	
		self.button_shirt_yes_image_logic = Button(self.root, 
			text="показать", 
			background="#555",		# фоновый цвет кнопки
			foreground="#ccc",		# цвет текста
			padx="30",				# отступ от границ до содержимого по горизонтали
			pady="10",				# отступ от границ до содержимого по вертикали
			font="16",		
			command=yes_image_logic).place(x=10, y=780)

		i = 0
		for xi in code_gamer:
			position_x = 10
			if i == 0:
				position_y = 100
			if i == 1:
				position_y = 248
			if i == 2:
				position_y = 395
			if i == 3:
				position_y = 540
			if i == 4:
				position_y = 695

			xi = windows_button(xi, src, position_x, position_y)
			i +=1 


class windows_form:
	def __init__(self, root_setings, message_text, message_text2, message_text3, message_row, message_column, element_sticky1, element_sticky2, default_value):
		super().__init__()
		self.message = StringVar()
		self.message_2 = StringVar()
		self.message_label = Label(text=message_text, font="Arial 13")
		self.message_label.grid(row=message_row, column=message_column, sticky=element_sticky1)
		self.message_entry = Entry(textvariable=self.message)
		self.message_entry.grid(row=message_row,column=message_column+1, padx=5, pady=5, sticky=element_sticky2)

		self.message_label_2 = Label(text=message_text2, font="Arial 13")
		self.message_label_2.grid(row=message_row, column=message_column+2, sticky=element_sticky1)
		self.message_entry_2 = Entry(textvariable=self.message_2)
		self.message_entry_2.grid(row=message_row,column=message_column+3, padx=5, pady=5, sticky=element_sticky2)
	
		self.message_label_3 = Label(text=message_text3, font="Arial 13")
		self.message_label_3.grid(row=message_row, column=message_column+4, sticky=element_sticky1)
	
		com = lambda: self.get_user_data()
		self.message_button_3 = Button(root_setings,
							text="цвет", 
							background="white",		# фоновый цвет кнопки
							foreground="#000",		# цвет текста
							padx="10",				# отступ от границ до содержимого по горизонтали
							pady="5",				# отступ от границ до содержимого по вертикали
											# высота шрифта
							command=com,
							font="16"
							)
		self.message_button_3.grid(row=message_row, column=message_column+5)

	def get_user_data(self):
		color = self.message_button_3["background"]
		if color == 'white':
			self.message_button_3["background"] = "red"
		elif color == 'red':
			self.message_button_3["background"] = "pink"
		elif color == 'pink':
			self.message_button_3["background"] = "orange"
		elif color == 'orange':
			self.message_button_3["background"] = "yellow"
		elif color == 'yellow':
			self.message_button_3["background"] = "green"
		elif color == 'green':
			self.message_button_3["background"] = "blue"
		elif color == 'blue':
			self.message_button_3["background"] = "purple"
		elif color == 'purple':
			self.message_button_3["background"] = "black"
		elif color == 'black':
			self.message_button_3["background"] = "white"

def main():
	root_setings = Tk()
	root_setings.geometry("1400x350")

	label = Label()
	label.grid(row=0, column=6, sticky="w")

	def get_safe_name():
		global name_gamer_global
		global code_gamer
		global collor_gamer
		users = [name_gamer_1, name_gamer_2, name_gamer_3, name_gamer_4, name_gamer_5]

		for x in users:
			if str(x.message_entry.get()) != '':
				name_gamer_global.append(str(x.message_entry.get()))
				if str(x.message_entry_2.get()) != '':
					code_gamer.append(str(x.message_entry_2.get()))
				if str(x.message_button_3['background']) != '':
					collor_gamer.append(x.message_button_3['background'])

		# print(name_gamer_global,"\n",code_gamer,"\n" ,collor_gamer)
		root_setings.destroy()

	name_gamer_1 = windows_form(root_setings, 
								"Введите Имя игрока:",
								"Введите Код игрока:", 
								"Выбери цвет фигуры игрока:",
								2, 0, "e", "w", "")
	name_gamer_2 = windows_form(root_setings,
								"Введите Имя игрока:",
								"Введите Код игрока:", 
								"Выбери цвет фигуры игрока:",
								3, 0, "e", "w", "")
	name_gamer_3 = windows_form(root_setings,
								"Введите Имя игрока:",
								"Введите Код игрока:", 
								"Выбери цвет фигуры игрока:",
								4, 0, "e", "w", "")
	name_gamer_4 = windows_form(root_setings,
								"Введите Имя игрока:",
								"Введите Код игрока:", 
								"Выбери цвет фигуры игрока:",
								5, 0, "e", "w", "")
	name_gamer_5 = windows_form(root_setings,
								"Введите Имя игрока:",
								"Введите Код игрока:", 
								"Выбери цвет фигуры игрока:",
								6, 0, "e", "w", "")


	# label_1 = Label(text="Укажите имя, код и цвет фикурки!\nцвет может быть любым!",
	# 	justify=LEFT,
	# 	font="Arial 16")
	# label_1.grid(row=0, column=6,rowspan=6, padx=5, pady=5, sticky="e")

	safe_name_button = Button(text="Начать игру", 
						background="#555",		# фоновый цвет кнопки
						foreground="#ccc",		# цвет текста
						padx="30",				# отступ от границ до содержимого по горизонтали
						pady="10",				# отступ от границ до содержимого по вертикали
						font="16",				# высота шрифта
						command=get_safe_name
						)

	safe_name_button.grid(row=7, column=3, padx=5, pady=5, sticky="e")
	root_setings.mainloop()


	root = Tk()
	root.title("Добро пожаловать в игру для мамы")
	root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

	img_fon = Image.open('font.jpg')
	imag_fon = img_fon.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.ANTIALIAS)
	image_fon = ImageTk.PhotoImage(imag_fon)

	logo = Label(root, image=image_fon)
	logo.grid(row=0,column=0)



	img_button_shirt = Image.open('1 ёжики обложка.png')
	width = 90
	ratio = (width / float(img_button_shirt.size[0]))
	height = int((float(img_button_shirt.size[1]) * float(ratio)))
	imag_button_shirt = img_button_shirt.resize((width, height), Image.ANTIALIAS)
	image_button_shirt = ImageTk.PhotoImage(imag_button_shirt)

	

	Get_button(root, image_button_shirt)

	def GET_button_cube():
		random_cube = random.randint(1,6)
		
		random_cube_canvas = Canvas(root, width=100, height=100)
		random_cube_canvas.place(x=200,y=850)
		random_cube_canvas.create_text(50, 50, text=str(random_cube),
					justify=CENTER, font="Verdana 44")

	def GET_button_rage_card():
		with open('text_card_in_game.txt', 'r',encoding="utf-8") as text_card_in_game:
			text_card_in_game_mass = text_card_in_game.read().split("\n")
			text_card_in_game.close()
		
		
		random_card = random.randint(0,len(text_card_in_game_mass)-1)
		atribute = text_card_in_game_mass[random_card]
		if "|" in atribute:
			atribute = str(text_card_in_game_mass[random_card]).replace("|", "\n")

		random_cube_canvas = Canvas(root, width=500, height=250)
		random_cube_canvas.place(x=1350,y=10)
		random_cube_canvas.create_text(250, 100, text=atribute,
					justify=CENTER, font="Verdana 20")

	def drag(event):
		mouse_x = logo.winfo_pointerx() - logo.winfo_rootx()
		mouse_y = logo.winfo_pointery() - logo.winfo_rooty()
		
		event.widget.place(x=mouse_x, y=mouse_y, anchor=CENTER)

	def canvas_game_fishka_windosw(y1, y2, name_user , color_user):
		canvas_game_fishka_1_0 = Canvas(root, width=70, height=70)
		canvas_game_fishka_1_0.place(x=280,y=y1, anchor=CENTER)
		canvas_game_fishka_1_0.create_rectangle(0, 0, 100, 100, fill=str(color_user))

		canvas_game_fishka_1 = Canvas(root, width=70, height=70)
		canvas_game_fishka_1.place(x=280,y=y1, anchor=CENTER)
		canvas_game_fishka_1.create_rectangle(0, 0, 100, 100, fill=str(color_user))
		canvas_game_fishka_1.bind("<B1-Motion>", drag)

		canvas_game_window_1 = Canvas(root, width=200, height=80)
		canvas_game_window_1.place(x=10,y=y2)
		canvas_game_window_1.create_text(100, 40, text=str(name_user),
				justify=CENTER, font="Verdana 12")
	
	if len(name_gamer_global) >= 1:
		canvas_game_fishka_windosw(50, 10, name_gamer_global[0], collor_gamer[0])
	if len(name_gamer_global) >= 2:
		canvas_game_fishka_windosw(200, 157, name_gamer_global[1], collor_gamer[1])
	if len(name_gamer_global) >= 3:	
		canvas_game_fishka_windosw(342, 303, name_gamer_global[2], collor_gamer[2])
	if len(name_gamer_global) >= 4:
		canvas_game_fishka_windosw(490, 450, name_gamer_global[3], collor_gamer[3])
	if len(name_gamer_global) >= 5:
		canvas_game_fishka_windosw(650, 605, name_gamer_global[4], collor_gamer[4])

	button_cube = Button(root, 
			text="бросок кубика", 
			background="#900",		# фоновый цвет кнопки
			foreground="#ccc",		# цвет текста
			padx="30",				# отступ от границ до содержимого по горизонтали
			pady="10",				# отступ от границ до содержимого по вертикали
			font="16",	
			command=GET_button_cube).place(x=10, y=900)

	button_rage_card = Button(root, 
			text="получить карту", 
			background="#900",		# фоновый цвет кнопки
			foreground="#ccc",		# цвет текста
			padx="30",				# отступ от границ до содержимого по горизонтали
			pady="10",				# отступ от границ до содержимого по вертикали
			font="16",	
			command=GET_button_rage_card).place(x=10, y=840)

	root.mainloop()

if __name__ == '__main__':
	main()

