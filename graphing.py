import matplotlib.pyplot as plt
import numpy as np
from app import TARGET

def draw_scatter(name, x, y, slope, intercept):
    b = np.linspace(0, np.amax(y), 10)
    a = slope*b + intercept
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.scatter(x, y)
    plt.plot(a,b)
    plt.xlabel(f'{TARGET}')
    plt.ylabel(f'{name}')
    fig.savefig(f'./figures/{name}.png')