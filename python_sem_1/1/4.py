# 4. Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
# должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
# числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)
from random import randint
num = randint(0, 1000)
attempt = 10

while attempt > 0:
    number = int(input('Введите число от 0 до 1000: '))
    if number == num:
        print('Вы угадали число!')
    elif number > num:
        print('Ваше число больше загаданного(')
    elif number < num:
        print('Ваше число меньше загаданного(')
    attempt -= 1
else:
    print('Конец игры')