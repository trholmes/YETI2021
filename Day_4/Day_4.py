class VigenereDecrypter:
    def __init__(self, key, encrypted_text):
        self.encrypted_text = encrypted_text
        k = []
        k.append(key)
        if(len(encrypted_text) != len(key)):
            for i in range(len(encrypted_text) - len(key)):
                k.append(key[i%len(key)])
        self.key = ''.join(k)

        self.d = {}
        count=0
        for c in 'abcdefghijklmnopqrstuvwxyz1234567890':
            self.d[c] = count;
            count += 1 

        self.inv_d = {v: k for k, v in self.d.items()}

    def decrypt(self):
        message = []
        for i in range(len(self.encrypted_text)):
            x = (self.d[self.encrypted_text[i]] - self.d[self.key[i]] + 36)%36
            x += self.d['a']
            message.append(self.inv_d[x])
        return ''.join(message)
        

def main():
    #The building address is 803 S Gay Street and the name is Bijou Theatre
    key = 'bijou'
    with open('secretCode.txt', 'r') as f:
        data = f.read()

    decrypter = VigenereDecrypter(key, data)
    plain_text = decrypter.decrypt()
    with open('plainText.txt', 'w') as f1:
        f1.write(plain_text)

if __name__=='__main__':
    main()
