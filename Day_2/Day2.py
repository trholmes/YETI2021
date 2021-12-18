import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():
    df = pd.read_csv('./FourVectorTest.csv', header=None, names = ['Px', 'Py', 'Pz', 'E'])
    df['phi'] = df.apply(lambda row : np.arctan2(row.Py,row.Px), axis=1)
    df['eta'] = df.apply(lambda row : np.arctanh(row.Pz/np.sqrt(row.Px*row.Px + row.Py*row.Py + row.Pz*row.Pz)), axis=1)
    plt.hist2d(df['phi'], df['eta'], (1000, 1000))
    plt.show()

if __name__=='__main__':
    main()
