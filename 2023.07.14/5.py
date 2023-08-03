letters = ['a','b','c','d','e','f','g','h']
letter_1, letter_2 = input(''),input('')

# УДАЛИТЬ: избыточные действия в контексте данной задачи
x_1, y_1 = int(letters.index(letter_1[0])), int(letter_1[1])
x_2, y_2 = int(letters.index(letter_2[0])), int(letter_2[1])

if x_1 == x_2 or y_1 == y_2:
    print('результат: да')
else:
    print('результат: нет')


# d4
# e4
# результат: да

# a2
# c4
# результат: нет


# ИТОГ: можно проще — 2/3
