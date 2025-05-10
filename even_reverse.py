text = input("문자열 입력 : ")
answer = ""

for i in range(len(text)):
    if i!=0 and i%2==0:
        answer = text[i] + answer
print(answer)