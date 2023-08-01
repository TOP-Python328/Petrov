ticket = input('ticket nubmer: ')
print('yes' if sum([int(n) for n in ticket[:3]]) == sum([int(n) for n in ticket[3:]]) else 'no')

# ➜  2023.07.21 git:(main) ✗ python3 6.py
# ticket nubmer: 123321
# yes
# ➜  2023.07.21 git:(main) ✗ python3 6.py
# ticket nubmer: 123456
# no
