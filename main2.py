import pandas as pd
import openpyxl
import itertools

# Переменные для записи данных
Namber_Acts, Data_Acts, Named_work, IS, materials = [], [], [], [], []
finel_act, finel_IS, finel_osi_otm = [], [], []


def path_file():
    path = input('puth: ')
    return path


def reading_data():
    # /Users/gregoryreyn/Documents/Developer/Общая БД.xlsm
    path_file_read_and_write_excel = path_file()
    df = pd.read_excel(path_file_read_and_write_excel, sheet_name='БД (3)')
    print(df)


def parsing_data():
    # Проверка
    path_file_read_and_write_excel = path_file()
    df = pd.read_excel(path_file_read_and_write_excel, sheet_name='БД (3)')
    print(df)
    # парсим и записываем данные в переменные
    for index, row in df.iterrows():
        Namber_Acts.append(row['№ акта'])
        Data_Acts.append(row['дата акта'])
        Named_work.append(row['1. К освидетельствованию предъявлены следующие работы:'])
        IS.append(row['4. Предъявлены документы'])
        materials.append(row['3. При выполнении работ применены:'])
    print(Namber_Acts, Data_Acts, Named_work, IS, materials)


def act_gen():
    # Проверка
    Namber_Acts = ['№0']
    Named_work = ['устройство']
    # генерируем акты
    aosr, act_namber, act_name_work = 'АОСР', Namber_Acts, Named_work
    for i in range(len(act_name_work)):
        finel_act.append(f"{aosr} {act_namber[i]} {act_name_work[i]}")
    # Вывод проверки
    print(finel_act)



def is_gen():
    # Проверка
    my_list1 = ['устройство']
    # генерируем схемы (разделяем схемы)
    finel_IS = []
    for item in my_list1:
        split_str = item.split(";")
        finel_IS += [x.strip() for x in split_str]
    # Вывод проверки
    print(finel_IS)


def materials_gen():
    # Проверка
    materials_list = ['устройство; устройство2; устройство3; устройство4']
    # генерируем паспорта/сертификаты (разделяем паспорта/сертификаты)
    finel_materials = []
    for item in materials_list:
        split_str = item.split(";")
        finel_materials += [x.strip() for x in split_str]
    # Вывод проверки
    print(finel_materials)


def osi_gen():
    finel_osi_otm = []  # новый список, куда будут записываться значения
    for item in finel_act:
        if "в осях" in item:
            new_item = item.split("в осях", 1)[1].strip()
            finel_osi_otm.append("в осях " + new_item)

    print(finel_osi_otm) # вывод нового списка

def all_write():
    finel_act, finel_IS, finel_osi_otm, Data_Acts, materials = [], [], [], ['1', '2', '3', '4', '5', ], []

    # открываем книгу для записи данных
    path_file_write_excel = '/Users/gregoryreyn/Documents/Developer/Общая БД.xlsm'
    workbook = openpyxl.load_workbook(path_file_write_excel)
    # выбираем лист, в который будем записывать значения
    worksheet = workbook['Реест']
    starting_row = 12  # определяем ячейку, с которой начнём записывать значения
    starting_column = 3

    # заполняем пропущенные значения в Data_Acts значением "-1"
    for write_finel_act, write_finel_IS, write_finel_materials, write_data_Acts, write_finel_osi_otm in itertools.zip_longest(
            finel_act, finel_IS, materials, Data_Acts, finel_osi_otm, fillvalue="none"):
        worksheet.cell(row=starting_row, column=starting_column, value=write_finel_act)
        worksheet.cell(row=starting_row, column=starting_column + 1, value=write_finel_osi_otm)
        worksheet.cell(row=starting_row, column=starting_column + 2, value=write_data_Acts)
        worksheet.cell(row=starting_row + 1, column=starting_column, value=write_finel_IS)
        worksheet.cell(row=starting_row + 2, column=starting_column, value=write_finel_materials)
        starting_row += 3





# path_file()
# reading_data()
# parsing_data()
# act_gen()
# is_gen()
# materials_gen()
all_write()
