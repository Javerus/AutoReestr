list1 = [
    'Документы о качестве бетонной смеси БСТ В12,5 П4 F/00 W6: №186., №1866., №/859., №1865 от 17.08.2022г. № 11478 от 18.08.2022г; Декларацuя о соответствии №РОСС RU Д-RU. HA45.B.00762/22 срок действuя по 12.01.2023г; Декларация о соответствии № РОСС RU Д-RU.PAO1.B.10095/22 срок действuя по 21.03.2025г.']
list2 = [
    'Документы о качестве бетонной смеси БСТ В12,5 П4 F/00 W6: №186., №1866., №/859., №1865 от 17.08.2022г. № 11478 от 18.08.2022г',
    'Декларацuя о соответствии №РОСС RU Д-RU. HA45.B.00762/22 срок действuя по 12.01.2023г',
    'Декларация о соответствии № РОСС RU Д-RU.PAO1.B.10095/22 срок действuя по 21.03.2025г.']
list3 = []


#
#
# def materials_gen():
#     # генерируем паспорта/сертификаты (разделяем паспорта/сертификаты)
#     materials_list = materials
#     finel_materials = []
#     for item in materials_list:
#         split_str = item.split(";")
#         finel_materials += [x.strip() for x in split_str]
#     print(finel_materials)
#
#
# materials_gen()

def merge_lists(list_1, list_2):
    # Удаляем пробелы в начале и конце каждого элемента списка
    list_1 = [elem.strip() for elem in list_1]
    # Записываем элементы из второго списка по очереди
    merged_list = []
    for index in range(len(list_1)):
        if list_1[index] in list_2[0]:
            merged_list.append(list_2[0].pop(0))
        else:
            merged_list.append("")

    print(merged_list)


merge_lists(list1, list2)


# def maim():
#     merge_lists(list1, list2)
#
#
# maim()