"""
creat a function
creat a flag
creat a while loop thet run when the flage is yes
ask the costumer yes or no
if condition: if yes ask the name
when no
break
and print the costumers name
"""
costumer = []


def add_comstumer():
    flag = True
    while flag:
        flage_value = input("Enter Customer (Yes/No) : ")
        flage_value = flage_value.lower()
        if flage_value == "yes" or flage_value == "y":
            enter_costumer_name()
        elif flage_value == "no" or flage_value == "n":
            flag = False
            print_constumer_name()
        else:
            print("Please Enter (Yes/NO) or (Y/N)")


def enter_costumer_name():
    try:
        full_name = input("Enter Customer Name : ")
        name_parts = full_name.split()
        if len(name_parts) == 2:
            first_name, last_name = name_parts
            costumer.append({first_name, last_name})
        else:
            print("Please Enter Both First and Last Name!")
    except ValueError:
        print("Invalid Input Please Enter The Full Name separated!")


def print_constumer_name():
    for item in costumer:
        fname, lname = item
        print(fname, lname)


add_comstumer()
