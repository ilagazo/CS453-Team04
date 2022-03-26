########################################################################
# COMPONENT:
#    CONTROL
# Author:
#    Br. Helfrich, Kyle Mueller, <your name here if you made a change>
# Summary: 
#    This class stores the notion of Bell-LaPadula
########################################################################

def check_auth(user_auth, message_auth):
    conditions = ["Secret",  "Privileged", "Confidential", "Public"]
    try: 
        user_index = conditions.index(user_auth)
        message_index = conditions.index(message_auth)
    except:
        print("Not a valid security clearance.")

    if(user_index >= message_index):
        return True
    else:
        return False