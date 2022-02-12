from ast import Or
from hmac import compare_digest
import platform
import re

    
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
    print("******************************\n**********Valid Test**********\n******************************")
    #test1 = ["This1sAu5ern4me", "This1sAp455w0rd"]
    test1 = ["This_1s_A_u5ern4me", "This_1s_A_p455w0rd"]
    print(f"Test Valid:\n Username: {test1[0]}\n Password: {test1[1]}")
    weakMitigation(test1[0], test1[1])
    strongMitigation(test1[0], test1[1])

def shaunTest():
    print("*********************************\n**********Shaun's Tests**********\n*********************************")
    #tautology attack
    username = "scrook"
    password = "pass or 1=1"
    print(f"Tautology:\n Username: {username}\n Password: {password}")
    weakMitigation(username, password)
    strongMitigation(username, password)
    #union query attack
    password = "pass; UNION all Select * from passwordlist"
    print(f"Union:\n Username: {username}\n Password: {password}")
    weakMitigation(username, password)
    strongMitigation(username, password)
    #additional statement attack
    password = "pass'; INSERT into ('bill','pass')"
    print(f"Additional Statement:\n Username: {username}\n Password: {password}")
    weakMitigation(username, password)
    strongMitigation(username, password)
    #comment attack
    username = "pass';--"
    password = "lol don't need this suckers"
    print(f"Comment:\n Username: {username}\n Password: {password}")
    weakMitigation(username, password)
    strongMitigation(username, password)


def collinTest():
    print("*******************************\n**********Collin Test**********\n*******************************")
    # tautology attack 
    username = "collinbrown32"
    password = "anything or x=x"
    print(f"Tautology:\n Username: {username}\n Password: {password}")
    weakMitigation(username, password)
    strongMitigation(username, password)
    #union query attack
    username = "collinbrown32"
    password = "UNION DROP TABLE table1;"
    print(f"Union:\n Username: {username}\n Password: {password}")
    weakMitigation(username, password)
    strongMitigation(username, password)
    #additional statement attack
    username = "collinbrown32;DROP TABLE table1;"
    password = "trt334"
    print(f"Additional Statement:\n Username: {username}\n Password: {password}")
    weakMitigation(username, password)
    strongMitigation(username, password)
    #comment attack
    username = "collinbrown32#"
    password = "DROP TABLE table1;"
    print(f"Comment:\n Username: {username}\n Password: {password}")
    weakMitigation(username, password)
    strongMitigation(username, password)
    
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

def devanTest():
    #tautology
    print("*********************************\n**********Devan's Tests**********\n*********************************")
    username = "Root"
    password = 'anything or x = x' #should have parentheses around both x's and one after anything and not before anything
    print(f"Tautology:\n Username: {username}\n Password: {password}")
    weakMitigation(username, password)
    strongMitigation(username, password)
    # union query attack 
    username = ' UNION SELECT * FROM emp_details # '
    password = "a"
    print(f"Union:\n Username: {username}\n Password: {password}")
    weakMitigation(username, password)
    strongMitigation(username, password)
    # additional statement attack 
    username = ";import os; dir = '/etc/passwd'; shutil.rmtree(dir)"
    password = "justdoit"
    print(f"Additional Statement:\n Username: {username}\n Password: {password}")
    weakMitigation(username, password)
    strongMitigation(username, password)
    # comment attack 
    username = "admin#"
    password = "a"
    print(f"Comment:\n Username: {username}\n Password: {password}")
    weakMitigation(username, password)
    strongMitigation(username, password)
    

# PART 03: Weak Mitigation
# Create a function to provide a weak mitigation against all four attacks. This function accepts the input as a parameter
# (or two!) and returns the sanitized input. In the lab report, provide the code, the output of the various test cases,
# and justification that the code represents a weak mitigation to the four attack types.

def weakMitigation(userName, userPassword):
    forbidden = ["OR", "AND", "=", "UNION", ";", "/", "#", "@", "$", "~","'","\""] #List of dangerous characters
    test = 1
    print("Weak Mitigation")
    for i in forbidden:
        if(i in userName.upper() or i in userPassword.upper()):
            print(f"  Invalid input from user {userName}, use of {i} not permitted.") #Loops through user input, checking for the forbidden characters. If found, prints "Invalid"
            test = 0
    if test == 1:
        print("  Test passed: " + genQuery(userName, userPassword))

# PART 04: Strong Mitigation
# Create a function to provide a strong mitigation against all command injection attacks. Provide the code, output showing
# that the valid test cases still work, output showing that all four malicious inputs are mitigated, and a justification
# the approach works the way one would expect.

def strongMitigation(userName, userPassword):
    test = 1
    print("Strong Mitigation")
    if not re.match("^[A-Za-z0-9_-]*$", userName):
        print ("  User Name Error! Only letters and numbers allowed!")
        test = 0
    elif len(userName) > 20:
        print ("  User Name Error! Only 20 characters allowed!")
        test = 0
    elif not re.match("^[A-Za-z0-9_-]*$", userPassword):
        print ("  Password Error! Only letters and numbers allowed!")
        test = 0
    elif len(userPassword) > 20:
        print ("  Password Error! Only 20 characters allowed!")
        test = 0 
    if test == 1:
        print("  Test Passed: " + genQuery(userName, userPassword))
    
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
    devanTest()

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