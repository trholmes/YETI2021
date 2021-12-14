import csv, numpy as np, matplotlib.pyplot as plt
from pylorentz import Momentum4 
from matplotlib.colors import LogNorm
def pseudorap(px,py,pz): #given three-momentum returns pseudorapidity
    mag = np.sqrt(px**2+py**2+pz**2)
    pr = np.arctanh(pz/mag)
    return pr
def az(px,py): #returns azimuthal angle
    az = np.arctan2(py,px)
    return az
pseudoRap = np.zeros(100000)
azimuthal = np.zeros(100000) 
fourVectors=[]
f = open('FourVectorTest.csv')
csv_reader=csv.reader(f)
for lineNumber,line in enumerate(csv_reader,1):
    pseudoRap[lineNumber-1] = pseudorap(float(line[0]),float(line[1]),float(line[2]))
    azimuthal[lineNumber-1] = az(float(line[0]),float(line[1]))
    fourVectors.append(Momentum4(line[3],line[0],line[1],line[2]))
    #creates list of four momenta
f.close()
plt.hist2d(pseudoRap,azimuthal,bins=250, cmap='winter', norm=LogNorm())
plt.colorbar()
plt.title('2D Histogram of Pseudorapidity vs Azimuthal Angle (aka Knoxville)')
plt.xlabel(r'Pseudorapidity $\eta$')
plt.ylabel(r'Azimuthal Angle $\phi$')
plt.savefig("HistogramYETI.jpg")