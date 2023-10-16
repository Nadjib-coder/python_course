with open("MyData.txt", mode="w", encoding="utf-8") as myFile:
    myFile.write("Some Random text\nMore Random text\nAnd Some More")

with open("MyData.txt", encoding="utf-8") as myFile:

    lineNum = 1
    while 1:
        line = myFile.readline()
        if not line:
            break
        print("Line", lineNum, ":", line, end="")
        lineNum += 1
