count = 0

for i in range(1, 100 + 1):
    num = str(i)
    for clap in num:
        if clap in "369":
            count += 1

print("박수 친 횟수 : " + str(count))