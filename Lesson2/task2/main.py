"""
2. Задание на закрепление знаний по модулю json. Есть файл orders
в формате JSON с информацией о заказах. Написать скрипт, автоматизирующий
его заполнение данными.
"""
import json


def write_order_to_json(item, quantity, price, buyer, date):
    with open('orders_test.json') as f:
        json_obj = json.load(f)

    new_order = {
        'item': item,
        'quantity': quantity,
        'price': price,
        'buyer': buyer,
        'date': date
    }
    json_obj['orders'].append(new_order)

    with open('orders_test.json', 'w', encoding='utf-8') as f:
        json.dump(json_obj, f, indent=4)


write_order_to_json('принтер', 10, 6700, 'Ivanov I.I.', '24.09.2017')
write_order_to_json('scaner', 20, 10000, 'Petrov P.P.', '11.01.2018')
write_order_to_json('computer', 5, 40000, 'Petrov P.S.', '2.05.2019')
write_order_to_json('принтер', 10, 6700, 'Ivanov I.S.', '24.03.2034')
