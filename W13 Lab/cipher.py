##############################################################################
# COMPONENT:
#    CIPHER01
# Author:
#    Br. Helfrich, Kyle Mueller
# Summary:
#    Implement your cipher here. You can view 'example.py' to see the
#    completed Caesar Cipher example.
##############################################################################


##############################################################################
# CIPHER
##############################################################################
class Cipher:
    def __init__(self):
        # TODO: Insert anything you need for your cipher here
        # pass
        self.alphabetSize = 26  # A-Z

    def get_author(self):
        return "Ivanro Lagazo"

    def get_cipher_name(self):
        return "Vigenère Cipher\n"\
                "PLEASE NOTE THAT THIS CIPHER ONLY WORKS WITH UPPERCASE TEXT AND PASSWORDS"

    ##########################################################################
    # GET CIPHER CITATION
    # Returns the citation from which we learned about the cipher
    ##########################################################################
    def get_cipher_citation(self):
        return "Vigenere cipher | Definition, Table, Example, & Facts | Britannica. (2022). In Encyclopædia Britannica.\n" \
            "https://www.britannica.com/topic/Vigenere-cipher \n\n" \
            "The Vigenère Cipher Encryption and Decryption. (2022). Mtu.edu.\n" \
            "https://pages.mtu.edu/~shene/NSF-4/Tutorial/VIG/Vig-Base.html"

    ##########################################################################
    # GET PSEUDOCODE
    # Returns the pseudocode as a string to be used by the caller
    ##########################################################################
    def get_pseudocode(self):
        # TODO: This function should return your psuedocode, neatly formatted

        # The encrypt pseudocode
        pc = "encrypt(plainText,password)\n" \
             "   cipher <- array[]\n" \
             "   key <- getKey\n" \
             "   FOR i is all values of plainText\n" \
             "       cipherLetter = (ord(plainText[i]) + ord(key[i])) % alphabetSize\n" \
             "       cipherLetter += ord('A')\n" \
             "       cipher.append(cipherLetter)\n" \
             "   RETURN cipher\n\n"

        # The decrypt pseudocode
        pc += "decrypt(cipher, password)\n" \
              "   decryptedCipher <- array[]\n" \
              "   FOR i is all values of cipher\n" \
              "       decryptedLetter = (ord(cipher[i]) - ord(password[i]) + alphabetSize) % alphabetSize\n" \
              "       decryptedLetter += ord('A')\n" \
              "       decryptedCipher.append(decryptedLetter)\n" \
              "   RETURN decryptedCipher\n\n"

        return pc

    ##########################################################################
    # GETKEY
    # Ensures that the key provided is the same length as the message provided
    ##########################################################################
    def getKey(self, key, plainText):
        key = list(key)

        if len(plainText) == len(key):
            return key
        else:
            for i in range(len(plainText) - len(key)):
                key.append(key[i % len(key)])
            return ("" . join(key))

    ##########################################################################
    # ENCRYPT
    # Encrypts the text provided using the password as a key
    ##########################################################################
    def encrypt(self, plainText, key):
        if(self.validateInput(plainText, key)):
            ciphertext = []

            for i in range(len(plainText)):
                cipherLetter = (ord(plainText[i]) +
                                ord(key[i])) % self.alphabetSize
                cipherLetter += ord('A')
                ciphertext.append(chr(cipherLetter))

            return ("" . join(ciphertext))
        else:
            return 'ERROR: PASSWORD ENTERED MUST BE ALL UPPERCASE LETTERS ONLY'

    ##########################################################################
    # DECRYPT
    # Decrypts the text using the cipher created from encryption and the
    # provided password
    ##########################################################################
    def decrypt(self, cipherText, key):
        if(self.validateInput(cipherText, key)):
            decryptedCipher = []

            for i in range((len(cipherText))):
                decryptedLetter = (ord(cipherText[i]) - ord(key[i]) + self.alphabetSize) % self.alphabetSize
                decryptedLetter += ord('A')
                decryptedCipher.append(chr(decryptedLetter))
            return ("" . join(decryptedCipher))
        else:
            return 'ERROR: PASSWORD ENTERED MUST BE ALL UPPERCASE LETTERS ONLY'


    ##########################################################################
    # VALIDATEINPUT
    # Vigenère Cipher only works with capital letters so this function ensures
    # that the provided inputs are capital letters only
    ##########################################################################
    def validateInput(self,text, password):
        if text.isalpha() and password.isalpha() and text.isupper():
            return True
        else:
            return False