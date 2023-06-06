import pandas as pd
import openpyxl
import itertools
# list_workbook = print(input('Лист книги'))


def read_book():
    # Читаем данные
    path_file_read_and_write_excel = '/Users/gregoryreyn/Desktop/Общая БД.xlsm'
    df = pd.read_excel(path_file_read_and_write_excel, sheet_name='БД (3)')

read_book()


def open_save_worbook():
    # открываем книгу для записи данных
    path_file_write_excel = '/Users/gregoryreyn/Documents/Developer/ProjectPTO/Auto_reestr_excel_v1/Реестр ИД.xlsx'
    workbook = openpyxl.load_workbook(path_file_write_excel)
    # выбираем лист, в который будем записывать значения
    worksheet = workbook['1']


open_save_worbook()


def save_worbook():
    workbook_save = workbook.save('Реестр ИД.xlsx')


save_worbook()


def save_worbook():
    Namber_Acts, Data_Acts, Named_work, IS, materials = [], [], [], [], []


save_worbook()
