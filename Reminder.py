from tkinter import * # библиотеку
from tkinter import messagebox as mb # сообщение пользователю
from tkinter import simpledialog as sd
import datetime
import time
import pygame # для работы со звуком
from угадай import window

#Создаем окно программы

window = Tk()
window.title("Напоминание")
#метка которая будет писать "Установите напоминание
label = Label(text="Установите напоминание")
label.pack(pady=10) # отступ по вертикали
#кнопка
set.button = Button(text="Установить напоминание", command=set) #command=set - выполняется операция set - установить
set.button.pack

window.mainloop()
