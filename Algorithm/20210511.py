
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

# n = 1
# while True:
#     res = len(collatz(n))
#     print(res)
#     if res > 500 :
#         print(n)
#         break
#     else:
#         n += 1
# 500번을 넘지 못한다. 없음
#------------------------------------------------------------
# 로마에서 아라비아까지 : 로마숫자를 아라비아 숫자로 바꾸기

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

