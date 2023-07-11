min = int(input('Минуты: '))
hour = int(min / 60)
print(f'{min} мин - это {hour} час(а) {int((min / 60 - hour) * 60)} мин')
# maksimpetrov@MacBook-Pro-Maksim 2023.07.07 % python3 3.py
# Минуты: 150
# 150 мин - это 2 час(а) 30 мин
