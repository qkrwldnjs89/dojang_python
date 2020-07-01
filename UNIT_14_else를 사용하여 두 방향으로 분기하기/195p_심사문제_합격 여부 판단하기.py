# 심사문제: 합격 여부 판단하기
kor, eng, math, science = map(int, input().split())
avg = (kor + eng + math + science) / 4

if (0 <= kor <= 100) and (0 <= eng <= 100) and (0 <= math <= 100) and (0 <= science <= 100):
    if (avg >= 80):
        print("합격")
    else:
        print("불합격")
else:
    print("잘못된 점수")
