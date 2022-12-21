from random import randint

s = input('Введите длину массива целое n: ')
while not s.isdigit():
    print('Неправильный ввод.\n')
    s = input('Введите длину массива целое n: ')
length = int(s)

a = [randint(-100,100) for i in range(length)]
print(f'Исходный несортированный массив: {a}\n')

ascending_a = a.copy()
for i in range(length - 1):
    for j in range(length - i - 1):
        if ascending_a[j] > ascending_a[j+1]:
            ascending_a[j], ascending_a[j+1] = ascending_a[j+1], ascending_a[j]
print(f'Сортированный по возрастанию массив: {ascending_a}\n')

descending_a = a.copy()
for i in range(length - 1):
    for j in range(length - i - 1):
        if descending_a[j] < descending_a[j+1]:
            descending_a[j], descending_a[j+1] = descending_a[j+1], descending_a[j]
print(f'Сортированный по убыванию массив: {descending_a}\n')