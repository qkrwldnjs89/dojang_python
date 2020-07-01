# 시퀀스 객체로 반복하기

# 리스트 넣어서 반복
print("***list 넣어서 반복***")
a = list(range(10, 51, 10))
for i in a:
    print(i)

# 튜플 넣어서 반복
print("***tuple 넣어서 반복***")
fruits = ("apple", "orange", "grape")
for fruit in fruits:
    print(fruit)

# 문자열 넣어서 반복
print("***문자열 넣어서 반복***")
for letter in "Python":
    print(letter, end = ' ')

# 시퀀스 객체 뒤집어서 반복
print("\n***시퀀스 객체 뒤집어 반복***")
for letter in reversed("Python"):
    print(letter, end = ' ')