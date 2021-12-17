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
        for c in 'abcdefghijklmnopqrstuvwzyx1234567890':
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
        for c in 'abcdefghijklmnopqrstuvwzyx1234567890':
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
    key = 'bijou'
    with open('secretCode.txt') as f:
        data = f.read()

    decrypter = VigenereDecrypter(key, data)
    print(decrypter.decrypt())

if __name__=='__main__':
    main()
