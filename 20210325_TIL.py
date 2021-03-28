def solution(data):
    # 값이 1개인 경우 그대로 반환
    if len(data) == 1:
       return data[0]
    # 값이 1개, 2개인 경우 추가
    result = [ data[0], max(data[0], data[1]) ]
    # 리스트 값이 3개 이상일때
    for i in range(2, len(data) ):
        result.append( max( result[i-1], result[i-2] + data[i] ) )
    return result[-1]

data = [ 3, 4, 5, 6, 1, 2, 5 ]
print(solution(data))