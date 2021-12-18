def decipher(ch, key):
    newindex = (vocab.index(ch) + key)%36
    true_ch = vocab[newindex]
    return true_ch


infile = 'secretCode.txt'
outfile = open("day4_result.txt",'w')

name = ["B", "I", "J", "O", "U"]    # Name of the place
key = [ord(i)-65 for i in name]     # convert to a number A = 0, B = 1 ...

alphabet = [chr(i) for i in range(65, 65 + 26)]
numbers = [str(i) for i in range(10)]

vocab = alphabet + numbers      # characters used in the problem

i = 0
# read characters from secret message and write deciphered characters to a file
with open(infile) as file:
    for line in file:  
        for ch in line:
            true_ch = decipher(ch.upper(), key[i])
            i = i+1
            i = i%5
            outfile.write(true_ch)