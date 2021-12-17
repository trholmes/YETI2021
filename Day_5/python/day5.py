import math
import numpy
from matplotlib import pyplot
class fibonacci:
    def __init__(self):
        self.Fnm1   = 0
        self.Fn   = 1
    def __call__(self) -> int:
        Fnp1 = self.Fn + self.Fnm1
        self.Fnm1 = self.Fn
        self.Fn = Fnp1
        return Fnp1

datapath = "../../Day_4/data/decoded.txt"

print("Generating Fibonacci numbers")
fib      = fibonacci()
nmax     = 30
evenfibs = [0]
oddfibs  = [1]
fibs     = [0, 1]
while len(evenfibs) < 10 or len(oddfibs) < 7:
    t_fib = fib()
    if t_fib % 2 == 0:
        evenfibs.append(t_fib)
    else:
        oddfibs.append(t_fib)
    fibs.append(t_fib)


print("Reading in data")
rawdat = []
with open(datapath, "r") as fp:
    rawdat = fp.readlines()[0].replace("\n","")
asbytes = bytearray.fromhex(rawdat)

print("Composing pixels")
colorvals = [0] * len(asbytes)
for i in range(len(colorvals)):
    colorvals[i] = asbytes[i] / 255.0

picwidth  = evenfibs[8] // oddfibs[5]
picheight = len(colorvals) // (3 * picwidth)

nppix     = numpy.array(colorvals)
nppix     = numpy.reshape(nppix, (picheight, picwidth, 3))

pyplot.imsave("../data/image.jpg", nppix)