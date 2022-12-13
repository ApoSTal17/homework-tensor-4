from random import randint

len1 = randint(5, 20)
len2 = randint(5, 20)
set1 = {randint(1, 30) for i in range(len1)}
set2 = {randint(1, 30) for i in range(len2)}
print(f'Два случайных набора набора чисел: \n1) {set1} \n2) {set2}')

print(f'''Элементы, которые входят: 
1. Одновременно в оба набора {set1.intersection(set2)}
2. Только в первый набор, но не входят во второй {set1.difference(set2)}
3. Только во второй набор, но не входят в первый {set2.difference(set1)}
4. Только в первый и второй, но не в оба одновременно {set1.symmetric_difference(set2)}''')