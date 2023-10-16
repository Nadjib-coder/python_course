import os

with open("test.txt", mode="w", encoding="utf-8") as myFile:
    myFile.write("Hello World\nI'am Nadjib and iam a software enginner")

with open("test.txt", encoding="utf-8") as myFile:
    print(myFile.read())

# os.rename("test.txt", "myData.txt")
os.remove("myData.txt")
os.rename("test.txt", "mydata.txt")
os.mkdir("new_dir")
os.chdir("new_dir")
print("current directory:", os.getcwd())


"""
print(myFile.closed)
print(myFile.name)
print(myFile.mode)
"""

