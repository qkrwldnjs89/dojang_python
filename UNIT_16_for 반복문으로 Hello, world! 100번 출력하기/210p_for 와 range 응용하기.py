# for 와 range 응용하기

# 시작하는 숫자와 끝나는 숫자 지정하기
print("***시작, 끝 숫자 지정***")
for i in range(5, 12):
    print("Hello, world!", i)

# 증가폭 사용하기
print("***증가폭 사용하기***")
for i in range(0, 10, 2):
    print("Hello, world!", i)

# 숫자를 감소시키기
print("***증가폭을 -1로***")
for i in range(10, 0, -1):
    print("Hello, world!", i)

print("***reversed 이용***")
for i in reversed(range(10)):
    print("Hello, world!", i)

# 입력한 횟수대로 반복하기
print("***입력한 횟수대로 반복***")
count = int(input("반복할 횟수: "))

for i in range(count):
    print("Hello, world!", i)