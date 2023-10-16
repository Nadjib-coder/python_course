def fib(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fib(num - 1) + fib(num - 2)

fibonacci_number = int(input("how many fibonacci number should be found : "))

i = 1
while i < fibonacci_number:
    fib_num = fib(i)
    print(fib_num)
    i += 1
print("All done")