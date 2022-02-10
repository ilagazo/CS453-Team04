from hmac import compare_digest
import platform

def sanitizeInput(dirtyInput):
    cleanedInput = 1
    return cleanedInput

def manualTest():
    dirtyUserName = getUserName()
    dirtyUserPassword = getUserPassword()
    cleanUserName = sanitizeInput(dirtyUserName)
    cleanUserPassword = sanitizeInput(dirtyUserPassword)

    print("Pre Cleaned User Name Input " + dirtyUserName)
    print("Cleaned User Name Input " + cleanUserName)

    print("Pre Cleaned User Password Input" + dirtyUserPassword)
    print("Cleaned User Password Input" + cleanUserPassword)

def automatedTest():
    return 1

def getUserName():
    print("Enter Username: ")
    userName = input("> ")
    return userName

def getUserPassword():
    print("Enter Password: ")
    userPassword = input("> ")
    return userPassword

def main ():
    testChoice = "0"
    while testChoice == "0":
        print("Enter 1 for manual test \n      2 for automated tests \n      3 to stop testing")
        testChoice = input("> ")
        if(testChoice == "1"):
            manualTest()
            testChoice="0"
        elif (testChoice == "2"):
            automatedTest()
            testChoice = "0"
        elif(testChoice == "3"):
            return
        else:
            testChoice="0"
            print("Only 1, 2 or 3 are acceptable inputs")
        
# //output..

main()