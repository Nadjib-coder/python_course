import random

random_list = []
for i in range(5):
    random_list.append(random.randint(1, 9))

random_list.sort()
random_list.reverse()
random_list.insert(5, 10)
random_list.remove(10)
random_list.pop(2)

for item in random_list:
    print(item, end=" ")
