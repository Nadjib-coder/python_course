# Create an Acronym program
# Ask for a string
string = input("Enter your string to Convert to Acronym: ")
# Convert the string to uppercase
string = string.upper()
# Convert the string into a list
a_list = string.split()
# Cycle through the list
for word in a_list:
    # Get the 1st letter of the word and eliminate the new line
    print(word[0], end='')
# Add a newline
print()
