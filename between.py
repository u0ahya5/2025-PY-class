def sum_of_integers(a,b):
    num = 0
    for i in range(a, b+1):
        num += i
    return num

a = int(input())
b = int(input())

print (sum_of_integers(a, b))