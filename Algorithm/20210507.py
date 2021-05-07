import math

# 소수 판별
def isPrime(num):
    for i in range(2, math.floor(math.sqrt(num))+1):
        if num % i == 0 :
            return False
    return True

# 소수 찾기
def findPrimes(n):
    primes = []
    for i in range(2, n+1):
        if isPrime(i):
            primes.append(i)
    return primes

print('소수 리스트', findPrimes(30))

# 소인수 분해 1
def factorize(n):
    factors = []
    primes = findPrimes(n)  # n의 소수 리스트를 추출
    for i in primes:
        while (n % i == 0):  # 소수 중 나누어 떨어지는(약수) 수를 찾는다
            factors.append(i)
            n = n // i
    return factors

print('소인수분해 결과', factorize(30))

# 효율적인 소인수 분해
def factorize2(n):
    factor = 2 #시작 소수 지정
    factors = []
    while (factor**2 <= n):  # 에라토스테네스를 떠올리며,, 즉 루트n까지 실행
        while (n % factor == 0):  # 소수로 나누어 떨어지면(= 즉 약수면)
            factors.append(factor)  # 리스트에 추가
            n = n // factor  # n을 몫으로 변경
        factor += 1
    if n > 1 : # 1보다 크고 factor**2(4)보다 작은 경우 n은 소수임으로 append
        factors.append(n)
    return factors

print('효율적인 소인수분해 결과', factorize2(30))

import time

start_t = time.time()
print('효율적인 소인수분해 결과', factorize2(4643623532532))
end_t = time.time() - start_t
print(end_t)

start_t = time.time()
print('소인수분해 결과', factorize(4643623532532))
end_t = time.time() - start_t
print(end_t)