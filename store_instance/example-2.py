class Students:
    def __init__(self, name):
        self.name = name


students = reload()  # recreate the list of Student objects from a file
s = Students("Nadjib")
students.append(s)
save(students)  # save all Student objects to a file
