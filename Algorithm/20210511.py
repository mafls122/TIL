
# 콜라츠의 추측(수열), 모든수 중 짝수는 2로 나누고 홀수는 곱하기3 + 1을 하다보면 결국에 1이 된다.
def collatz(n):
    seq = [n]
    while (n>1):
        if n%2 == 0 :
            n = n // 2
        else:
            n = 3 * n + 1
        seq.append(n)
    return seq

# Q. 콜라츠 수열의 길이가 100인 숫자들 중에서 가장 작은 수는?  A. 322
n = 1
while True:
    res = len(collatz(n))
    if res == 100 :
        print(n)
        break
    else:
        n += 1

# Q. 10,000 이하의 자연수 중에서 콜라츠 수열의 길이가 가장 긴 수와 길이는?

# 내가 푼 것
res_seq = []
for i in range(1,10001):
    res_seq.append(len(collatz(i)))

print(res_seq.index(max(res_seq)) + 1)
print(max(res_seq))

# 강의 코드
maxlen = 0
maxseq = []
for n in range(1, 10001):
    halestone = collatz(n)
    length = len(halestone)
    if maxlen < length :
        maxlen = length
        maxseq = halestone

print('우박수 : ',maxseq[0])
print('우박수의 길이 : ', maxlen)

# Q. 콜라츠 수열의 길이가 500보다 큰 첫번째 자연수는?

n = 0

while True:
    n += 1
    halestone = collatz(n)
    if len(halestone) > 500:
        break

print(len(halestone))  # 길이 509
print('길이가 500보다 큰 첫번째 자연수 :', n)  # 626331

# Q. 콜라츠 수열의 길이가 500보다 큰 열번째 자연수의 콜라츠 수열의 길이는?
n = 0
c_list = []

while True:
    n += 1
    halestone = collatz(n)
    if len(halestone) > 500:
        c_list.append(len(halestone))

    if len(c_list) == 10:
        break

print(c_list)
print('길이가 500보다 큰 열번째 자연수의 콜라츠 수열 길이 :', c_list[-1])

#------------------------------------------------------------
# 로마에서 아라비아까지 : 로마 숫자를 아라비아 숫자로 바꾸기

romanDict = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
s = 'MDCLXVI'
val = 0
for i in range(len(s)):
    print(s[i], ':', romanDict[s[i]])
    val += romanDict[s[i]]
print(val)

# 감산표기법(IV=4, IX=9, XL=13, XC=19,,,) 추가 및 함수로 변경
def romatoArabic(roman):
    arabic = 0
    for i in range(len(roman)):
        val = romanDict[roman[i]]
        # 총 길이의 마지막을 제외하고 and 현재 roman[i]와 뒤의 roman[i+1]을 비교하여 감산
        if (i<len(roman)-1) and val < romanDict[roman[i+1]]:
            arabic -= val
        else:
            arabic += val
    return arabic

res_roma = romatoArabic('XIV')
print(res_roma)

# 숫자를 로마 문자로 변경하여 출력

romanDict = { 1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}

# 1에서 9까지 출력 함수
def romanNumber1(n):
    str = ""
    while n >= 1 :
        if n == 9 :
            str += romanDict[1] + romanDict[10]
            n -= 9
        elif n == 4 :
            str += romanDict[1] + romanDict[5]
            n -= 4
        elif n >= 5 :
            str += romanDict[5]
            n -= 5
        else :
            for _ in range(n):
                str += romanDict[1]
            n -= n
    return str

for n in range(1,10):
    print(n, ' : ', romanNumber1(n))

# 100 미만의 숫자로 확장
def romanNumber2(n):
    str = ""
    while n >= 50 :
        if n >= 90:
            str += romanDict[10] + romanDict[100]
            n -= 90
        else:
            str += romanDict[50]
            n -= 50
    while n >= 10 :
        if n >= 40 :
            str += romanDict[10] + romanDict[50]
            n -= 40
        else:
            str += romanDict[10]
            n -= 10
    return str + romanNumber1(n)

for n in range(10, 100, 10):
    print(n, ' : ', romanNumber2(n))

# 숫자를 로마 문자로 변경하자!
romanDict2 = { 1:'I', 4:'IX', 5:'V', 9:'IX', 10:'X',40:'XL', 50:'L', 90:'XC', 100:'C',400:'CD', 500:'D', 900:'CM', 1000:'M'}
keyValues = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

def toRomanNumber(n):
    str = ""
    for i in range(len(keyValues)):
        while n >= keyValues[i] :
            str += romanDict2[keyValues[i]]
            n -= keyValues[i]
    return str

# 결과 확인
numbers = [369, 80, 29, 155, 14, 492, 348, 301, 469, 499]
for i in numbers :
    print(toRomanNumber(i), end=', ')
