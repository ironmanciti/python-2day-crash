"""
chapter 5 연습문제

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
#%%
"""
2) 섭씨 온도를 화씨 온도로 변환하는 함수를 작성한다. 변환 공식은 다음과 같다.
"""
def fc_convert(tc):
    return 9 / 5 * tc + 32

print(fc_convert(100))

