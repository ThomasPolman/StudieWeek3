# Caesar Cypher
code = "xuo, yji nqdjhyffu xuhu! oek sqddej huqt jxyi. oek cywxj dej uluh ru qrbu je huqt jxyi. oek feefyuxuqt! ulyb qhiedyij! yd sqiu oek te yc iehho jxekwx. rou!"
alphabet = "abcdefghijklmnopqrstuvwxyz"
decipher = ""

for letter in code:
    if letter in alphabet:
        index = alphabet.find(letter)
        decipher += alphabet[(index+10)%26]
    else:
        decipher += letter

message = "hi there! xantrippe sent me a weird message that i couldnt make sense of. but then i found out about coding in computer languages, and now i can read what she sends! shes pretty funny."
cypher = ""

for letter in message:
    if letter in alphabet:
        index = alphabet.find(letter)
        cypher += alphabet[(index-10)%26]
    else:
        cypher += letter

# Functions for known offsets     
def decoder(message, offset):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    decryption = ""
    for letter in message:
        if letter in alphabet:
            index = alphabet.find(letter)
            decryption += alphabet[(index+offset)%26]
        else:
            decryption += letter
    return decryption

def coder(message, offset):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encryption = ""
    for letter in message:
        if letter in alphabet:
            index = alphabet.find(letter)
            encryption += alphabet[(index-offset)%26]
        else:
            encryption += letter
    return encryption

# Function testing for any offset
def decoder_for_unknown_offset(message, offset=26):
    if offset == 0:
        return 0
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    decryption = ""
    for letter in message:
        if letter in alphabet:
            index = alphabet.find(letter)
            decryption += alphabet[(index+offset)%26]
        else:
            decryption += letter
    print(decryption)
    return decoder_for_unknown_offset(message, offset-1)

# Function for Vigenere decryption
def decoder_vigenere(message, keyword):
    keyword_string = ""
    while len(keyword_string) < len(message):
        keyword_string += keyword
    chopped_string = keyword_string[0:len(message)]
        
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    decryption = ""
        
    for i in range(len(message)):
        if message[i] in alphabet:
            index = alphabet.find(message[i]) - alphabet.find(chopped_string[i])
            decryption += alphabet[index%26]
        else:
            decryption += message[i]
    return decryption

def coder_vigenere(message, keyword):
    keyword_string = ""
    while len(keyword_string) < len(message):
        keyword_string += keyword
    chopped_string = keyword_string[0:len(message)]
        
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encryption = ""
        
    for i in range(len(message)):
        if message[i] in alphabet:
            index = alphabet.find(message[i]) + alphabet.find(chopped_string[i])
            encryption += alphabet[index%26]
        else:
            encryption += message[i]
    return encryption
