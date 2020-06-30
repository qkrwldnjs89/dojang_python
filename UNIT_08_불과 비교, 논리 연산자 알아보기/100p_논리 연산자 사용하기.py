# 논리 연산자 사용하기

# and
print("**and**")
print(True and True)
print(True and False)
print(False and False)

# or
print("**or**")
print(True or True)
print(True or False)
print(False or False)

# not
print("**not**")
print(not True)
print(not False)

# 섞여 있을 때 -> not, and, or 순으로 판단
print("**섞여 있을 때 -> not, and, or 순으로 판단**")
print( not True and False or not False ) # ((not True) and False) or (not False) 