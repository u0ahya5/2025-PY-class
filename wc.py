def wc(n):
    word = len(n.split())
    letter = len(n.replace(' ', ''))
    blank = n.count(' ')
    return word, letter, blank
print(wc("파이썬 수업"))

# 단어 : 파이썬, 수업 2개
# 글자 : 파, 이, 썬, 수, 업 5개
# 공백 :  1개