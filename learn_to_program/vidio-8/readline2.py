with open("MyData.txt", encoding="utf-8") as myFile:

    lineNum = 1
    while True:
        line = myFile.readline()
        if not line:
            break

        print("Line", lineNum)

        word_list = line.split()
        print("Number of words :", len(word_list))

        charCount = 0
        for word in word_list:
            for char in word:
                charCount +=1

        AvgNumChar = charCount / len(word_list)
        print("Avg Word Length : {:.2f}:".format(AvgNumChar))

        lineNum += 1