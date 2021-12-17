
def vignere_encode(key, plaintext, alphabet):
    # we could change the alphabet, so forst make a mapping of the alphabet
    map_to_num = {}
    map_from_num = {}
    for i in range(len(alphabet)):
        map_to_num[alphabet[i]] = i
        map_from_num[i] = alphabet[i]
    # map the key and plaintext using the mapping
    plaintext_mapped = [map_to_num[i] for i in plaintext.upper()]
    key_mapped = [map_to_num[i] for i in key.upper()]
    keylen = len(key_mapped)
    alphabetlen = len(alphabet)
    # apply the shift
    for i in range(len(plaintext_mapped)):
        plaintext_mapped[i] = (plaintext_mapped[i] + key_mapped[i % keylen]) % alphabetlen
    # keeping all this in memory while encrpyting isn't 
    # safe, but then again, neither is using vignere
    return "".join([map_from_num[i] for i in plaintext_mapped])

def vignere_decode(key, ciphertext, alphabet):
    # we could change the alphabet, so forst make a mapping of the alphabet
    map_to_num = {}
    map_from_num = {}
    for i in range(len(alphabet)):
        map_to_num[alphabet[i]] = i
        map_from_num[i] = alphabet[i]
    # map the key and plaintext using the mapping
    ciphertext_mapped = [map_to_num[i] for i in ciphertext.upper()]
    key_mapped = [map_to_num[i] for i in key.upper()]
    keylen = len(key_mapped)
    alphabetlen = len(alphabet)
    # apply the shift
    for i in range(len(ciphertext_mapped)):
        ciphertext_mapped[i] = (ciphertext_mapped[i] - key_mapped[i % keylen]) % alphabetlen
    # keeping all this in memory while encrpyting isn't 
    # safe, but then again, neither is using vignere
    return "".join([map_from_num[i] for i in ciphertext_mapped])

encode_test_alphabet = [i for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
encode_tests = [
    # key, plaintext, ciphertext
    ("ABCDABCDABCDABCDABCDABCDABCD", "cryptoisshortforcryptography", "CSASTPKVSIQUTGQUCSASTPIUAQJB"),
    ("LIONLIONLIONLIONLIONLIONLIONLIONLIO", "thequickbrownfoxjumpsoverthelazydog", "EPSDFQQXMZCJYNCKUCACDWJRCBVRWINLOWU")
]
for i in encode_tests:
    if vignere_encode(i[0], i[1], encode_test_alphabet) != i[2]:
        print(f"encode fails for {i[1]}")
    if vignere_decode(i[0], i[2], encode_test_alphabet) != i[1].upper():
        print(f"decode fails for {i[2]} expected {i[1]} but got {vignere_decode(i[0], i[2], encode_test_alphabet)}")


addresses = []
with open("../data/possibleaddress.txt", "r") as fp:
    addresses =  fp.readlines()

nowsaddresses = [i.replace(" ", "").replace("\n", "").upper() for i in addresses]

for i in nowsaddresses:
    print(i)

current_alphabet = [i for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"]
targetciphertext = ''
with open("../secretCode.txt", "r") as fp:
    targetciphertext = [i.replace("\n", "").upper() for i in fp.readlines()][0]


#possibleplaintexts= {}
# don't need to write it to a file anymore

##for i in nowsaddresses:
##    possibleplaintexts[f"{i}_encode"] = vignere_encode(i, targetciphertext, current_alphabet)
##    possibleplaintexts[f"{i}_decode"] = vignere_decode(i, targetciphertext, current_alphabet)

#    with open(f"../data/possibleplaintext/{i}encode.txt", "w+") as fp:
#        fp.write(vignere_encode(i, targetciphertext, current_alphabet))
#    with open(f"../data/possibleplaintext/{i}decode.txt", "w+") as fp:
#        fp.write(vignere_decode(i, targetciphertext, current_alphabet))

# i think the key is actually bijou, so let's play with that
# based on the output, I think that is hex, so let's rebuild it into characters
# and see if we can find anthing from it?
hexstr = []
chosenkey=  "BIJOU"
print(f"Encoding with {chosenkey}")
cand = vignere_encode(chosenkey, targetciphertext, current_alphabet)
print("writing to file")
with open("decomp.txt", "w+") as fp:
    fp.write(bytes.fromhex(cand).decode("utf-32"))