n = int(input())
arr = set(map(int, input().split()))
m = int(input())
test = list(map(int, input().split()))

for i in test:
    if i in arr:
        print("1")
    else:
        print("0")