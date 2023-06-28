import pandas as pd
import openpyxl
from tkinter import filedialog


def open_read_files():
    # Открываем файл чтения
    file_path_o = filedialog.askopenfilename()
    print(file_path_o)
    return file_path_o


def open_file_write():
    # Открываем файл записи
    file_path_w = filedialog.askopenfilename()
    print(file_path_w)
    return file_path_w


def read_files(file_path_o):
    # Читаем данные
    path_file_read_and_write_excel = file_path_o
    return path_file_read_and_write_excel


def open_book_write(file_path_w):
    # открываем книгу для записи данных
    path_file_write_excel = file_path_w
    workbook = openpyxl.load_workbook(path_file_write_excel)
    return workbook


def reading_data(path_file_read_and_write_excel):
    # читаем лист
    df = pd.read_excel(path_file_read_and_write_excel, sheet_name='БД (4)')
    return df


def open_list_write(workbook):
    # выбираем лист, в который будем записывать значения
    worksheet = workbook['Реестр']
    return worksheet

