def isPrime_On(n):
    d = 2
    while n % d != 0:
        d += 1
    return d == n

a = [i for i in range(2,2000001)]

def result(list_number):
    num_Prime = []
    for i in list_number:
        if isPrime_On(i):
            num_Prime.append(i)
    return sum(num_Prime)


if __name__ == '__main__':
    # print(isPrime_On(37))
    print(result(a))