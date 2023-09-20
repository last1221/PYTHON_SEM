balance = 0
count = 0


def rich():
    global balance
    wealth_tax = balance / 100 * 10
    balance -= wealth_tax
    return print(f'У вас вычтен налог за богатство:{wealth_tax}  ')

def Pw3o():
    global balance
    global count
    pw3o = balance / 100 * 3
    balance += pw3o
    count = 0
    return print(f'Поздравляем вам начислен процент за активное пользование нашим банкоматом.'
                 f'Он составил: {pw3o} и теперь ваш баланс составляет: {balance}')



def withdrawal():
    global balance
    global count
    min_t = 30
    max_t = 600
    sum_w = int(input('Введите сумму для снятия (кратную 50): '))
    if sum_w % 50 != 0:
        print('Сумма не кратна 50(')
    if sum_w > balance:
        return print('Вы не можете снять столько денег')
    else:
        balance -= sum_w

    pfw = sum_w / 100 * 1.5

    if pfw < min_t:
        pfw = min_t
    if pfw > max_t:
        pfw = max_t
    balance -= pfw
    count += 1
    return print(f'Ваш баланс после операции: {balance}, списанный процент за операцию: {pfw} ')



def replenishment():
    global balance
    global count
    sum_r = int(input('Введите сумму для пополнения (кратную 50): '))
    if sum_r % 50 != 0:
        print('Сумма не кратна 50(')
    balance += sum_r
    count += 1
    return print(f'Вы внесли на баланс: {sum_r}, теперь он составляет {balance}')


def menu():

    global balance
    global count

    while True:
        print(f'Текущий баланс: {balance}' )
        print('Выберите действие')
        print('1. Пополнить')
        print('2. Снять')
        print('3. Выйти')
        choise = int(input('Введите номер действия: '))
        if choise == 3:
            return print('Всего доброго')
        if choise == 2:
            cash_withdrawal = withdrawal()
        if choise == 1:
            cash_replenishment = replenishment()
        if count == 3:
            cash_pw3o = Pw3o()
        if balance > 5000000:
            cash_rich = rich()







menu()