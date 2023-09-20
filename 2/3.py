from math import gcd


Fraction = tuple[int, int]

def reduce(fract: Fraction) -> Fraction:
    div = gcd(*fract)
    return fract[0] // div, fract[1] // div


def summ(a: Fraction, b: Fraction) -> Fraction:
    if a[1] == b[1]:
        return reduce((a[0] + b[0], b[1]))
    return reduce(((a[0] * b[1]) + (b[0] * a[1]), a[1] * b[1]))

def mult(a: Fraction, b: Fraction) -> Fraction:
    return reduce((a[0] * b[0], a[1] * b[1]))

user_fract1 = input('дробь вида “a/b”: ').split('/')
user_fract2 = input('дробь вида “a/b”: ').split('/')

fract1 = tuple([int(num) for num in user_fract1])
fract2 = tuple([int(num) for num in user_fract2])

print(summ(fract1, fract2), mult(fract1, fract2))