# Tuples

myTuple = (1, 2, 3, 4)

print("First Value :", myTuple[0])
print(myTuple[0:3])
print("the length is :", len(myTuple))
moreValue = myTuple + (5, 6, 7)
print("6 in tuple ? :", 6 in moreValue)
for i in moreValue:
    print(i)

# convert a list to tuple and vers versa

list_a = [13, 23, 45]
tuple_a = tuple(list_a)
print(tuple_a)
list_a = list(tuple_a)
print(list_a)

# print the min amd max value in a tuple
print("Min :", min(tuple_a))
print("Max :", max(tuple_a))

