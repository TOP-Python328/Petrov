whole = int(input('Введите целую часть: '))
fraction = int(input('Введите дробную часть: '))
distance = whole + (fraction / 10)
mile = 1.61

print(f'{distance} миль = {distance * mile:.1f} км')
# maksimpetrov@MacBook-Pro-Maksim 2023.07.07 % python3 5.py
# Введите целую часть: 15
# Введите дробную часть: 7
# 15.7 миль = 25.3 км
