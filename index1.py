def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
            return result
        

plaintext = input("Enter the plaintext:")
shift = int(input("Enter the shift (an integer): "))
encrypted_text =  caesar_cipher(plaintext, shift)

print("plaintext" , plaintext)
print("shift", shift)
print("encrypted text:" , encrypted_text)