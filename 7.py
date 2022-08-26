'''
Выписав первые шесть простых чисел, получим 2, 3, 5, 7, 11 и 13. Очевидно, что 6-е простое число - 13.

Какое число является 10001-м простым числом?
'''

def EratosfenNaiv(num):
    out = []
    for i in range(2, num+1):
        '''заполняем массив числами от 2 до num'''
        out.append(i)
    i = 0

    while i < len(out):
        j = i + 1
        while j < len(out):
            aa = out[j]
            ss = out[i]
            if aa % ss == 0:
                '''если числа делятся без остатка то извлекаем их из массива'''
                out.pop(j)
            j += 1
        i += 1
    return out



# def Eratos(num):
#     out = []
#
#     for i in range(num+1):
#         out.append(True)
#
#     for i in range(2, len(out)):
#         if not out[i]: continue
#         for j in range(2*i, len(out), i):
#             out[j] = False
#     print(out)
#     result = []
#
#     for i in range(2, len(out)):
#         if out[i]:
#             result.append(i)
#
#     return result
#
# print(Eratos(1000))

if __name__ == "__main__":
    print(EratosfenNaiv(30))
'''
10001 104743 True

real    0m31.605s
user    0m31.592s
sys     0m0.009s
'''