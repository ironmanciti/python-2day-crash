"""
1) 두개의 문자열을 parameter 로 받아 서로의 첫번째 두 글자를 교환한 후 중간에 한칸 띄우고 반환하는 함수
"""
def swap_first_two(a, b):
    return b[:2]+a[2:], a[:2] + b[2:]

print(swap_first_two('12345', 'abcde'))
#%%
"""
2) 다음의 출력 결과는 ?
"""
for x in "Mississippi".split("i"):
    print(x, end="")