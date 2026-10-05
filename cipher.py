text = input("Enter the text: ")

choice = input("Do you want to encrypt (e) or decrypt? (d) ").lower()

shift = int(input("By how many characters should the alphabet shift? "))

result = ""

for char in text:
    if char.isalpha():
        # Keep uppercase and lowercase letters separate
        if char.isupper():
            start = 65
        else:
            start = 97

        if choice == "e":
            new_char = chr((ord(char) - start + shift) % 26 + start)

        elif choice == "d":
            new_char = chr((ord(char) - start - shift) % 26 + start)

        else:
            print("Invalid choice. Please enter 'e' or 'd'.")
            exit()

        result += new_char

    else:
        # Keep spaces, numbers, punctuation unchanged
        result += char

print("Output:", result)
