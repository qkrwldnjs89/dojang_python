# 심사문제: 온라인 할인 쿠폰 시스템 만들기 
price = int(input())
couponName = input()

if (couponName == "Cash3000"):
    price -= 3000

if (couponName == "Cash5000"):
    price -= 5000

print(price)