print('Введите три числа:')
num_1,num_2,num_3 = float(input('')),float(input('')),float(input(''))
num = [num_1,num_2,num_3]
positive = []
count = 0
while count < len(num):
    if num[count] > 0:
        positive.append(num[count])
        count+=1
    else:
        count+=1
if len(positive) == 0:
    print('все цифры отрицательные')
if len(positive) == 1:
    print(f'Сумма = {positive[0]}')
if len(positive) == 2:
    print(f'Сумма = {positive[0] + positive[1]}')
if len(positive) == 3:
    print(f'Сумма = {positive[0] + positive[1] + positive[2]}')

# maksimpetrov@MacBook-Pro-Maksim 2023.07.14 % python3 1.py
# Введите три числа:
# 3
# 1.5
# -6
# Сумма = 4.5
