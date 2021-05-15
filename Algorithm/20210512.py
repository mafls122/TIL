
# 임의의 수 : 난수 (random 모듈 사용 : randint(a,b))
import random

def guess(answer, start, end):
    print(answer)
    while start < end :
        mid = (start+end) // 2
        if mid < answer :
            start = mid +1
        else:
            end = mid
    return start

A = random.randint(1, 1000)
print(guess(A, 1, 1000))

# 몇 고개를 넘어야 답을 맞출까?
def guess2(answer, start, end):
    count = 0
    while start < end :
        count += 1
        mid = (start+end) // 2
        if mid < answer :
            start = mid +1
        else:
            end = mid
    return count

B = random.randint(1,1000)
print(guess2(B, 1, 1000))

# 로그를 깨닫자
start = 1
for n in range(21):  # 0부터 20까지
    end = 2 ** n
    maxcount = 0
    for _ in range(1000):
        answer = random.randint(start,end)
        count = guess2(answer, start, end)
        if maxcount < count :
            maxcount = count
    print(start, end, maxcount, 2 ** n)  # 횟수와 2의n승이 같은 것을 볼 수 있다. (=n번의 질문을 통해서 답을 찾는다)


# 계란 낙하실험 문제
n = 100  # 횟수
answer = random.randint(1, n)  # 높이

# 계란이 깨지는지 안깨지는지 판별
def isSafe(h):
    if h < answer :
        return True
    return False

# 계란이 1개일 때, 순차탐색(1부터 100(n)까지)
def eggDrop1(n):
    for height in range(1, n+1):
        if (not isSafe(height)):
            return height

print(answer, eggDrop1(n))

# 계란이 많은 경우, 분할탐색
def eggDrop2(n):
    start = 1
    end = n
    while start + 1 < end :
        mid = (start+end) // 2
        if isSafe(mid):
            start = mid
        else:
            end = mid
    return end

print(answer, eggDrop2(n))

# 계란이 몇 개나 필요할까? -> log
def countEggDrop2(n):
    start = 1
    end = n
    count = 0
    while start + 1 < end :
        count += 1
        mid = (start+end) // 2
        if isSafe(mid):
            start = mid
        else:
            end = mid
    return count

for i in range(1,21):
    maxcount = 0
    n = 2 ** i
    for _ in range(1000):
        answer = random.randint(1, n)
        count = countEggDrop2(n)
        if maxcount < count :
            maxcount = count
    print(n, maxcount)

print()
# 계란이 두 개 뿐이라면?, 이진탐색
import math

def twoEggsDrop(n):
    sqrt_n = math.floor(math.sqrt(n))
    for h in range(sqrt_n, n+1, sqrt_n):
        if not isSafe(h):
            break
    for h2 in range(h - sqrt_n+1, h):
        if not isSafe(h2):
            return h2

n = 100
answer = random.randint(1, n)
print(answer, twoEggsDrop(n))

# 계란이 두 개 뿐일때 횟수 구하기
def twoEggsDrop2(n):
    count = 0
    sqrt_n = math.floor(math.sqrt(n))
    for h1 in range(sqrt_n, n+1, sqrt_n):
        count += 1
        if not isSafe(h1):
            break
    for h2 in range(h1 - sqrt_n+1, h1):
        count += 1
        if not isSafe(h2):
            return count

n = 100
for answer in range(1,101):
    print(answer, twoEggsDrop2(n))