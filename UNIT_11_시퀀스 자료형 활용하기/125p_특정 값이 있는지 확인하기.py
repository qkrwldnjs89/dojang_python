# 특정 값이 있는지 확인하기
a = list(range(0, 91, 10))
print(30 in a)
print(100 in a)

b = tuple(range(10))
print(10 not in b)

print('P' not in "Hello, Python")