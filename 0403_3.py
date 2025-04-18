a, b = map(int, input('학년 반을 입력해주세요: ').split())

if (a == 2 and b in [1, 3, 5]) or (a + b) % 2 != 0:
    print("부담임 선생님")
elif a == 2 and b == 2:
    print("권지웅 선생님")
elif a == 2 and b == 4:
    print("임진하 선생님")
elif a == 2 and b == 5:
    print("손명수 선생님")
elif a == 2 and b == 6:
    print("6반 선생님")