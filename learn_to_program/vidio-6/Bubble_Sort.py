import random


def bubble_sort(_list):
    x = len(_list) - 1
    while x > 1:
        j = 0
        while j < x:
            if _list[j] > _list[j + 1]:
                temp = _list[j]
                _list[j] = _list[j + 1]
                _list[j + 1] = temp
            j += 1
        x -= 1
    return _list


rand_list = []
for i in range(5):
    rand_list.append(random.randint(1, 9))

bubble_sort(rand_list)

for i in rand_list:
    print(i, end="")
