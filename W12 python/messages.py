########################################################################
# COMPONENT:
#    MESSAGES
# Author:
#    Br. Helfrich, Kyle Mueller, <your name here if you made a change>
# Summary: 
#    This class stores the notion of a collection of messages
########################################################################

import control, message

##################################################
# MESSAGES
# The collection of high-tech messages
##################################################
class Messages:

    ##################################################
    # MESSAGES CONSTRUCTOR
    # Read a file to fill the messages
    ##################################################
    def __init__(self, filename):
        self._messages = []
        self._read_messages(filename)
        self._control = control.PUBLIC

    ##################################################
    # MESSAGES :: DISPLAY
    # Display the list of messages
    ################################################## 
    def display(self, controlData):
        for m in self._messages:
            #userControl=control.getControlLevel(m._control)
            #if (control.getReadControlLevel(userControl, controlData)):
            m.display_properties()

    ##################################################
    # MESSAGES :: SHOW
    # Show a single message
    ################################################## 
    def show(self, id, controlData):
        for m in self._messages:
            if m.get_id() == id:
                userControl=control.getControlLevel(m._control)
                if (control.getReadControlLevel(userControl, controlData)):
                    m.display_text()
                else:
                    print("Read Access Denied")
                return True
        return False

    ##################################################
    # MESSAGES :: UPDATE
    # Update a single message
    ################################################## 
    def update(self, id, text, controlData):
        for m in self._messages:
            if m.get_id() == id:
                userControl=control.getControlLevel(m._control)
                if (control.getWriteControlLevel(userControl, controlData)):
                    m.update_text(text, controlData)
                else: 
                    print("Write Access Denied")

    ##################################################
    # MESSAGES :: REMOVE
    # Remove a single message
    ################################################## 
    def remove(self, id, controlData):
        for m in self._messages:
            if m.get_id() == id:
                userControl=control.getControlLevel(m._control)
                if (control.getWriteControlLevel(userControl, controlData)):
                    m.clear()
                else:
                    print("Remove Access Denied")

    ##################################################
    # MESSAGES :: ADD
    # Add a new message
    ################################################## 
    def add(self, text, author, date, controlData):
        m = message.Message(text, author, date, controlData)
        self._messages.append(m)

    ##################################################
    # MESSAGES :: READ MESSAGES
    # Read messages from a file
    ################################################## 
    def _read_messages(self, filename):
        try:
            with open(filename, "r") as f:
                for line in f:
                    text_control, author, date, text = line.split('|')
                    self.add(text.rstrip('\r\n'), author, date, text_control)

        except FileNotFoundError:
            print(f"ERROR! Unable to open file \"{filename}\"")
            return
