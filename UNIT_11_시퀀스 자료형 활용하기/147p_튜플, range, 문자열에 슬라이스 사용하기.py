# 튜플, range, 문자열에 슬라이스 사용하기
b = tuple(range(0, 100, 10))
print(b[4:7])
print(b[4:])
print(b[:7:2])

r = range(10)
print(r[4:7])
print(r[4:])
print(r[:7:2])
print(list(r[:7:2]))

hello = "Hello, world!"
print(hello[2:9])
print(hello[2:])
print(hello[:9:2])