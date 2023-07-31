numbers = list()
while True:
    num = int(input('Введите число, кратное 7: '))
    if num % 7:
        break
    else:
        numbers.insert(0, num)
print(*numbers)

#➜  2023.07.21 git:(main) ✗ python3 1.py
#Введите число, кратное 7: 7
#Введите число, кратное 7: 21
#Введите число, кратное 7: 14
#Введите число, кратное 7: 23
#14 21 7
