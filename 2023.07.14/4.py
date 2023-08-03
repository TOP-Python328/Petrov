# КОММЕНТАРИЙ: можно было использовать объект str, а не list — метод index() есть у всех последовательностей
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
letter_1, letter_2 = input(''), input('')
# ИСПРАВИТЬ: метод index() всегда возвращает int объект — преобразование избыточно
x_1, y_1 = int(letters.index(letter_1[0])), int(letter_1[1])
x_2, y_2 = int(letters.index(letter_2[0])), int(letter_2[1])
# ИСПРАВИТЬ: проанализируйте сумму чётных и нечётных чисел и упростите логическое выражение
if (x_1 + y_1) % 2 == 0 and (x_2 + y_2) % 2 == 0 or (x_1 + y_1) % 2 != 0 and (x_2 + y_2) % 2 != 0:
    print('результат: да')
else:
    print('результат: нет')


# a1
# b2
# результат: да

# a1
# b1
# результат: нет


# ИТОГ: хорошо, но можно ещё лучше — 4/6


# КОММЕНТАРИЙ: моделирование шахматной доски: https://disk.yandex.ru/i/m-krUt3xbY8Y7g
