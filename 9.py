'''
пример чисел для вставки 2⁰, 2¹, 2², 2³, 2⁴, 2⁵, 2⁶, 2⁷, 2⁸, 2⁹.
Тройка Пифагора - три натуральных числа a < b < c, для которых выполняется равенство

a² + b² = c²
Например, 3² + 4² = 9 + 16 = 25 = 5².

Существует только одна тройка Пифагора, для которой a + b + c = 1000.
Найдите произведение abc.
'''

def compute():
    PERIMETER = 1000
    for a in range(1, PERIMETER + 1):
        for b in range(a + 1, PERIMETER + 1):
            c = PERIMETER - a - b
            if a * a + b * b == c * c:
                return str(a * b * c)
if __name__ == "__main__":
    print(compute())

