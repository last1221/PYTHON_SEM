# 3. Напишите код, который запрашивает число и сообщает является ли оно простым или составным. Используйте правило для
# проверки: “Число является простым, если делится нацело только на единицу и на себя”. Сделайте ограничение на ввод
# отрицательных чисел и чисел больше 100 тысяч.
def prime_number(number):
    count = 0
    for i in range(1, number+1):
        if number % i == 0:
            count+=1
    if count == 2:
        return True

flag = True

while flag:
    num = int(input('Введите число от 1 до 100000: '))
    if 100000 > num > 0:
        flag = False
    else:
        print('Вы ввели неверное число(')
if prime_number(num):
    print('Число простое')
else:
    print('Число составное')


