import csv
import math
from matplotlib import pyplot
from matplotlib.colors import LogNorm
vec4path = "../../Day_1/data/FourVectorTest.csv"

class Vec4:
    def __init__(self, vec):
        self.Px = float(vec[0])
        self.Py = float(vec[1])
        self.Pz = float(vec[2])
        self.P = math.sqrt(self.Px * self.Px + 
                            self.Py * self.Py +
                            self.Pz * self.Pz)
        self.E  = float(vec[3])
        self.Pt = math.sqrt(self.Px * self.Px + self.Py * self.Py)
        self.phi = math.acos(self.Px / self.P)
        self.eta = math.atanh(self.Pz / self.P)
    
    # allows a pretty print to make sure the data came in nicely
    def __repr__(self) -> str:
        return f"{self.Px}, {self.Py}, {self.Pz}, {self.E}"

def main() -> None:
    # get data from disk
    vec4s = []
    with open(vec4path, "r") as incsv:
        fr = csv.reader(incsv, delimiter=",")
        for row in fr:
            vec4s.append(Vec4(row))
    # collect angles and plot histogram
    # lognorm scale makes the low count bins stand out
    h = pyplot.hist2d([i.eta for i in vec4s], [i.phi for i in vec4s], bins=200, norm=LogNorm())
    pyplot.colorbar(h[3])
    pyplot.xlabel("Pseudorapidity")
    pyplot.ylabel("Azimuthal angle")
    pyplot.savefig("../data/phi-v-eta-py.png")








if (__name__ == "__main__"):
    main()