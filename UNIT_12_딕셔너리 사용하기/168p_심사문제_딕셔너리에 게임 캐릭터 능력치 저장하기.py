# 심사문제: 딕셔너리에 게임 캐릭터 능력치 저장하기
key = input().split()
val = map(float, input().split())

dic = dict(zip(key, val))
print(dic)