"""
Простые делители числа 13195 - это 5, 7, 13 и 29.

Каков самый большой делитель числа 600851475143, являющийся простым числом?
"""

def isPrime(a):
    d = 2
    while a % d != 0:
        d += 1
    return d == a

i = 2
while i < 600851475143:
    d = 2
    a = 600851475143 % i
    if a == 0:
        if isPrime(i) == True:
            print(i)
    i += 1



# num = 600851475143
# div = []
#
# for i in range(2, num):
#     if (num % i == 0):
#         div = num / i
#         print(div) #=> 84626is96833.0