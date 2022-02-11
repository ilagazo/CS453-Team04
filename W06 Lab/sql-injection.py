from hmac import compare_digest
import platform
    
# PART 01: Query Generation
# Write a function to accept two strings (username and a password) and return a single string (SQL) representing
# the query used to determine if a user is authenticated on a given system. The query will be similar to one
# presented in the textbook. Provide the code for the function in the report and a couple sentences justifying
# that it works the way one would expect.
#
# Generate a set of cases (one for each member of your team) that represent valid input where the username and the
# password consist of letters, numbers, and underscores. Create a function that feeds these test cases through the
# query function and displays the resulting query. Provide the code in the report, a sample of the output from the
# function, and a couple sentences justifying why the test cases provide adequate coverage of the valid input.

def genQuery(username, password):
    sqlQuery = (f"SELECT authenticate FROM passwordList WHERE name='{username}' and passwd='{password}';")
#    print(f" SQL Query: {sqlQuery}\n")
    return sqlQuery

# PART 02: Vulnerabilities
# Generate test cases (again, each team member should generate one test case) that demonstrate a tautology attack.
# Create a function that feeds these test cases through the query function and displays the output. Provide the code,
# output, and justification in the lab report.
#
# Do the same thing for a union query attack, an additional statement attack, and a comment attack. As with tautology,
# each attack must be demonstrated with a separate set of test cases, a separate function feeding the test cases to
# the query function, and justification in the lab report.

def testValid():
    test1 = ["This_1s_A_u5ern4me", "This_1s_A_p455w0rd"]

    print(f"Test 1:\n Username: {test1[0]}\n Password: {test1[1]}")
    print(genQuery(test1[0], test1[1]))

def shaunTest():
    #tautology attack
    #union query attack
    #additional statement attack
    #comment attack
    return 1

def collinTest():
    #tautology attack
    #union query attack
    #additional statement attack
    #comment attack
    return 1
def ivanroTest():
    #tautology attack
    #union query attack
    #additional statement attack
    #comment attack
    return 1

def steveTest():
    #tautology attack
    #union query attack
    #additional statement attack
    #comment attack
    return 1

def camilaTest():
    #tautology attack
    #union query attack
    #additional statement attack
    #comment attack
    return 1

def davanTest():
    #tautology attack
    #union query attack
    #additional statement attack
    #comment attack
    return 1

# PART 03: Weak Mitigation
# Create a function to provide a weak mitigation against all four attacks. This function accepts the input as a parameter
# (or two!) and returns the sanitized input. In the lab report, provide the code, the output of the various test cases,
# and justification that the code represents a weak mitigation to the four attack types.

def weakMitigation(userName, userPassword):
    #tautology attack
    #union query attack
    #additional statement attack
    #comment attack
    print(genQuery(userName, userPassword))

# PART 04: Strong Mitigation
# Create a function to provide a strong mitigation against all command injection attacks. Provide the code, output showing
# that the valid test cases still work, output showing that all four malicious inputs are mitigated, and a justification
# the approach works the way one would expect.

def strongMitigation(userName, userPassword):
    #tautology attack
    #union query attack
    #additional statement attack
    #comment attack
    print(genQuery(userName, userPassword))
    
def manualTest():
    userName = getUserName()
    userPassword = getUserPassword()
    
    weakMitigation(userName, userPassword)
    strongMitigation(userName, userPassword)


def automatedTest():
    testValid()
    shaunTest()
    collinTest()
    ivanroTest()
    steveTest()
    camilaTest()    
    davanTest()

def getUserName():
    print("Please enter username: ")
    userName = input("> ")
    return userName

def getUserPassword():
    print("Enter Password: ")
    userPassword = input("> ")
    return userPassword

def main():
    option = "0"
    while option == '0':
        print("Please select an option:\n Enter 1 for manual test\n Enter 2 for automated tests\n Enter 3 to end program execution")
        option = input("> ")
        if(option == '1'):
            manualTest()
            option = '0'
        elif(option == '2'):
            automatedTest()
            option = '0'
        elif(option == '3'):
            print("SQL Injection Program Ended. Goodbye!")
        else:
            option = '0'
            print("Invalid Input! Please select a valid input (i.e. 1,2,3")

#  Run Main
main();
