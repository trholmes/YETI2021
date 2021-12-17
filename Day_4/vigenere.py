import string
characters = string.ascii_lowercase+string.digits
def encodeMessage(key,message):
    encrypted = []
    keyLen=len(key)
    for index, char in enumerate(message):
        charPos = characters.find(char)
        #initial position of character in letters
        charPos += characters.find(key[index%keyLen]) #shifting
        #index%keyLen cycles through the key
        charPos %= len(characters) #accounting for wraparound
        encrypted.append(characters[charPos].upper())
    return "".join(encrypted)

f = open("secretCode.txt")
text = f.read()
f.close()

with open('encrypted.txt','a') as g:
    g.write(encodeMessage('bijou',text))

