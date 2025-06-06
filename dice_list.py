import random

def dice_list(eye, count):
    result = []
    for i in range(0, count):
        a = random.randint(1, eye)
        result = result + [a]

    return result
print(dice_list(6, 3))