"""
Chapter 9 연습문제

1) 두개의 문자열을 parameter 로 받아 서로의 첫번째 두 글자를 교환한 후 중간에 한칸 띄우고 반환하는 함수
"""
def swap_first_two(a, b):
    return b[:2]+a[2:], a[:2] + b[2:]

print(swap_first_two('12345', 'abcde'))
#%%
"""
1) 다음의 출력 결과는 ?
"""
for x in "Mississippi".split("i"):
    print(x, end="")
#%%   
"""
2) parameter 로 받은 string 의 양 끝단 2 글자를 붙여서 반환하는 함수
"""
def both_ends(s):
    if len(s) < 2:
        return ''
    first2 = s[:2]
    last2 = s[-2:]
    return first2 + last2

print(both_ends('spring'))
print(both_ends('Hello'))

#%%
"""
3) 두개의 문자열을 parameter 로 받아 서로의 첫번째 두 글자를 교환한 후 중간에 한칸 띄우고 반환하는 함수
"""
def mix_up(a, b):
    a_swapped = b[:2] + a[2:]
    b_swapped = a[:2] + b[2:]
    return a_swapped + ' ' + b_swapped

print(mix_up('frog', 'dinner'))