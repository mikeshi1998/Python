# Yuchen Shi
# ITP115, Spring 2018
# Assignment A4
# yuchensh@usc.edu

# Part 2: Encrypt/Decrypt
goOn="y"
while goOn.lower()=="y":
    originalAlphabet=list("abcdefghijklmnopqrstuvwxyz")
    message=input("Enter a message: ")
    number=int(input("Please enter a number to shift by (0-25): "))
    part=originalAlphabet[0:number]
    cipherAlphabet=originalAlphabet+part
    for letter in part:
        cipherAlphabet.remove(letter)
    encrypted=[]
    for letter2 in message:
        if letter2 in originalAlphabet:
            letter2=cipherAlphabet[originalAlphabet.index(letter2)]
            encrypted.append(letter2)
        else:
            encrypted.append(letter2)

    delimiter=""
    encryptedMessage=delimiter.join(encrypted)
    print("Encrypting message...\n\tEncrypted message::", encryptedMessage)

    decrypted=[]
    for letter3 in encryptedMessage:
        if letter3 in cipherAlphabet:
            letter3=originalAlphabet[cipherAlphabet.index(letter3)]
            decrypted.append(letter3)
        else:
            decrypted.append(letter3)
    decryptedMessage=delimiter.join(decrypted)
    print("Decrypting message...\n\tDecrypted message:", decryptedMessage, "\n\tOriginal message:", message)
    goOn=input("Do you want to encrypt/decrypt another message? (y/n) ")