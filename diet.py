now = int(input("현재 몸무게 : "))
target = int(input("목표 몸무게 : "))
week = 1

while now>target:
    update = int(input(str(week)+"주차 감량 몸무게 : "))
    now -= update
    week += 1

print(str(now)+"kg 달성! 축하합니다!")