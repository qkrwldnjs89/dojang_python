# dict 로 딕셔너리 만들기
lux1 = dict(health = 490, mana = 334, melee = 550, armor = 18.72)
# ' 나 " 를 붙여주지 않아야 함, 키는 딕셔너리를 만들고 나면 문자열로 바뀜
print("lux1:", lux1)

lux2 = dict(zip(["health", "mana", "melee", "armor"], [490, 334, 550, 18.72]))
print("lux2:", lux2)

lux3 = dict([("health", 490), ("mana", 334), ("melee", 550), ("armor", 18.72)])
print("lux3:", lux3)

lux4 = dict({"health": 490, "mana": 334, "melee": 550, "armor": 18.72})
print("lux4:", lux4)