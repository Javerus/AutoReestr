import pandas as pd

# Читаем данные
path_file_read_and_write_excel = '/Users/gregoryreyn/Desktop/Общая БД.xlsm'
df = pd.read_excel(path_file_read_and_write_excel, sheet_name='БД')


class Piszdec:
    @staticmethod
    def parse_data():
        psp_list = ['afeds', 'ergf', 'ehdfb', 'ufymgh', 'saDFD']
        print('parse_data', psp_list)
        return psp_list

    # parse_data()

    def blya(self):
        view_1 = self.parse_data()
        print('blya print', view_1)
        return view_1


print(Piszdec.blya())
