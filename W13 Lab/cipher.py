##############################################################################
# COMPONENT:
#    CIPHER01
# Author:
#    Br. Helfrich, Kyle Mueller, <your name here if you made a change>
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
        return "Vigenère Cipher"

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
    # ENCRYPT
    # TODO: ADD description
    ##########################################################################
    def getKey(self, key, plainText):
        key = list(key)

        if len(plainText) == len(key):
            return key
        else:
            for i in range(len(plainText) - len(key)):
                key.append(key[i % len(key)])
            return ("" . join(key))

    def encrypt(self, plainText, key):
        ciphertext = []

        for i in range(len(plainText)):
            cipherLetter = (ord(plainText[i]) +
                            ord(key[i])) % self.alphabetSize
            cipherLetter += ord('A')
            ciphertext.append(chr(cipherLetter))

        return ("" . join(ciphertext))

    ##########################################################################
    # DECRYPT
    # TODO: ADD description
    ##########################################################################
    def decrypt(self, cipherText, key):
        decryptedCipher = []

        for i in range((len(cipherText))):
            decryptedLetter = (ord(cipherText[i]) - ord(key[i]) + self.alphabetSize) % self.alphabetSize
            decryptedLetter += ord('A')
            decryptedCipher.append(chr(decryptedLetter))
        return ("" . join(decryptedCipher))
