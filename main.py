import pandas as pd
import openpyxl
import itertools
# list_workbook = print(input('Лист книги'))


# Читаем данные
path_file_read_and_write_excel = '/Users/gregoryreyn/Desktop/Общая БД.xlsm'
df = pd.read_excel(path_file_read_and_write_excel, sheet_name='БД (3)')

# # Открыть и активировать книгу
# workbook = openpyxl.load_workbook(path_file_read_and_write_excel)
# workbook_active = workbook.active

# открываем книгу для записи данных
path_file_write_excel = '/Users/gregoryreyn/Documents/Developer/ProjectPTO/Auto_reestr_excel_v1/Реестр ИД.xlsx'
workbook = openpyxl.load_workbook(path_file_write_excel)
# выбираем лист, в который будем записывать значения
worksheet = workbook['1']


# Переменные для записи данных
Namber_Acts, Data_Acts, Named_work, IS, materials = [], [], [], [], []

# парсим и записываем данные в переменные
for index, row in df.iterrows():
    Namber_Acts.append(row['№ акта'])
    Data_Acts.append(row['дата акта'])
    Named_work.append(row['1. К освидетельствованию предъявлены следующие работы:'])
    IS.append(row['4. Предъявлены документы'])
    materials.append(row['3. При выполнении работ применены:'])


# def act_generation(aosr, act_namber, act_name_work):
# генерируем акты
aosr, act_namber, act_name_work = 'АОСР', Namber_Acts, Named_work
finel_act = []
for i in range(len(act_name_work)):
    finel_act.append(f"{aosr} {act_namber[i]} {act_name_work[i]}")
# act_generation(aosr, act_namber, act_name_work)

# генерируем схемы (разделяем схемы)
my_list1 = IS

finel_IS = []

for item in my_list1:
    split_str = item.split(";")
    finel_IS += [x.strip() for x in split_str]


# генерируем паспорта/сертификаты (разделяем паспорта/сертификаты)
# materials_list = materials
#
# finel_materials = [materials]

# for item in materials_list:
#     split_str = item.split(";")
#     finel_materials += [x.strip() for x in split_str]


finel_osi_otm = [] # новый список, куда будут записываться значения
for item in finel_act:
    if "в осях" in item:
        new_item = item.split("в осях", 1)[1].strip()
        finel_osi_otm.append("в осях " + new_item)

# print(finel_osi_otm) # вывод нового списка


# записываем каждое значение из списка в ячейку
starting_row = 12 # определяем ячейку, с которой начнём записывать значения
starting_column = 3

# for write_finel_act, write_finel_IS, write_finel_materials, write_data_Acts in zip(finel_act, finel_IS, materials, Data_Acts):  # проходимся каждым из 4 значений по каждому списку в кол-ве 4
#     worksheet.cell(row=starting_row, column=starting_column, value=write_finel_act)  # Определяем стартовые точки строки, столбца, значения данных и для колонн делаем оттуп на 1 больше предыдущего
#     # worksheet.cell(row=starting_row, column=starting_column + 1, value=write_finel_osi_otm)
#     worksheet.cell(row=starting_row, column=starting_column + 2, value=write_data_Acts)
#     worksheet.cell(row=starting_row + 1, column=starting_column, value=write_finel_IS)
#     worksheet.cell(row=starting_row + 2, column=starting_column, value=write_finel_materials)
#     starting_row += 3  # с помощью оператора += как раз таки происходит цикл, но пока хз как. Не понятно...



# заполняем пропущенные значения в Data_Acts значением "-1"
for write_finel_act, write_finel_IS, write_finel_materials, write_data_Acts, write_finel_osi_otm in itertools.zip_longest(finel_act, finel_IS, materials, Data_Acts, finel_osi_otm, fillvalue=""):
    worksheet.cell(row=starting_row, column=starting_column, value=write_finel_act)
    worksheet.cell(row=starting_row, column=starting_column + 1, value=write_finel_osi_otm)
    worksheet.cell(row=starting_row, column=starting_column + 2, value=write_data_Acts)
    worksheet.cell(row=starting_row + 1, column=starting_column, value=write_finel_IS)
    worksheet.cell(row=starting_row + 2, column=starting_column, value=write_finel_materials)
    starting_row += 3



workbook_save = workbook.save('Реестр ИД.xlsx')

# print(Named_work)
# проверяем написанную херню
# path_file_excel11 = '/Users/gregoryreyn/Documents/Developer/ProjectPTO/Auto_reestr_excel_v1/Реестр ИД.xlsx'
# df1 = pd.read_excel(path_file_excel11, sheet_name='1')
# print(df1)

print(finel_act)
print()
print(finel_IS)
print()
print(materials)
print()
print(finel_osi_otm)
print()
print(Data_Acts)
