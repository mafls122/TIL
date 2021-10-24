def solution(n):
    # 배열 초기화
    answer = [[0 for i in range(1, j+1)] for j in range(1, n+1)]
    # x:행, y:열
    x, y = -1, 0
    num = 1
    for i in range(n):
        for j in range(i, n):
            # 3 -> 아래, 오른쪽, 위 순서로 반복
            # 아래 : 행(x) + 1
            if i % 3 == 0:
                x += 1
            # 오른쪽 : 열(y) + 1
            elif i % 3 == 1:
                y += 1
            # 위 : 행(x)-1, 열(y)-1
            else:
                x -= 1
                y -= 1
            answer[x][y] = num
            # print(answer)
            num += 1
    return sum(answer, [])

if __name__ == '__main__':
    print(solution(10))