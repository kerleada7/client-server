"""
3. ЗАДАНИЕ НА ЗАКРЕПЛЕНИЕ ЗНАНИЙ ПО МОДУЛЮ YAML.
 НАПИСАТЬ СКРИПТ, АВТОМАТИЗИРУЮЩИЙ СОХРАНЕНИЕ ДАННЫХ
 В ФАЙЛЕ YAML-ФОРМАТА.
"""
import yaml

DATA = {
    'items': ['computer', 'printer', 'keyboard', 'mouse'],
    'items_quantity': 4,
    'items_price': {
        'computer': '200€-1000€',
        'keyboard': '5€-50€',
        'mouse': '4€-7€',
        'printer': '100€-300€'
    },
}

with open('file_test.yaml', 'w', encoding='utf-8') as f:
    yaml.dump(DATA, f, default_flow_style=False, allow_unicode=True)

with open('file_test.yaml', encoding='utf-8') as f:
    yaml_content = yaml.safe_load(f)

print(yaml_content == DATA)