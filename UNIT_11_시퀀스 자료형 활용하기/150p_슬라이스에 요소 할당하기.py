# 슬라이스에 요소 할당하기 
a = list(range(0, 100, 10))
a[2:5] = ['a', 'b', 'c']
print(a)

a[2:5] = ['a']
print(a)

a[2:3] = ['a', 'b', 'c', 'd', 'e', 'f']
print(a)

# 인덱스 증가 폭을 지정해 할당
b = list(range(0, 100, 10))
b[2:8:2] = ['a', 'b', 'c']
print(b)