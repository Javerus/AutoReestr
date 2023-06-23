class test:
    def test1_1(self, materials_list):
        # Проверка
        materials_list = ['устройство; устройство2; устройство3; устройство4']
        # генерируем паспорта/сертификаты (разделяем паспорта/сертификаты)
        finel_materials = []
        for item in materials_list:
            split_str = item.split(";")
            finel_materials += [x.strip() for x in split_str]
        # Вывод проверки
        print(finel_materials)

edfs = input('sfdv')
test.test1_1(edfs)
