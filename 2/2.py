def to_hex(num: int) -> str:
    alphabet = '0123456789ABCDEF'
    result = ''
    while num != 0:
        index = num % 16
        num //= 16
        result = alphabet[index] + result
    return result

user_num = int(input('Введите целое неотрицательное число: '))

print(to_hex(user_num))

print((hex(user_num)))