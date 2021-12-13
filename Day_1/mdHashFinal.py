import hashlib as hsh, itertools as it, string

characters=string.ascii_uppercase+string.digits+string.ascii_lowercase
plaintxt = map(''.join, it.product(characters, repeat=4)) #list of all possible alphanumeric strings length four
hashStr = lambda plaintxt: hsh.md5(plaintxt.encode()).hexdigest() #makes it so you can compare the values
getptx = lambda hash: next((plain for plain in plaintxt if hashStr(plain) == hash),None) #returns string corresponding to given mdhash and if there are none, returns None
print(getptx("4002f685108db38f1af9965f3bc869eb"))

