n = int(input('Натуральное число: '))
sumPositiv = list()
for i in range(n):
    num = int(input('> '))
    if num > 0:
        sumPositiv.append(num)
print(sum(sumPositiv))

#➜  2023.07.21 git:(main) ✗ python3 2.py
#Натуральное число: 5
#> 1
#> 4
#> 5
#> -6
#> -10
#10
