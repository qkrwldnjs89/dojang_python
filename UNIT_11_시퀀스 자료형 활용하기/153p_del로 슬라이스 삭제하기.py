# del 로 슬라이스 삭제하기
a = list(range(0, 100, 10))
del a[2:5]
print(a)

b = list(range(0, 100, 10))
del b[2:8:2]
print(b)