# 이차방정식의 근 구하기
a = (2**(1/2)) - 1
b = 3 - (2**(1/2))
c = (2**(1/2))

res = ((-b + ((b**2)-(4*a*c)) )/2*a )
print(res)

res2 = ((-(2-1j) + ((2-1j)**2) - (4*1j*-1-1j)) / 2*1j)
print(res2)

# 1. 최대 공약수 구하기
note = 20
pen = 12

# 유클리드 호제법 사용
while note:
    pen, note = note, pen % note

print(pen)

# 2. 어떤 자연수로 77을 나누어도 나머지가 2, 92를 나누어도 나머지가 2이다. 이러한 자연수 중 가장 큰 수는?
x=77
y=92

while x:
    y, x = x, y % x

print(y+2)

# 확인
res = []
res2 = []
for i in range(1,y+1):
    if y % i == 0 :
        res.append(i)

for i in range(1, x+1):
    if x % i == 0 :
        res2.append(i)

print(res)
print(res2)

# 세 가지 수의 최대 공약수 구하기
num1 = 78696
num2 = 19332
num3 = 73500

def gcd(a,b):
    while b:
        a, b = b, a%b

    return a

print(gcd(gcd(num1,num2),num3))

# 사물함 문제 1~100번까지
# 닫혀있는게 0
locker = [ 0 ] * 101
print(len(locker))
print(locker)

for i in range(1,101):
    for j in range(i,101,i):
        if locker[j] == 0 :
            locker[j] = 1
        else :
            locker[j] = 0

print(locker)

cnt = []
for i in locker:
    if i == 1:
        cnt.append(i)
print(len(cnt))

# 완전제곱수를 활용하여 구하기
locker2 = []
n= 100
i = 1

# for i in range(1,101):
#     if i**2 <= n :
#         locker.append(i**2)


while( i**2 <= n ):
    locker2.append(i**2)
    i += 1

print('locker : ',locker2)
print(len(locker2))
