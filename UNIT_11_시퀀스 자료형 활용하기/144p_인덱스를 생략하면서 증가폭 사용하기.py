# 인덱스를 생략하면서 증가폭 사용하기
a = list(range(0, 100, 10))
print(a[:7:2])
print(a[7::2])
print(a[::2])
print(a[::])
print(a[::-1])