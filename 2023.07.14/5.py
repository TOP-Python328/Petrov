letters = ['a','b','c','d','e','f','g','h']
letter_1, letter_2 = input(''),input('')
x_1, y_1 = int(letters.index(letter_1[0])), int(letter_1[1])
x_2, y_2 = int(letters.index(letter_2[0])), int(letter_2[1])
if x_1 == x_2 or y_1 == y_2:
    print('результат: да')
else:
    print('результат: нет')


# maksimpetrov@MacBook-Pro-Maksim 2023.07.14 % python3 5.py
# d4
# e4
# результат: да
# maksimpetrov@MacBook-Pro-Maksim 2023.07.14 % python3 5.py
# a2
# c4
# результат: нет
