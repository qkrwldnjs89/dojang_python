# 변수에 값 할당을 if, else 로 축약하기
'''
x = 5
if x == 10:
    y = x
else:
    y = 0

를 축악하면
'''
x = 5
y = x if x == 5 else 0
print(y)