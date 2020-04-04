"""
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
