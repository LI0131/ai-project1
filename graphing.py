import matplotlib.pyplot as plt
import numpy as np
import app

def draw_scatter(name, x, y, slope, intercept, iteration, showLine=True):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    scatter = ax.scatter(x, y)
    ax.set_xlim(0,np.amax(x))
    if showLine:
        line = [(slope * b + intercept) for b in list(range(0,50,1))]
        scatter.set_label(f'm={slope}, b={intercept}')
        ax.legend()
        ax.plot(line, scaley=True, scalex=True)
    plt.xlabel(f'{app.TARGET}')
    plt.ylabel(f'{name}')
    fig.savefig(f'./figures/{name}_{app.LEARNING_RATE}_{app.ITERATIONS}/{name}_{iteration}.png')

