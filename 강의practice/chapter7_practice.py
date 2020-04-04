"""
1) 다음 문장 수행 후의 output 은 ?
"""
xlist = [1, [1, 2], [1, 2, 3]]
print(xlist[1][1] + 1)
#%%
"""
3) 다음 문장 수행 후의 output 은 ?
"""
def sum_part(xlist, n):
    sum = 0
    for x in xlist[n]:
        sum = sum + x
    return sum

ylist = [[1, 2], [3, 4], [5, 6], [7, 8]]
x = sum_part(ylist, 2)
print(x)
