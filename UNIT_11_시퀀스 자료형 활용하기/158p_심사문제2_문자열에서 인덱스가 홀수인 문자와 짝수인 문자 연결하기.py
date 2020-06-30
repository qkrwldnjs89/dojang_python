# 심사문제: 문자열에서 인덱스가 홀수인 문자와 짝수인 문자 연결하기
str1 = input()
str2 = input()

connectedStr = str1[1::2] + str2[0::2]
print(connectedStr)
