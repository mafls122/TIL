import time

# 소수 판별기 만들기
num = 13
res = True

for i in range(2,num):
    if num % i == 0 :
        res = False
    
if res :
        print("소수 맞습니다.")
else :
        print("소수가 아님")

# 함수로 변경
def isPrime(num):
    for i in range(2, num):
        if num % i == 0 :
            return False
    return True

# math 내장함수 사용
import math
def isPrime2(num):
    for i in range(2, math.floor(math.sqrt(num))+1):
        if num % i == 0 :
            return False
    return True

# 1보다 크고 100보다 작은 소수는 모두 몇 개 있는가?
cnt = 0
for i in range(2,100):
    if isPrime2(i) :
        cnt +=1

print(cnt)

# 에라토스테네스의 체
def countPrime(num):
    sieve = [False, False] + ([True] * (num-1))
    count = 0
    for i in range(2, num+1):
        if sieve[i]:
            count += 1
        for j in range(i*2, num+1, i):
            sieve[j] = False

    return count, sieve

print(countPrime(100))
