import hashlib as hsh, itertools as it, string
def checkHash(hash, plaintxt): return hsh.md5(plaintxt.encode()).hexdigest() == hash
#checks the hash of plain against the inputted hash
def ptxt(chars,length): return map(''.join, it.product(chars, repeat=length))
#generates all strings created from list chars with the given length
def getPTX(hash, chars): 
    decode = next((string for string in ptxt(chars,4) if checkHash(hash,string) == True),None)
    return decode
#returns string from plaintxt(chars,length) that has the desired hash, if there are none returns none 
#rests on injectivity of md5hash
print(getPTX("4002f685108db38f1af9965f3bc869eb", string.ascii_uppercase+string.digits+string.ascii_lowercase))

