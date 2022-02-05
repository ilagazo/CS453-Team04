# //Forbidden Path: /home/user/secret/password.txt
#/home/../home/../home/user/./secret/password.txt

# // Assigned to: Collin Brown
# // 
# // Create a canonicalization function to convert an encoding (the input path) into some canon. 
# // This function will then be used to see if two file paths are homographs of each other. 
# // Note that you are not allowed to use the canonical() function available in the <filesystem> library. 
# // If using Python, you are not allowed to use anything in the os.path library.


# // Assigned to: 
# // 
# // Create a homograph function that determines if two file paths are the same. 
# // It should make use of the work done by the canonicalization function. 
# // See the textbook for an idea of what this should look like. 
# // This function should return True or False to indicate whether the two encodings are the same.


# // Assigned to:
# // 
# // Write a function to compare each of your non homograph test cases against a forbidden file path to demonstrate that they are different (not homographs). 
# // In your report, justify why each test case in the "Non Homographs" set is not equivelent to the forbidden file and why the set of test cases is 
# // representative of distinct file paths.Your test cases should account for the current working directory and should cover the range of possible symbols for your operating system.


# // Assigned to:
# // 
# // Write a function to compare each of your homograph test cases against a forbidden file path to demonstrate that they are the same. 
# // In your report, justify why each test case in the "Homographs" set is equivelent to the forbidden file. 
# // Your set of test cases should cover the range of possible homograph paths for your operating system. 
# // Justify why the set of test cases is representative of equivelent file paths.


# // Assigned to:
# // 
# // Demonstrate that all of the paths in "Non Homographs" are not homographs and that all the paths in "Homographs" are in fact homographs. 
# // This demonstration is in the form of program output and descriptive text explaining what the output means. When generating these test cases, 
# // it is a good rule of thumb to have 2-3 test cases per construct. For example, have 2-3 test cases to verify that the single-dot "./" works as you expect.

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
#    if(compare == 1):
#        print("Paths are homographs\n")
#    else:
#        print("Paths are not homographs\n")

# This is where the manual tests will be built
def automatedTest():
    nonHomographs()
    homographs()

def nonHomographs():
    forbiddenPath = "/home/user/secret/password.txt"
    test1 = "home/user/secret/password.txt"
    test2 = "home/user/secret/password.txt"
    test3 = "home/user/secret/password.txt"
    print("Non-Homographs tests for this forbidden path " + forbiddenPath)

#Test 1
    print("Test 1 " + test1)
    runTest(forbiddenPath, test1)

#Test 2
    print("Test 2 " + test2)
    runTest(forbiddenPath, test2)

#Test 3
    print("Test 3 " + test3)
    runTest(forbiddenPath, test3)

def homographs():
    forbiddenPath = "/home/user/secret/password.txt"
    test1 = "/home/../home/../home/user/secret/password.txt"
    test2 = "/home/user/../../home/user/secret/password.txt"
    test3 = "/home/user/./secret/password.txt"
    test4 = "/home/../home/../home/user/./secret/password.txt"
    print("Homographs tests for this forbidden path " + forbiddenPath)

    #Test 1 Demonstrates a single ../ back directory   
    print("Test 1 " + test1)
    runTest(forbiddenPath, test1)
    
    #Test 2 Demonstrates a double back directory
    print("Test 2 " + test2)
    runTest(forbiddenPath, test2)
    
    #Test 3 Demonstrates a ./ calling the current directory
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
# for code testing    print(runTest(canon("/home/user/secret/password.txt"),canon("/home/user/cse453/./../secret/password.txt")))
        
        


# //output..

main();

#     return 0;

# }

# /**************************************************************************************************
# * Create a homograph function that determines if two file paths are the same. 
# * It should make use of the work done by the canonicalization function. 
# * See the textbook for an idea of what this should look like. 
# * This function should return True or False to indicate whether the two encodings are the same.
# ***************************************************************************************************/
# bool Homograph()
# {
# //H(e1,e2) H(filepath 1 filepath 2, )
# // if filepath 1 = filepath 2 = true
# // C()canonicalization function

# }