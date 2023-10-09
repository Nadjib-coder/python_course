class MyClass:
    pass

obj = MyClass()

print(isinstance(obj, object))

x = 34
if isinstance(x, int):
    print("x is an integer")
else:
    print(type(x))