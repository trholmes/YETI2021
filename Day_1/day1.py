import hashlib
import itertools


class CodeBreaker:
    def __init__(self):
        self.alphanumeric = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.target_hash = '4002f685108db38f1af9965f3bc869eb'

    def break_code(self):
            for p in itertools.product(self.alphanumeric, repeat=4):
                x=''.join(str(i) for i in p)
                hash = hashlib.md5(x.encode('utf-8')).hexdigest()
                #print(x, hash)
                if(hash==self.target_hash):
                    return x


def main():
    codeBreaker = CodeBreaker()
    print(codeBreaker.break_code())

if __name__=='__main__':
    main()
