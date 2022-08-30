'''Возвращает простое число'''
def isPrime_On(n):
    d = 2
    while n % d != 0:
        d += 1
    return d == n

def isPrime_O_sqr_n(n):
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return d * d > n

def isPrime_O_sqr_n_2(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n

if __name__ == '__main__':
    # print(isPrime_On(37))
    print(isPrime_O_sqr_n(9))
    # # print(isPrime_O_sqr_n_2(37))