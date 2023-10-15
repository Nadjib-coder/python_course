import os

with open("test.txt", mode="w", encoding="utf-8") as myFile:
    myFile.write("Hello World\nI'am Nadjib and iam a software enginner")

with open("test.txt", encoding="utf-8") as MyFile:
    print(MyFile.read())
