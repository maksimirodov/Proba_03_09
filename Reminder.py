from tkinter import * # библиотеку
from tkinter import messagebox as mb # сообщение пользователю
from tkinter import simpledialog as sd
import datetime
import time
import pygame # для работы со звуком


#Создаем окно программы


#установка напоминания
def set():
    rem = sd.askstring("Время напоминания","Введите время напоминания в формате: ЧЧ:ММ (в 24 часовом формате)") # получим время, которое введет пользователь с помощью simpledialog, askstring - запрашиваем текстовую строку
    # получаем временную метку, когда сработает напоминание
    if rem: # если переменная rem не пустая, пользователь что-то ввел
# обработка исключений
        try:
            hour = int(rem.split(":")[0]) #split() делит то что ввел пользователь, в данном случае через : часы и минуты [0] - сначаkf идут часы, нулевой элемент строки, часы виде числа поэтому int
            minute = int(rem.split(":")[1]) # число часов попадет в hour, минуты в минут из-за [0],[1]
# получаем текущее время в переменной now
            now = datetime.datetime.now()
            print(now)
# получаем время на которе уставливаем напоминание
            dt = now.replace(hour=hour, minute=minute) #заменяем часы на часы и минуты установленные для напоминания. красным выделен параметр
            print(dt)
        #получаем временную метку в млрд сек.
            t = dt.timestamp()
            print(t)
    #прорабатываем исключения
        except Exception as e:
            mb.showerror("Ошибка!", f"Произошла ошибка {e}" )

window = Tk()
window.title("Напоминание")
#метка которая будет писать "Установите напоминание
label = Label(text="Установите напоминание")
label.pack(pady=10) # отступ по вертикали
#кнопка
set_button = Button(text="Установить напоминание", command=set) #command=set - выполняется операция set - установить
set_button.pack()

window.mainloop()
