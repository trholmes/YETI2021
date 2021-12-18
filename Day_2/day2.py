import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def calcPhi(row):
    # returns phi using Py and Px

    if row["Px"] < 0.0:
        return np.arctan( row["Py"] / row["Px"]) + np.pi
    if row["Px"] > 0.0:
        return np.arctan( row["Py"] / row["Px"])
    if row["Px"] == 0:
        return np.pi


data = pd.read_csv("FourVectorTest.csv", header=None, names=["Px", "Py", "Pz", "E"])

# calculate phi - azimuthal angle
data["phi"] = data.apply(lambda row: calcPhi(row), axis=1)

# calculates the magnitude of the momentem 3 vector
data["P"] = np.sqrt(data["Px"]**2 + data["Py"]**2 + data["Pz"]**2)

# polar angle theta
data["theta"] = np.arccos(data["Pz"]/data["P"])

# pseudo-rapidity eta
data["psu"] = np.log10(np.tan(data["theta"]/2))

fig, ax = plt.subplots()
counts, xedges, yedges, im = ax.hist2d(x=data["phi"], y=data["psu"], bins=500)
fig.set_size_inches(18.5, 10.5, forward=True)
plt.ioff()
plt.savefig("day2_result.png")