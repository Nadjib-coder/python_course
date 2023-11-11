# Define a list of student records
students = [
    {"name": "Alice", "class_section": "A"},
    {"name": "Bob", "class_section": "B"},
    {"name": "Carol", "class_section": "A"},
    {"name": "David", "class_section": "C"},
    {"name": "Eve", "class_section": "B"},
]

# Perform a stable sort by name using the sorted() function
students = sorted(students, key=lambda x: x["name"])

# Print the sorted list by name
print("Sorted by name (stable):")
for student in students:
    print(student["name"], student["class_section"])

# Perform an unstable sort by class_section using the sorted() function
students = sorted(students, key=lambda x: x["class_section"])

# Print the sorted list by class_section
print("\nSorted by class_section (unstable):")
for student in students:
    print(student["name"], student["class_section"])
