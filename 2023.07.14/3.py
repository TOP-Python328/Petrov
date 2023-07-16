print('Введите год:')
year = int(input())
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print('да')
else:
    print('нет')

# maksimpetrov@MacBook-Pro-Maksim 2023.07.14 % python3 3.py
# Введите год:
# 1997
# нет
# maksimpetrov@MacBook-Pro-Maksim 2023.07.14 % python3 3.py
# Введите год:
# 2024
# да
