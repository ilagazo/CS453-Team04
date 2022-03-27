########################################################################
# COMPONENT:
#    CONTROL
# Author:
#    Br. Helfrich, Kyle Mueller, <your name here if you made a change>
# Summary: 
#    This class stores the notion of Bell-LaPadula
########################################################################

PUBLIC       = 1
CONFIDENTIAL = 2 
PRIVILEGED   = 3
SECRET       = 4
 #this is not in the book. I am puting it 4 like it was TOP_SECRET

Control = {
            "PUBLIC"        : PUBLIC
           ,"CONFIDENTIAL"  : CONFIDENTIAL
           ,"PRIVILEGED"    : PRIVILEGED
           ,"SECRET"        : SECRET }

def getControlLevel(controlUser):
  if(type(controlUser) == int):
    return controlUser
  return Control[controlUser.upper()]

def compareControlLevel(control, controlUser, type):
    if(type): #write
       return getControlLevel(controlUser) <= control
    else: #read
       return getControlLevel(controlUser) >= control

def getWriteControlLevel(control, controlUser):
  return compareControlLevel(control, controlUser,1)

def getReadControlLevel(control, controlUser):
  return compareControlLevel(control, controlUser,0)
