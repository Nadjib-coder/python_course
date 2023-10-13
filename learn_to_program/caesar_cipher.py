# A - Z 65 - 90
# a -z 97 - 122
# ord(your_letter)
# chr(your_unicode)

# Hints
# Use isupper() to decide which unicodes to work with
# Add the key (number of characters to shift) and if
# the key is bigger or smaller than the unicode for
# A , Z, a, z increase or decrease by 26

# receive the message to encrypt and the number of
# characters to shift
message = input("Enter your message: ")
key = int(input("How many characters should we shift (1 - 26): "))
# Prepare the secret_message
secret_message = ""
# Cycle through each character in the message
for char in message:
    # If it isn't a letter then keep it as it is
    if char.isalpha():
        # Get the character code and add the shift amount
        char_code = ord(char)
        char_code += key
        # If uppercase then compare to uppercase unicode
        if char.isupper():
            # If bigger than Z subtract 26
            if char_code > ord('Z'):
                char_code -= 26
            # If smaller than A add 26
            if char_code < ord('A'):
                char_code += 26
        else:
            if char_code > ord('z'):
                char_code -= 26
            if char_code < ord('a'):
                char_code += 26
        # Convert from code to letter and add to message
        secret_message += chr(char_code)
    # If not a letter leave character as is
    else:
        secret_message += char

print("Encrypted :", secret_message)

key = -key
original_message = ""
for char in secret_message:
    if char.isalpha():
        char_code = ord(char)
        char_code += key
        if char.isupper():
            if char_code > ord('Z'):
                char_code -= 26
            if char_code < ord('A'):
                char_code -= 26
        else:
            if char_code > ord('z'):
                char_code += 26
            if char_code < ord('a'):
                char_code -= 26
        original_message += chr(char_code)
    else:
        original_message += char

print("Decrypted :", original_message)
