def add_numbers(*args):
    result = 0
    for num in args:
        result += num
    print(result)

add_numbers(2, 3, 5)