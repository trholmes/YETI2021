import csv, numpy as np, matplotlib.pyplot as plt
from pylorentz import Momentum4 
from matplotlib.colors import LogNorm

pseudoRap = np.zeros(100000)
azimuthal = np.zeros(100000) 
fourVectors=[]
f = open('FourVectorTest.csv')
csv_reader=csv.reader(f)

pseudorap=lambda px,py,pz: np.arctanh(pz/(np.sqrt(px**2+py**2+pz**2)))
#function for pseudorapidity: arctanh(pz/p)

for lineNumber,line in enumerate(csv_reader,1):
    px, py, pz, E = float(line[0]), float(line[1]),float(line[2]), float(line[3])
    pseudoRap[lineNumber-1] = pseudorap(px,py,pz)
    azimuthal[lineNumber-1] = (lambda x, y:np.arctan2(x,y))(py, px)
    #azimuthal angle is arctan2(py/px)
    fourVectors.append(Momentum4(E,px,py,pz))
    #creates list of four momenta (E,px,py,pz)
f.close()
plt.hist2d(pseudoRap,azimuthal,bins=250, cmap='cool', norm=LogNorm())
plt.colorbar()
plt.title('2D Histogram of Pseudorapidity vs Azimuthal Angle (aka Knoxville)')
plt.xlabel(r'Pseudorapidity $\eta$')
plt.ylabel(r'Azimuthal Angle $\phi$')
plt.savefig("HistogramYETI.jpg")