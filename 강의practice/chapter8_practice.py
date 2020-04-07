"""
Chapter 8 연습문제

1) 다음의 출력 결과는 ?
"""
d = {'c': 9,'a': 4, 'b':6}
for x in sorted(d):
    print(d[x], end="")
#%%
"""
2) 다음의 출력 결과는 ?
"""
d = {'c': 9,'a': 4, 'b':6}
for x in sorted(d.values()):
    print(x, end="")
    #%%
"""
3) 다음의 출력 결과는 ?
"""
d = {'c': 9,'a': 4, 'b':6}
for k, v in sorted(d.items()):
    print(k, v)
    
#%%
"""
4) 두개의 주사위를 던져서 두 주사위의 합이 같은 것끼리 출력
"""
d = {}

for dice1 in range(1, 7):
    for dice2 in range(1, 7):
        newTuple = (dice1, dice2)
        added = dice1 + dice2
        if added not in d:
            d[added] = []
        d[added].append(newTuple)

print(d)
