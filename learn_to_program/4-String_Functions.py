string = "    hello from nadjib to annia   "
string = string.lstrip()
string = string.rstrip()
string = string.strip()
print(string.capitalize())
print((string.upper()))
print(string.lower())
a_list = ["Bunch", "of", "random", "words"]
print(" ".join(a_list))
a_list_2 = string.split()
for i in a_list_2:
    print(i)
print(f"there is {string.count('o')} character 'o' in the list")
# i need to find nadjib
print("nadjib is at index", string.find("nadjib"))
# i want to change annia to feriel
print(string.replace("annia", "feriel"))

letter_z = "z"
num_3 = "3.14"
a_space = " "

print("Is z a letter or a number :", letter_z.isalnum())
print("Is z a letter :", letter_z.isalpha())
print("Is 3 a number :", num_3.isdigit())
print("Is z a lowercase :", letter_z.islower())
print("Is z a uppercase :", letter_z.isupper())
print("Is space a space :", a_space.isspace())