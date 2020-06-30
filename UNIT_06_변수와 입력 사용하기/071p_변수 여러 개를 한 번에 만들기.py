# 변수 여러 개를 한 번에 만들기
x, y, z = 1, 2, 3
print("x = ", x, "y = ", y, "z = ", z)

# 값이 같아도 된다면
x = y = z = 1
print("x = ", x, "y = ", y, "z = ", z)

# 두 변수의 값을 바꾸려면
x, y = 10, 20
x, y = y, x
print("x = ", x, "y = ", y)

# 변수 삭제하기
del x, y, z

# 빈 변수 만들기
x = None
print(x) # None 이 출력
