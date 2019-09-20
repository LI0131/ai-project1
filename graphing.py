import matplotlib.pyplot as plt
import numpy as np
from app import TARGET, LEARNING_RATE, ITERATIONS

def draw_scatter(name, x, y, slope, intercept):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    line = [(slope * b + intercept) for b in list(range(0,50,1))]
    scatter = ax.scatter(x, y)
    ax.set_xlim(0,np.amax(x))
    scatter.set_label(f'm={slope}, b={intercept}')
    ax.legend()
    ax.plot(line, scaley=True, scalex=True)
    plt.xlabel(f'{TARGET}')
    plt.ylabel(f'{name}')
    fig.savefig(f'./figures/{LEARNING_RATE}_{ITERATIONS}/{name}.png')
