print('введите два числа: ')
num_1 = int(input())
num_2 = int(input())
if num_1 % num_2 == 0:
    print(f'''{num_1} делится на {num_2} нацело
    частное: {int(num_1 / num_2)}''')
else:
    print(f'''{num_1} не делится на {num_2} нацело
    неполное частное: {int(num_1 / num_2)}
    остаток: {num_1 % num_2}''')
# maksimpetrov@MacBook-Pro-Maksim 2023.07.14 % python3 2.py
# введите два числа:
# 10
# 3
# 10 не делится на 3 нацело
#     неполное частное: 3
#     остаток: 1
# maksimpetrov@MacBook-Pro-Maksim 2023.07.14 % python3 2.py
# введите два числа:
# 8
# 2
# 8 делится на 2 нацело
#     частное: 4
