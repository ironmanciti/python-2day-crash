"""
1) 다음 code 가 수행된 이후 z 의 값은 ?
"""
def f1(x, y):
    return (x + 1) / (y - 1)

z = f1(2, 2)
print(z)

def f1(x, y=2):
    return (x + 1) / (y - 1)

z = f1(1)
print(z)
