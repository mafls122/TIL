#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from itertools import combinations

# 최대 공약수 구하기
def gcd(x,y):
  while x:
      y, x = x, y % x
  
  return y


n = int(input())
lists = []
result = 0

for _ in range(n):
    lists = list(map(int, input().split())) # 최대공약수 구할 숫자 리스트
    lists = lists[::-1] # 내림차순 정렬
    del lists[len(lists) - 1] # 마지막 요소 제거
    ncr = combinations(lists, 2) # 조합 생성
    
    for i in ncr:
        result += gcd(i[0], i[1]) # 조합을 통해 최대공약수들 합 result에 저장
    
    print(result) # 출력
    result = 0 # 초기화


# In[1]:


import itertools

lists = [1, 2, 3]
permut = list(itertools.permutations(lists, 2))
comb = list(itertools.combinations(lists, 2))

# permutations는 순열, combinations는 조합을 쉽게 출력한다.
print('순열: {} \n조합: {}'.format(permut, comb))

