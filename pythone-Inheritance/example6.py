class A:
    pass

class D:
    pass
class B(D):
    pass

if issubclass(B, D):
    print("B is a subclass of D")
else:
    print(type(B))