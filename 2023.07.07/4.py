num = int(input('Введите трёхзначное число: '))
third = num % 10
second = int(num / 10 % 10)
first = int(num / 100 % 10)
print(f"""Сумма цифр = {first+second+third}
Произведение цифр = {first*second*third}""")
# maksimpetrov@MacBook-Pro-Maksim 2023.07.07 % python3 4.py
# Введите трёхзначное число: 333
# Сумма цифр = 9
# Произведение цифр = 27
