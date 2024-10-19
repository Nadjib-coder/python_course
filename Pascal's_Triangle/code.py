def generate_pascal_triangle(num_of_row):
    triangle = []

    for i in range(num_of_row):
        row = [1] * (i + 1)

        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        triangle.append(row)

    return triangle

triangle1 = generate_pascal_triangle(5)

for row in triangle1:
    print(row)
