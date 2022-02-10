# //Forbidden Path: /home/user/secret/password.txt

from hmac import compare_digest
import platform

#################################################################################################
# list of functions
# canon(path)                       takes a given path and canonizes it.
# runTest(filePath1, filePath2)     compares two file paths. Uses canon to make them comparable.
# manualTest()                      Allows for user to input two paths to be compared.
# automatedTest()                   Runs all the automated test.
# nonHomographs()                   Runs tests for Non-Homograph examples.
# homographs()                      Runs tests for Homograph examples.
# main()                            Driving function
#################################################################################################

#cannonizes the path given
def canon(path):
    canon = []
    result = ''
    temp = ''

    if(platform.system() == 'Windows'):
        slash = '/'
    else:
        slash = '\''

    directories = path.split(slash)

    for x in directories:
        if(x == ".."):
            if(x != temp):
                temp = canon.pop()
        if(x != "." and x != ".."):
            canon.append(x)
    for x in range(len(canon)):
        result += f'{canon[x]}{slash}'

    return result

# compares two canonized values to see if they are homographs
def runTest(filePath1, filePath2):
    homograph = 0
    print(filePath1 + "\nand\n" + filePath2)
    if(canon(filePath1) == canon(filePath2)):
        homograph = 1
        print("are Homographs\n")
    else:
        print("are Non-Homographs\n")
    return homograph

# user entered tests
def manualTest():
    file_1 = ""
    file_2 = ""

    print("Specify the first filename: ")
    filename1 = input("> ")
    
    print("Specify the second filename: ")
    filename2 = input("> ")
    runTest(filename1,filename2)

# This is where the manual tests will be built
def automatedTest():
    nonHomographs()
    homographs()

# various tests of Non-Homograph paths
def nonHomographs():
    forbiddenPath = "/home/user/secret/password.txt"
    test1 = "home/user/secret/password.txt"
    test2 = "/home/user/.././secret/password.txt"
    test3 = "/home/../user/secret/password.txt"
    print("Non-Homographs tests for this forbidden path " + forbiddenPath)

    #Test 1 test just being wrong the wrong path
    print("Test 1 " + test1)
    runTest(forbiddenPath, test1)

    #Test 2 this test uses the back directory and current directory
    print("Test 2 " + test2)
    runTest(forbiddenPath, test2)

    #Test 3 this test uses only the back directory
    print("Test 3 " + test3)
    runTest(forbiddenPath, test3)

# various test of Homograph paths
def homographs():
    forbiddenPath = "/home/user/secret/password.txt"
    test1 = "/home/../home/../home/user/secret/password.txt"
    test2 = "/home/user/../../home/user/secret/password.txt"
    test3 = "/home/user/./secret/password.txt"
    test4 = "/home/../home/../home/user/./secret/password.txt"
    print("Homographs tests for this forbidden path " + forbiddenPath)

    #Test 1 Demonstrates a single back directory   
    print("Test 1 " + test1)
    runTest(forbiddenPath, test1)
    
    #Test 2 Demonstrates a double back directory
    print("Test 2 " + test2)
    runTest(forbiddenPath, test2)
    
    #Test 3 Demonstrates calling the current directory
    print("Test 3 " + test3)
    runTest(forbiddenPath, test3)

    #Test 4 Demonstrates using both back directory and current directory
    print("Test 4 " + test4)
    runTest(forbiddenPath, test4)

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

