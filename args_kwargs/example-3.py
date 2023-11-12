def show_details(*args, **kwargs):
    print("positional arguments (args):", args)
    for key, value in kwargs.items():
        print(f"{key}: {value}")


show_details(1, 2, 3, name="nadjib", age=2)
