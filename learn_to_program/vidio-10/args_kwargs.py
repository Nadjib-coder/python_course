
def test_var_args(f_arg, *argv):
    print("first normal arg:", f_arg)
    for arg in argv:
        print("another arg through *argv :", arg)


test_var_args('yasoob', 'python', 'eggs', 'test')


def greet_me(**kwargs):
    if kwargs is not None:
        for key, value in kwargs.items():
            print("{} == {}".format(key, value))


greet_me(name="Nadjib")


def a_function_test(arg1, arg2, arg3):
    print("arg1 :", arg1)
    print("arg2 :", arg2)
    print("arg3 :", arg3)


a_function_test(1, 2, 3)
args = (4, 5, 6)
a_function_test(*args)
kwargs = {"arg2": 8, "arg1": 7, "arg3": 9}
a_function_test(**kwargs)
