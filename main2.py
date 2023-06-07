import pandas as pd

# import openpyxl
# import itertools

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
    # генерируем схемы (разделяем схемы)
    my_list1 = ['устройство']
    finel_IS = []
    for item in my_list1:
        split_str = item.split(";")
        finel_IS += [x.strip() for x in split_str]
    # Вывод проверки
    print(finel_IS)





# path_file()
# reading_data()
# parsing_data()
# act_gen()
is_gen()
