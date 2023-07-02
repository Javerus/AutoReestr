from logics import *
import openpyxl
import pandas as pd
from tkinter import filedialog


""" модуль: работа с файлами"""


# Переменные для записи данных
sheet_name_open = str('БД (5)')
sheet_name_write = str('Реестр')


def open_read_files():
    # Открываем файл чтения
    ORF = filedialog.askopenfilename()
    print('Открываем файл чтения', ORF)
    return ORF


def open_file_write():
    # Открываем файл записи
    OFW = filedialog.askopenfilename()
    print('Открываем файл записи', OFW)
    return OFW


def read_files(ORF):
    # Читаем данные
    RF = ORF
    return RF


def open_book_write(OFW):
    # Открываем книгу для записи данных
    path_file_write_excel = OFW
    workbook = openpyxl.load_workbook(path_file_write_excel)
    return workbook


def reading_data(RF):
    # читаем лист
    df = pd.read_excel(RF, sheet_name=sheet_name_open)
    return df


def open_list_write(workbook):
    # выбираем лист, в который будем записывать значения
    worksheet = workbook[sheet_name_write]
    return worksheet


def show_sheet(sheet_name, root):
    # Функция, которая будет вызываться при нажатии на кнопку листа
    print(f"Имя выбранного листа: {sheet_name}")
    root.destroy()
    return sheet_name