import struct
from PIL import Image

def fibonacci(n):
    a,b = 0,1

    if n == 1: 
        return a
    elif n == 2:
        return b

    for i in range(n-2):
        tmp = a+b
        a = b
        b = tmp
    return b

def calculate_width():
    evens,odds = 0,0
    even_9th = -1
    odd_6th = -1

    i = 1
    while True:
        x = fibonacci(i)
        if x%2 == 0:
            evens += 1
            if evens == 9:
                even_9th = x
        else: 
            odds += 1 
            if odds == 6:
                odd_6th = x
        if even_9th > - 1 and odd_6th > -1 : #This means both are set now
            break
        i += 1
    return int(even_9th/odd_6th) 
    
def main():
    n = calculate_width() #width of image
    image_data = []
    count = 0
    with open('../Day_4/plainText.txt', 'r') as f:
        while True:
            block = ''
            end = False
            for i in range(6):
                c = f.read(1)
                count += 1
                if not c:
                    count -= 1 
                    end = True
                    break
                block += c
            if len(block) < 6:
                count -= len(block)
                break
            if end:
                break
            image_data.append(struct.unpack('BBB', bytes.fromhex(block)))

    length = int(count/n)
    im = Image.new('RGB', (n, length))
    im.putdata(image_data)
    im.show()

if __name__=='__main__':
    main()
