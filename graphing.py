import matplotlib.pyplot as plt
from app import TARGET

def draw_scatter(name, x, y):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.scatter(x, y)
    plt.xlabel(f'{TARGET}')
    plt.ylabel(f'{name}')
    fig.savefig(f'./figures/{name}.png')