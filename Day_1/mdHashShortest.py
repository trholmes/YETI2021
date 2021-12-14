import hashlib as hsh, itertools as it, string
getPTX = next((plain for plain in map(''.join, it.product(string.ascii_uppercase+string.digits+string.ascii_lowercase, repeat=4)) if hsh.md5(plain.encode()).hexdigest() == "4002f685108db38f1af9965f3bc869eb"),None)
#returns string from a generated list of alphanumeric strings with length four corresponding to given mdhash and if there are none, returns None
#it.product returns list of tuples and ''.join makes them strings
#checks if mb5hash of each string in the list of strings is equal to the string we were given
print(getPTX)
