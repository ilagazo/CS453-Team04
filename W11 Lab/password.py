import math

def calculateCombinations(password):
    size = 0
    # Obtained these numbers from book (Page 229)
    symbols = 32
    number = 10
    letters = 26
    specialCharacters = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    isUpperLetterAddable = True
    isLowerLetterAddable = True
    isNumberAddable = True
    isSymbolAddable = True

    if password.isdigit():  # All numbers
        size = number
    elif password.isalpha() and password.islower():  # All lowercase
        size = letters
    elif password.isalpha() and password.isupper():  # All uppercase
        size = letters
    else:  # Mixed Case
        # Check for numbers and letters
        for character in password:
            if character.isdigit() and isNumberAddable:
                size += number
                isNumberAddable = False
            elif character.isupper() and isUpperLetterAddable:
                size += letters
                isUpperLetterAddable = False
            elif character.isalpha() and isLowerLetterAddable:
                size += letters
                isLowerLetterAddable = False
        # Check for special chracters
        if any(character in specialCharacters for character in password):
            if(isSymbolAddable):
                size += symbols
                isSymbolAddable = False

    combinations = size**len(password)
    print("There are " + str(combinations) + " combinations\n")
    return combinations


def promptPassword():
    password = ''
    print("Please enter the password:")
    password = input("")
    return password

def calculateBitStrength(combinations):
    if (combinations != 0):
        print("That is equivalent to a key of " + str(int(math.log2(combinations))) + " bits\n")
    else:
        print("Bit Strength is 0.\n")


def runProgram():
    password = promptPassword()
    combinations = calculateCombinations(password)
    calculateBitStrength(combinations)

def main():
    choice = "0"
    while choice == "0":
        print("Enter 1 for manual test.\nEnter 2 to exit program.\n")
        choice = input("> ")
        if(choice == "1"):
            runProgram()
            choice = "0"
        elif(choice == "2"):
            return
        else:
            choice = "0"
            print("Only enter 1 or 2.")

main()
