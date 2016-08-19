import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib as mpl

HEIGHT = .1
choices = [mpl.colors.rgb2hex(c) for c in sns.color_palette()[:3]]

def plot_factorize():
    starts = np.arange(0, 1, .1)
    np.random.seed(4)
    colors = np.random.choice(choices, 10)
    factors, _ = pd.factorize(colors)

    fig, ax = plt.subplots()
    for start, c in zip(starts, colors):
        ax.add_patch(
            mpl.patches.Rectangle((0, start), .4, HEIGHT, facecolor=c),
        )

    for start, c, f in zip(starts, colors, factors):
        ax.add_patch(
            mpl.patches.Rectangle((.6, start), .4, HEIGHT, fill=False),
        )
        ax.annotate(f, xy=(.4, start + .05), xytext=(.75, start + .05),
                    verticalalignment='center',
                    arrowprops=dict(facecolor=c,
                                    arrowstyle='<-'),
                    fontsize=16)
    sns.despine()
    ax.yaxis.set_visible(False)
    ax.xaxis.set_visible(False)
    ax.set_axis_bgcolor('none')
    plt.grid(0)


def plot_get_dummies():
    WIDTH = .2
    starts = np.arange(0, 1, .1)
    np.random.seed(4)
    colors = np.random.choice(choices, 10)
    factors, _ = pd.factorize(colors)

    fig, ax = plt.subplots()
    for start, c in zip(starts, colors):
        ax.add_patch(
            mpl.patches.Rectangle((0, start), .2, HEIGHT, facecolor=c),
        )

    lefts = [.4, .6, .8]
    for i, left in enumerate(lefts):
        for start, c, f in zip(starts, colors, factors):
            if i != f:
                ax.add_patch(
                    mpl.patches.Rectangle((left, start), WIDTH,
                                          HEIGHT, fill=False)
                )
            else:
                ax.add_patch(
                    mpl.patches.Rectangle((left, start), WIDTH, HEIGHT,
                                          facecolor=c),
                )

    ax.yaxis.set_visible(False)
    ax.xaxis.set_visible(False)
    ax.set_axis_bgcolor('none')
    plt.grid(0)
