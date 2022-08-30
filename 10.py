'''
Сумма простых чисел меньше 10 равна 2 + 3 + 5 + 7 = 17.

Найдите сумму всех простых чисел меньше двух миллионов.
'''

def isPrime_O_sqr_n_2(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n

def sum_isPrime(max_number):
    max = [i for i in range(max_number)]
    sum = 0
    for i in max:
        if isPrime_O_sqr_n_2(i):
            sum += i
    return sum -1




if __name__ == '__main__':
    print(sum_isPrime(2000000))
    # print([a for a in range(2000000)])


'''
isPrime_O_sqr_n
142913828922
real    0m20.673s
user    0m20.660s
sys     0m0.012s

isPrime_O_sqr_n_2
142913828922
real    0m12.447s
user    0m12.430s
sys     0m0.008s

'''