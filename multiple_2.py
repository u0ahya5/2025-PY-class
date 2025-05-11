print("2의 제곱 맞추기!")
p = 0  # 제곱 수
n = 50  # 기회 수

for i in range(n):
    answer = 2 ** p  # 정답 계산
    x = input("")

    if x == "end":
        print("종료")
        break

    if x.isdigit():
        x = int(x)
        if x == answer:
            print("정답")
            p += 1
        else:
            print("다시 입력하세요")

else:
    print("기회 소진")