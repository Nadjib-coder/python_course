# solve for x
# x + 4 = 9 : 4 + x = 9

def solve_eq(equation):
    x, add, num1, equal, num2 = equation.split()

    num1, num2 = int(num1), int(num2)

    return "x = " + str(num2 - num1)


print(solve_eq("x + 4 = 9"))


def mult_divide(num1, num2):
    return (num1 * num2), (num1 / num2)


mult, divide = mult_divide(5, 4)

print("5 * 4 =", mult)
print("5 / 4 =", divide)
