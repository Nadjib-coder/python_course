list_num = [[0] * 3 for i in range(5)]
print(list_num)

for i in range(5):
    for j in range(3):
        list_num[i][j] = "{} : {}".format(i, j)

print(list_num)
