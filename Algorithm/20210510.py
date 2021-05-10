import math

def lcm(n,m):
    return (n*m) // math.gcd(n,m)

def lcmFromTo(start, end):
    l = start
    for i in range(start+1, end+1):
        l = lcm(l,i)
    return l

# 1에서 10까지 최소공배수 -> 2520
print(lcmFromTo(1,10))
# 1에서 20까지 최소공배수
print(lcmFromTo(1,20))

# 1000일 후의 날짜를 계산하자
year = 2021
month = 5
day = 10
n = 1000

# 윤년, 그레고리력 근거하여 구함
def leapyear(y):
    # 4의 배수이며 100의 배수가 아닐 때 and 400의 배수일 때
    if ((y%4 == 0 and y%100 !=0) or y % 400 == 0):
        return True
    else:
        return False

def invalidDay(y,m,d):
    num = 31
    if m in [4,6,9,11]:
        num = 30
    if m == 2:
        if leapyear(year):
            num = 29
        else:
            num = 28
    if d > num :
        return True
    else:
        return False

for _ in range(n):
    day += 1
    if (invalidDay(year, month, day)):
        day = 1
        month += 1
        if (month > 12):
            month = 1
            year += 1

print(year, month, day)

# 파이썬 함수 사용
import datetime
year, month, day, n = 2021, 5, 10, 1000

day = datetime.date(year, month, day)
theday = day + datetime.timedelta(n)
print(theday)

print('\n')
# 달력 출력하기
def daysOfMonth(y, m):
    num = 31
    if m in [4,6,9,11]:
        num = 30
    if m == 2 :
        if (leapyear(y)):
            num = 29
        else:
            num = 28
    return num

year, month, day_of_week = 2021, 5, 6

print(year, '년', month, '월: ')
weekdays = ['일','월','화','수','목','금','토']
for day in weekdays:
    print(' ', day, end=' ')
print()
# 1일 전, 공백 출력
for _ in range(day_of_week):
    print('    ', end=' ')
# 날짜 출력
for day in range(1, daysOfMonth(year,month) + 1):
    if day < 10 :
        print('  ', day, end=' ')
    else:
        print(' ', day, end=' ')
    if (day_of_week + day) % 7 == 0 :
        print()
print()

# 수학적으로 1일이 무슨 요일인지 알아보자
def dayOfWeek(y, m, d):
    t1 = y - (14-m) // 12
    t2 = t1 + (t1//4) - (t1//100) + (t1//400)
    t3 = m + 12 * ((14-m) //12) -2
    return (d+t2+(31*t3//12)) % 7

year, month, day = 2021,5,10
res = dayOfWeek(year,month,day)
print(weekdays[res],'요일')

# 달력 출력
def printCalendar(y,m):
    m_num = daysOfMonth(y,m)
    day_of_week = dayOfWeek(y,m,1)
    print(y,'년',m,'월')
    for day in weekdays:
        print(' ', day, end=' ')
    print()
    for _ in range(day_of_week):
        print('    ', end=' ')
    for day in range(1, m_num+1):
        if day<10:
            print('  ', day, end=' ')
        else:
            print(' ', day, end=' ')
        if (day_of_week + day) % 7 == 0:
            print()
    print()

printCalendar(2021,5)

print('\n')

# Q. 연도를 입력하면 그 해의 달력을 모두 출력하기
in_year = int(input())

for i in range(1,13):
    printCalendar(in_year, i)