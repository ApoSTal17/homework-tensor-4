color_dictionary = {'Red': (255, 0, 0),
                    'Orange': (255, 165, 0),
                    'Yellow': (255, 255, 0),
                    'Green': (0, 128, 0),
                    'Light Blue': (255, 255, 255),
                    'Blue': (173, 216, 230),
                    'Purple': (128, 0, 128)}
print('Словарь вида "имя цвета" (ключ) -> "RGB tuple" (значение):')

for key in color_dictionary:
    print(key, '->', color_dictionary[key])