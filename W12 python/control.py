########################################################################
# COMPONENT:
#    CONTROL
# Author:
#    Br. Helfrich, Kyle Mueller, <your name here if you made a change>
# Summary: 
#    This class stores the notion of Bell-LaPadula
########################################################################

#def check_auth(user_auth, message_auth):
#    conditions = ["Secret",  "Privileged", "Confidential", "Public"]
#    try: 
#        user_index = conditions.index(user_auth)
#        message_index = conditions.index(message_auth)
#    except:
#        print("Not a valid security clearance.")
#
#    if(user_index >= message_index):
#        return True
#    else:
#        return False
#from enum import Enum 

#class Control(Enum):
#control = Enum("PUBLIC", "CONFIDENTIAL","PRIVILEGED", "SECRET")
PUBLIC       = 1
CONFIDENTIAL = 2 
SECRET       = 3
PRIVILEGED   = 4 #this is not in the book. I am puting it 4 like it was TOP_SECRET

Control = {
            "PUBLIC"        : PUBLIC
           ,"CONFIDENTIAL"  : CONFIDENTIAL
           ,"PRIVILEGED"    : PRIVILEGED
           ,"SECRET"        : SECRET }

def getControlLevel(controlUser):
  if(type(controlUser) == int):
    return controlUser
  elif (type(controlUser) == str):
    return Control[controlUser.upper()]

def getWriteControlLevel(control, controlUser):
  return controlUser <= control

def getReadControlLevel(control, controlUser):
  return controlUser >= control
