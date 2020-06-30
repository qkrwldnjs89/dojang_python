# slice 객체 사용하기
print(range(10)[slice(4, 7, 2)])
print(range(10).__getitem__(slice(4, 7, 2)))

s = slice(1, 7, 2)
a = list(range(0, 100, 10))
b = tuple(range(0, 100, 10))
r = range(10)
hello = "Hello, world!"

print(a[s])
print(b[s])
print(r[s])
print(hello[s])
