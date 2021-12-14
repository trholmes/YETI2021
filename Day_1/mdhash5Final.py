import hashlib as hsh, itertools as it, string
checkHash = lambda plain, hash: hsh.md5(plain.encode()).hexdigest() == hash
#checks the hash of plain against the inputted hash
plaintxt = lambda chars,length: map(''.join, it.product(chars, repeat=length))
#generates all strings created from chars with the given length
getPTX = lambda hash, chars, length: next((plain for plain in plaintxt(chars,length) if checkHash(plain, hash) == True),None)
#returns string made from chars with given length that has the desired hash, if there are none returns none 
#rests on injectivity of md5hash
print(getPTX("4002f685108db38f1af9965f3bc869eb", string.ascii_uppercase+string.digits+string.ascii_lowercase,4))
