from logics import *
import openpyxl
import tkinter as tk


""" модуль: интерфейс"""



def get_sheet_name():
    # Открытие книги Excel
    wb = openpyxl.load_workbook('/Users/gregoryreyn/Desktop/Общая БД 2.xlsm')
    # Создание окна с кнопками листов
    root = tk.Tk()
    root.title("Выберите лист")
    for i, sheet in enumerate(wb.sheetnames):
        # Создание кнопки с именем листа
        btn = tk.Button(root, text=sheet, command=lambda sheet_name=sheet: show_sheet(sheet_name, root))
        btn.grid(row=0, column=i)
    root.mainloop()
    return root


def button():
    root = tk.Tk()
    root.title("Доступныее функции")
    # button1 = tk.Button(root, text="Открыть файл чтения", command='')
    # button1.pack()
    # button2 = tk.Button(root, text="Открыть файл записи", command='')
    # button2.pack()
    button3 = tk.Button(root, text="запись", command=lambda: main())
    button3.pack()
    button3 = tk.Button(root, text="проверка кнопок", command=get_sheet_name)
    button3.pack()
    root.mainloop()


button()
