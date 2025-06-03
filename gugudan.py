def gugudan3(*args):
    for dan in args:
        for i in range(1, 10):
            print(str(dan) + "X" + str(i) + "=" + str(dan*i))
        print()
gugudan3(2, 3, 7)