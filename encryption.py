import string


#Saves the text in text.txt as variable
text_file = open("text.txt", "rt")
plain_text = text_file.read()
text_file.close()

#Deletes all entries in the text.txt file
text_file = open("text.txt", "wt")
text_file.write("")
text_file.close()

#Writes text into the specified file
def write_to_file(text):
    file = open("text.txt", "wt")
    file.write(text)
    file.close()

print("-----------------------------------------------------------------------")
print("------------------------Simple En-/Decryptor---------------------------")
print("-----------------------------------------------------------------------")
print('')
user_input = input("Do you want to Encrypt OR Decrypt the file? (E/D) ")


if(user_input == 'E' or user_input == 'e'):
    print("Encrypting...")
    #Encrypts the text that is saved as a variable 
    def encrypt(text, shift, alphabets):

        def shift_alphabet(alphabet):
            return alphabet[shift:] + alphabet[:shift]

        shifted_alphabet = tuple(map(shift_alphabet, alphabets))
        final_alphabet = ''.join(alphabets)
        final_shifted_alphabet = ''.join(shifted_alphabet)
        table = str.maketrans(final_alphabet, final_shifted_alphabet)
        return text.translate(table)
    
    encrypted_text = encrypt(plain_text, 3, [string.ascii_lowercase, string.ascii_uppercase, string.punctuation])
    write_to_file(encrypted_text)
    print("The file has been encrypted!")
elif (user_input == 'D' or user_input == 'd'):
    print("Decrypting...")
    #Decrypts the text that is saved as a variable 
    def decrypt(text, shift, alphabets):

        def shift_alphabet(alphabet):
            return alphabet[shift:] + alphabet[:shift]

        shifted_alphabet = tuple(map(shift_alphabet, alphabets))
        final_alphabet = ''.join(alphabets)
        final_shifted_alphabet = ''.join(shifted_alphabet)
        table = str.maketrans(final_alphabet, final_shifted_alphabet)
        return text.translate(table)

    decrypted_text = decrypt(plain_text, 23, [string.ascii_lowercase, string.ascii_uppercase, string.punctuation])
    write_to_file(decrypted_text)
    print("The file has been decrypted!")
else:
    print("Invalid option")
    write_to_file(plain_text)
        

        







