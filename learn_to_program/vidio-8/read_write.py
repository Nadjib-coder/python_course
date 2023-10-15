import os

with open("test.txt", mode="w", encoding="utf-8") as myFile:
    myFile.write("Hello World\nI'am Nadjib and iam a software enginner")

with open("test.txt", encoding="utf-8") as myFile:
    print(myFile.read())

# os.rename("test.txt", "myData.txt")
os.remove("myData.txt")

"""
print(myFile.closed)
print(myFile.name)
print(myFile.mode)
"""

