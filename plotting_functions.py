import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

points  = ["A","B","C","D","E","F"]
def load_data(datapath):
    df = pd.read_csv(datapath)
    data = df.to_numpy()[:,1:]
    return data

def condition(data, node_idx, lower_bound = None, upper_bound = None):
    Node_data = data[:,node_idx].flatten()
    cond_idx = (-1 < Node_data) & (Node_data < 0)
    cond = np.where(cond_idx)[0]
    cond_data = data[cond,:]
    return cond_data

#plotter pairwise scatter plots. Set idx for at farvelægge punkter efter værdi af node "idx".

def plot_grid(data, idx = None, n = 4):
    fig, axes = plt.subplots(n, n, figsize=(10, 10))

    for i in range(n):
        for j in range(n):
            x = data[:,i].flatten()
            y = data[:,j].flatten()
            
            if (i == j):
                axes[i, j].hist(y, bins =10)
                axes[i, j].set_title(f"Histogram")
            else:
                if idx != None:
                    z = data[:, idx].flatten()
                    axes[i, j].scatter(x, y, c=z, cmap='viridis')
                else: 
                    axes[i, j].scatter(x, y)
                axes[i, j].set_title(f"{points[i]} vs {points[j]}")

    plt.tight_layout()
    plt.show()

#plotgrid men til når man laver intervention,
#fordi plotsne ellers er grimme ved den variable man har lavet intervention på. 
def plot_grid_hist(data, idx, n = 4):
    # Create figure and axes (4x4 grid)
    fig, axes = plt.subplots(n, n, figsize=(20, 20))

    # Generate scatter plots
    for i in range(n):
        for j in range(n):
            x = data[:,i].flatten()
            y = data[:,j].flatten()
            if (i == idx or j == idx):
                axes[i, j].hist(y, bins =10)
                axes[i, j].set_title(f"Histogram")
            else:
                axes[i, j].scatter(x, y)
                axes[i, j].set_title(f"{points[i]} vs {points[j]}")

    plt.tight_layout()
    plt.show()

#histogram for all variables seperatly (not a grid)
def plot_4hist(data, n = 4):
    fig, axes = plt.subplots(1, n, figsize=(20, 5))

    for i in range(n):
        x = data[:,i].flatten()
        axes[i].hist(x, bins = 10)
        axes[i].set_title(f"Histpgram {points[i]}")

    plt.tight_layout()
    plt.show()
