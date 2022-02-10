import csv
import re
from os import listdir


def get_data():
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    main_data = [['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']]
    for file in listdir():
        if file.startswith('info_') and file.endswith('.txt'):
            with open(file) as f:
                file_content = f.read()
                os_prod_list.append(*re.search(r'Изготовитель системы:\s*(.*)', file_content).groups())
                os_name_list.append(*re.search(r'Название ОС:\s*(.*)', file_content).groups())
                os_code_list.append(*re.search(r'Код продукта:\s*(.*)', file_content).groups())
                os_type_list.append(*re.search(r'Тип системы:\s*(.*)', file_content).groups())
    for i in range(len(os_prod_list)):
        main_data.append([])
        main_data[i + 1].append(os_prod_list[i])
        main_data[i + 1].append(os_name_list[i])
        main_data[i + 1].append(os_code_list[i])
        main_data[i + 1].append(os_type_list[i])
    return main_data


def write_to_csv(file_name):
    with open(file_name, 'w', encoding='utf-8') as f:
        csv.writer(f).writerows(get_data())


write_to_csv('data_report.csv')