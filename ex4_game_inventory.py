
items_dict = {'М4А4': 4.5,
          'AK-47': 3.5,
          'usp': 1.2,
          'glock': 1.2,
          'Galil': 1.3,
          'P-250': 1.5,
          'Deagle': 1.6,
          'Negev': 10,
          'P-2000': 2}
inventary_dict = dict()
command_info = '''Введи команду:
0 - Вывести список доступных предметов на добавление/удаление
1 - Добавить в инвентарь предмет
2 - Удалить предмет из инвентаря
3 - Посмотреть инвентарь и узнать общий вес
4 - Выход из программы
'''
max_weight = 10

def print_dict(dict):
    for key in dict:
        print(key, '->', dict[key])
    print()

while True:
    s = input(command_info)
    match s:
        case '0':
            print('Доступные предметы: ')
            print_dict(items_dict)

        case '1':
            item = input('Что добавляем? cancel - отмена. Название: ')
            while not item in items_dict:
                if item == 'cancel':
                    break
                item = input('\nНет такой вещи. cancel - отмена. Попробуй ещё раз: ')
            if (item != 'cancel'):
                if (sum(inventary_dict.values()) + items_dict.get(item) <= max_weight):
                    inventary_dict[item] = items_dict[item]
                    print('Успешно!')
                else:
                    print('Инвентарь переполнен.')

        case '2':
            item = input('Что удаляем? cancel - отмена. Название: ')
            while not item in items_dict:
                if item == 'cancel':
                    break
                item = input('\nНет такой вещи. cancel - отмена. Попробуй ещё раз: ')
            if item != 'cancel':
                if item in inventary_dict:
                    del inventary_dict[item]
                    print('Успешно!')
                else:
                    print('Предмета нет.')

        case '3':
            print('Текущий инвентарь: ')
            print_dict(inventary_dict)
            print(f'Вес инвентаря: {sum(inventary_dict.values())}')
            
        case '4':
            print('До свидания!')
            break
        case _:
            print('Неправильный ввод!')