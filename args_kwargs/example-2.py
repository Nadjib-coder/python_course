def print_dict(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_dict(name="nadjib", age=21, city="Dellys")
