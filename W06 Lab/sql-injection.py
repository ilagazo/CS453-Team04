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

def promptUser():
    username = ""
    password = ""

    print("Please enter username:")
    username = input("> ")

    print("Please enter password:")
    password = input("> ")

    sqlQuery = genQuery(username,password)
    print(sqlQuery)



def genQuery(username, password):
    sqlQuery = (f"SELECT authenticate FROM passwordList WHERE name='{username}' and passwd='{password}';")
    return sqlQuery

# PART 02: Vulnerabilities
# Generate test cases (again, each team member should generate one test case) that demonstrate a tautology attack.
# Create a function that feeds these test cases through the query function and displays the output. Provide the code,
# output, and justification in the lab report.
#
# Do the same thing for a union query attack, an additional statement attack, and a comment attack. As with tautology,
# each attack must be demonstrated with a separate set of test cases, a separate function feeding the test cases to
# the query function, and justification in the lab report.



# PART 03: Weak Mitigation
# Create a function to provide a weak mitigation against all four attacks. This function accepts the input as a parameter
# (or two!) and returns the sanitized input. In the lab report, provide the code, the output of the various test cases,
# and justification that the code represents a weak mitigation to the four attack types.



# PART 04: Strong Mitigation
#Create a function to provide a strong mitigation against all command injection attacks. Provide the code, output showing
# that the valid test cases still work, output showing that all four malicious inputs are mitigated, and a justification
# the approach works the way one would expect.


def main():
    promptUser()

#  Run Main
main();