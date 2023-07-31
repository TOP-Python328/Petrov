n = int(input('введите число: '))

def Divider(num):
    '''Функция возвращает гениратор из делителей числа num'''
    for i in range(1, int(num / 2 + 1)):
        if num % i == 0:
            yield i
        yield num

print(f'Cумма делителей числа {n}: {sum(set(Divider(n)))}')
#➜  2023.07.21 git:(main) ✗ python3 3.py
#введите число: 5
#Cумма делителей числа 5: 6
#➜  2023.07.21 git:(main) ✗ python3 3.py
#введите число: 25
#Cумма делителей числа 25: 31
