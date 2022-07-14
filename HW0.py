# Created by Joel Nail
# MIS385N HW0 - Python Programming

# input text can be any printable ASCII character except Space and !
# N is the number of positions to shift characters by. It must be >= 1
# D denotes the direction of the shift. It must be either -1 or +1
def customEncrypt(inputText, N, D):
    # reverses inputText and stores it in a variable
    reversedText = inputText[::-1]

    # creates an empty string which will be used to store the new encrypted text
    encryptedText = ""

    # prevents the algorithm from running in case of invalid input for N
    if N < 1:
        raise Exception("N not equal to or greater than 1")

    # prevents the algorithm from running in case of invalid input for D
    if D != 1 and D != -1:
        raise Exception("D not equal to -1 or 1")

    # loops through inputText and prevents algorithm from running if any characters are invalid
    # depending on the value of D, new Ascii values are assigned based on the inputText
    # the new values are added to the encryptedText variable which is then returned by the function
    for i in range(len(reversedText)):
        asciiVal = ord(reversedText[i])
        # prevents algorithm from running in case of invalid input
        if asciiVal < 34 or asciiVal > 126:
            raise Exception("Input contains invalid ASCII characters")

        if D == 1:
            newAsciiVal = asciiVal + N

            # loops back to the beginning of our acceptable list of characters if newAsciiValue is invalid (>126)
            if newAsciiVal > 126:
                newAsciiVal = (newAsciiVal % 92) - 1

            encryptedText += chr(newAsciiVal)

        if D == -1:
            newAsciiVal = asciiVal - N

            # loops back to the end of our acceptable list of characters if newAsciiValue is invalid (<34)
            if newAsciiVal < 34:
                newAsciiVal = 34 - newAsciiVal
                newAsciiVal = (newAsciiVal % 92)
                newAsciiVal = 127 - newAsciiVal

            encryptedText += chr(newAsciiVal)

    return encryptedText

# function to test the customEncrypt algorithm by prompting user for input and returning the matching ciphertext
def testCustomEncrypt():

    print("Testing Custom Encryption Algorithm")

    # prompts user for user ID and reprompts until acceptable input is given
    while True:
        badInputBool = False

        try:
            userID = input("Enter UserID as text: ")
        except ValueError:
            print("Sorry, only printable ASCII characters are allowed (except spaces and exclamation marks). Please try again.")
            continue

        for i in range(len(userID)):
            if ord(userID[i]) < 34 or ord(userID[i]) > 126:
                badInputBool = True

        if badInputBool == True:
            print("Sorry, only printable ASCII characters are allowed (except spaces and exclamation marks). Please try again.")
            continue
        else:
            break

    # prompts user for password and reprompts until acceptable input is given
    while True:
        badInputBool = False

        try:
            userPass = input("Enter password as text: ")
        except ValueError:
            print("Sorry, only printable ASCII characters are allowed (except spaces and exclamation marks). Please try again.")
            continue

        for i in range(len(userPass)):
            if ord(userPass[i]) < 34 or ord(userPass[i]) > 126:
                badInputBool = True

        if badInputBool == True:
            print("Sorry, only printable ASCII characters are allowed (except spaces and exclamation marks). Please try again.")
            continue
        else:
            break


    # prompts user for n value and reprompts until valid input is given
    while True:
        try:
            n = int(input("Enter value of n: "))
        except ValueError:
            print("Sorry, n must be greater than or equal to 1. Please try again")
            continue

        if n < 1:
            print("Sorry, n must be greater than or equal to 1. Please try again.")
            continue
        else:
            break

    # prompts user for d value and reprompts until valid input is given
    while True:
        try:
            d = int(input("Enter value of d: "))
        except ValueError:
            print("Sorry, n must be equal to 1 or -1 to indicate a direction. Please try again.")
            continue

        if d !=1 and d!=-1:
            print("Sorry, d must be equal to 1 or -1 to indicate a direction. Please try again.")
            continue
        else:
            break

    # encrypts user name and password then stores them in a variable
    # the encrypted text is then unencrypted and stored in a variable
    encryptedUserID = customEncrypt(userID, n, d)
    unencryptedUserID = customEncrypt(encryptedUserID, n, -d)
    encryptedPass = customEncrypt(userPass, n, d)
    unencryptedPass = customEncrypt(encryptedPass, n, -d)

    # prints encrypted and unencrypted userID and password
    print("Encrypted UserID: ", encryptedUserID)
    print("Encrypted Password: ", encryptedPass)
    print("Original UserID: ", unencryptedUserID)
    print("Original password: ", unencryptedPass)


def main():
    # testCustomEncrypt()

    f = open("database.txt", "r")

    for i in f:
        userInfo = i.split(" ")

        userInfo[1] = userInfo[1].replace("\n", "")

        print(customEncrypt(userInfo[0], 3, -1))
        print(customEncrypt(userInfo[1], 3, -1))
        print()


# Task 3 Answers
# 1. [asamant, Temp123], [skharel, Life15$]
# 2. aissa, bjha
# 3. Ally! because of the exclamation mark


main()
