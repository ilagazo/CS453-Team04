# PART 01:
# Write a function to accept two strings (username and a password) and return a single string (SQL) representing
# the query used to determine if a user is authenticated on a given system. The query will be similar to one
# presented in the textbook. Provide the code for the function in the report and a couple sentences justifying
# that it works the way one would expect.

def main():
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


# PART 02:
# Generate a set of cases (one for each member of your team) that represent valid input where the username and the
# password consist of letters, numbers, and underscores. Create a function that feeds these test cases through the
# query function and displays the resulting query. Provide the code in the report, a sample of the output from the
# function, and a couple sentences justifying why the test cases provide adequate coverage of the valid input.


main();