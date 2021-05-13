
# 이차원 배열과 마방진

# 간단하게 이차원 배열 출력하기
magicSquare = [
    [1, 14, 14, 4],
    [11, 7, 6, 9],
    [8, 10, 10, 5],
    [13, 2, 3, 15]
]

for i in range(len(magicSquare)):
    print(magicSquare[i])

# 1. 배열 중 행의 합을 출력하는 함수 만들기
def checkRow(square):
    for row in range(len(square)):
        sum = 0
        for col in range(len(square)):
            sum += square[row][col]
        print(sum, end=' ')
    print()

checkRow(magicSquare)

# 2. 배열 중 열의 합을 출력하는 함수 만들기
def checkCol(square):
    for col in range(len(square)):
        sum = 0
        for row in range(len(square)):
            sum += square[row][col]
        print(sum, end=' ')
    print()

checkCol(magicSquare)

# 3. 배열 중 대각선의 합을 출력하는 함수 만들기
def checkDiagonal(square):
    sum = 0
    for d in range(len(square)):
        sum += square[d][d]
    print(sum, end=' ')
    sum = 0
    for d in range(len(square)):
        d2 = len(square) - 1 - d
        sum += square[d2][d2]
    print(sum)

checkDiagonal(magicSquare)

# 마방진을 체크하는 함수
def checkMagic(square):
    magic = 0
    for i in range(len(square)):
        magic += square[0][i]
    for i in range(len(square)):
        rsum = 0
        csum = 0
        for j in range(len(square)):
            rsum += square[i][j]
            csum += square[j][i]
        if rsum != magic or csum != magic :
            return False
    dsum = 0
    d2sum = 0
    for d in range(len(square)):
        d2 = len(square) -1 -d
        dsum += square[d][d]
        d2sum += square[d2][d2]
    if dsum != magic or d2sum != magic:
        return False
    return True

print(checkMagic(magicSquare))

# n * n 마방진 만들기 (단, n은 홀수)
'''
1. 첫번째 열의 가운데 행을 1로 채움
2. 해당 위치에서 한 칸 왼쪽, 한 칸 위쪽으로 이동
 - 칸을 벗어나면 그 줄의 반대쪽으로 이동
3. 이동할 위치에 숫자가 이미 있으면 한 칸 아래로 이동
 - 이동할 위치에 숫자가 없으면 이동해서 숫자를 채움
'''

def makeMagicSquare(n):
    # 배열 초기화
    square = [ [0] * n for _ in range(n) ]
    row = 0
    col = n // 2
    for k in range(1, n*n+1):  # 1부터 25까지
        square[row][col] = k
        row -= 1
        if row < 0 :
            row += n
        col -= 1
        if col < 0 :
            col += n
        if square[row][col] > 0 :
            row = ( row + 2 ) % n
            col = ( col + 1 ) % n
    return square

print('\n내가 만든 마방진 출력')
magicSquare2 = makeMagicSquare(5)
for row in magicSquare2:
    print(row)

print(checkMagic(magicSquare2))


# 등차수열의 합 구하기
def summation(n):
    s = 0
    for i in range(1, n+1): 
        s += i * (n+1 - i)
    return s

print(summation(20))

# 재귀
def sumOfArray(array, i):
    end = len(array) - 1
    if end == i :
        return array[end]
    else:
        return array[i] + sumOfArray(array, i+1)

print(sumOfArray([1,2,3,4,5,6,7,8,9,10],0))

# 재귀2 - 팩토리얼
def factorial(n):
    if n == 0 or n == 1 :
        return 1
    else:
        return n * factorial(n-1)

for n in range(11):
    print(n, " != ", factorial(n))
print()

# 재귀3 - 피보나치 수
def fibonacci(n):
    if n < 2 :
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

for n in range(11):
    print("F({}) = {}".format(n, fibonacci(n)))
print()

# 재귀4 - 두 자연수 n,k에 대한 이항계수 구하기
def binomial(n, k):
    if k == 0 or n == k :
        return 1
    else:
        return binomial(n-1, k-1) + binomial(n-1, k)
    
# 재귀 호출 제한 횟수 변경
# import sys
# sys.setrecursionlimit(10**9)

print('이항계수 n, k : ', binomial(5,2))