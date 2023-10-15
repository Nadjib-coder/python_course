nadjib_dict = {
    "fname": "Nadjib",
    "lname": "Mouhoun",
    "Age": 21
}

print("my name is :", nadjib_dict["fname"])
nadjib_dict["Age"] = 22
nadjib_dict['town'] = "Boumerdes"
print(nadjib_dict)
print("Is there is A city :", "city" in nadjib_dict)
print("Is there is A town :", "town" in nadjib_dict)

print(nadjib_dict.values())
print(nadjib_dict.keys())

for k, v in nadjib_dict.items():
    print(k, v)

print(nadjib_dict.get("adress", "Not there"))
print(nadjib_dict.get("fname", "Not there"))
del nadjib_dict["lname"]
for i in nadjib_dict:
    print(i)
nadjib_dict.clear()
print(nadjib_dict)

employees = []

try:
    full_name = input("Enter Employee Name : ")
    name_parts = full_name.split()
    if len(name_parts) == 2:
        fname, lname = name_parts
        employees.append({"fname": fname, "lname": lname})
        print(employees)
    else:
        print("Please Enter both first name and last name")
except ValueError:
    print("Invalid Input please enter the full name separately")
