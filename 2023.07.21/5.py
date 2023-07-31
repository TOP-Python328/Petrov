text = input('Текст: ')
letters = [letter for letter in text if letter != ' ']

price = str(len(letters) * 30)
print(f'{price[:-2] or 0} руб. {price[-2:]} коп.')


# ➜  2023.07.21 git:(main) ✗ python3 5.py
# Текст: грузите апельсины бочках братья карамазовы
# 1140
# 11 руб. 40 коп
