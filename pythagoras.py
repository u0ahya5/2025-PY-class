for a in range(1, 400):
    for b in range(a+1, 400+1):  # b는 a보다 커야 하니까 a+1부터 시작
        c = 400-a-b  # a + b + c = 400 이므로 c = 400 - a - b
        if a**2 + b**2 == c**2:  # 피타고라스 정리 확인
            print("a = " + str(a) + ", b = " + str(b) +", c = " + str(c))