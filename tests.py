# # class Animal:
# #     def __init__(self, voice):
# #         self.voice = voice
# #
# #
# # cat = Animal('Meow')
# # print(cat.voice)  # => Meow
# #
# # dog = Animal('Woof')
# # print(dog.voice)  # => Woof
#
#
# def get_input():
#     """This function prompts the user for input and returns it"""
#     user_input = input("Enter a value: ")
#     return user_input
#
#
# def convert_to_int(user_input):
#     """This function takes a string as input and converts it to an integer"""
#     num = int(user_input)
#     return num
#
#
# def apply_operation(num):
#     """This function takes an integer as input and applies an operation (e.g. multiplying by 2)"""
#     result = num * 2
#     return result
#
#
# def convert_to_str(result):
#     """This function takes an integer as input and converts it to a string"""
#     string = str(result)
#     return string
#
#
# def print_output(string):
#     """This function takes a string as input and prints it to the console"""
#     print("The result is:", string)
#
#
# def main():
#     """This function is the main function that calls other functions"""
#     user_input = get_input()
#     num = convert_to_int(user_input)
#     result = apply_operation(num)
#     string = convert_to_str(result)
#     print_output(string)
#
#
# # Call the main function to run the program
# main()


import pandas as pd
import openpyxl
import itertools
finel_act = '1'
finel_IS = '2'
materials = '3'
finel_data_acts = '4'
finel_osi_otm = '5'


# открываем книгу для записи данных
path_file_write_excel = '/Users/gregoryreyn/Desktop/тест книга.xlsx'  # заменить на выбор
workbook = openpyxl.load_workbook(path_file_write_excel)
# выбираем лист, в который будем записывать значения
worksheet = workbook['Лист2']  # заменить на выбор


# записываем каждое значение из списка в ячейку
starting_row = 12  # определяем ячейку, с которой начнём записывать значения
starting_column = 3
# заполняем пропущенные значения значением "-"
for write_finel_act, write_finel_IS, write_finel_materials, write_finel_data_acts, write_finel_osi_otm in itertools.zip_longest(
        finel_act, finel_IS, materials, finel_data_acts, finel_osi_otm, fillvalue="-"):
    worksheet.cell(row=starting_row, column=starting_column, value=write_finel_act)
    worksheet.cell(row=starting_row, column=starting_column + 1, value=write_finel_osi_otm)
    worksheet.cell(row=starting_row, column=starting_column + 2, value=write_finel_data_acts)
    worksheet.cell(row=starting_row + 1, column=starting_column, value=write_finel_IS)
    worksheet.cell(row=starting_row + 2, column=starting_column, value=write_finel_materials)
    starting_row += 3
