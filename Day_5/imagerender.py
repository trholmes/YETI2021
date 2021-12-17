# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 17:14:58 2021

@author: harin
"""
from PIL import Image, ImageColor
import numpy as np

def fib(length):
    fib = [0,1]
    for i in range(2,length):
        fib.append(fib[i-1]+fib[i-2]) #recursive fibonnaci sequence
    evens = [i for i in fib if i%2==0]
    odds = [i for i in fib if i not in evens]
    return fib, evens, odds

def renderImage(width,height,colorList):
    grid=np.reshape(colorList,(height,width)) #reshapes color list into grid
    im=Image.new('RGB',(width,height))
    for i in range(height):
        for j in range(width):
            im.putpixel((j,i), ImageColor.getcolor(grid[i,j], "RGB"))
    im.save('finalday.png')

def main():
    f = open("encrypted.txt")
    text = f.read()
    f.close()
    colorArray=np.array(["#"+text[i:i+6] for i in range(0,len(text),6)])
    #reformatting to be readable as hex colors
    fibo, evens, odds = fib(50)
    width=int(evens[8]/odds[5])
    height=int((len(colorArray)/width))
    renderImage(width,height,colorArray)
main()
