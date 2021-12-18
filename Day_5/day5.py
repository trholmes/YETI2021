import numpy as np
import matplotlib.pyplot as plt


def fib(n):
    a = 0
    b = 1
    
    if n <= 0:
        return "invalid"
         
    elif n == 1:
        return 0
       
    elif n == 2:
        return 1
    
    else:
        for i in range(n-2):
            c = a + b
            a = b
            b = c
        return b
    
    
filename = "day4_result.txt"  # input file

even9 = fib( (9-1)*3 + 1 ) # 9th even number based on the even odd pattern in fib sequence
odd6 = fib( int(6/2) * 3 ) # 6th odd number based on the even odd pattern in fib sequence

width = int(even9/odd6)

# read the decoded text string
with open(filename) as infile:
    textstring = infile.readline()
    
total_characters = len(textstring) 
height = int(total_characters/width/3/2)


image = np.zeros([height, width, 3], dtype=int)


k = 0
for i in range(height):
    for j in range(width):
        image[i][j] = [int(textstring[k:k+2], 16), int(textstring[k+2:k+4], 16), int(textstring[k+4:k+6], 16)]
        k = k + 6
        
plt.figure(figsize = (15,15))
plt.imshow(image)
plt.savefig("day5_result.png")