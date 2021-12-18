class VigenereEncrypter:
    def __init__(self, key, plain_text):
        self.plain_text = plain_text
        k = []
        k.append(key)
        if(len(plain_text) != len(key)):
            for i in range(len(plain_text) - len(key)):
                k.append(key[i%len(key)])
        self.key = ''.join(k)

        self.d = {}
        count=0
        for c in 'abcdefghijklmnopqrstuvwxyz0123456789':
            self.d[c] = count;
            count += 1 

        self.inv_d = {v: k for k, v in self.d.items()}

    def encrypt(self):
        cipher_text = []
        for i in range(len(self.plain_text)):
            x = (self.d[self.plain_text[i]] + self.d[self.key[i]])%36
            x += self.d['a']
            cipher_text.append(self.inv_d[x])
        return ''.join(cipher_text)

def main():
    #The building address is 803 S Gay Street and the name is Bijou Theatre
    key = 'bijou'
    with open('secretCode.txt', 'r') as f:
        data = f.read()

    encrypter = VigenereEncrypter(key, data)
    cipher_text = encrypter.encrypt()
    with open('encodedText.txt', 'w') as f1:
        f1.write(cipher_text)

if __name__=='__main__':
    main()
