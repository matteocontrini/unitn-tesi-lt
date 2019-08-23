#!/usr/bin/python3
# https://stackoverflow.com/questions/51229126/how-to-find-the-red-color-regions-using-opencv

import cv2
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams
import matplotlib.ticker as plticker

vid = cv2.VideoCapture("1561366571.mp4")

x = []
y_r = []
y_g = []
y_b = []
y_diff = []

while vid.isOpened():
    ret, img = vid.read()

    if not ret:
        break

    average = img.mean(axis=0).mean(axis=0)

    b, g, r = average
    diff = g - ((r + b) / 2)
    y_r.append(r)
    y_g.append(g)
    y_b.append(b)
    y_diff.append(diff)

    msec = vid.get(cv2.CAP_PROP_POS_MSEC) / 1000
    x.append(msec)

    #print(str(msec) + " => " + str(diff))

# https://jwalton.info/Embed-Publication-Matplotlib-Latex/

def get_size(width, fraction=1):
    # Width of figure
    fig_width_pt = width * fraction

    # Convert from pt to inches
    inches_per_pt = 1 / 72.27

    # Golden ratio to set aesthetic figure height
    golden_ratio = (5**.5 - 1) / 2

    # Figure width in inches
    fig_width_in = fig_width_pt * inches_per_pt
    # Figure height in inches
    fig_height_in = fig_width_in * golden_ratio

    fig_dim = (fig_width_in, fig_height_in)

    return fig_dim

# rcParams['font.family'] = 'serif'
# rcParams['text.usetex'] = True
# rcParams['font.size'] = 10
# rcParams['figure.figsize'] = (9, 5)

nice_fonts = {
    # Use LaTeX to write all text
    "text.usetex": True,
    "font.family": "serif",
    # Use 10pt font in plots, to match 10pt font in document
    "axes.labelsize": 10,
    "font.size": 10,
    # nooo # Make the legend/label fonts a little smaller
    #"legend.fontsize": 8,
    "xtick.labelsize": 10,
    "ytick.labelsize": 10,
    "figure.figsize": get_size(483.69687)
}

rcParams.update(nice_fonts)

plt.xticks(np.arange(min(x), max(x)+1, 1).astype(int))
#plt.yticks(np.arange(min(y_diff), max(y_diff), 3).astype(int))

#plt.figure(figsize=(9, 5))
plt.grid(True)
#plt.ylim(ymin = 0, ymax=255)
# plt.gca().tick_params(axis='x', colors='#444444')
# plt.gca().tick_params(axis='y', colors='#444444')

plt.xlabel('Tempo (s)')
plt.ylabel('Valore canale (0-255)')

def channels():
    plt.plot(x, y_r, 'red')
    plt.plot(x, y_g, 'green')
    plt.plot(x, y_b, 'blue')

    plt.gca().yaxis.set_major_locator(plticker.MultipleLocator(base=14.0))
    plt.ylim(ymin = 0, ymax=255)
    plt.savefig('opencv_channels.pdf', format='pdf', bbox_inches='tight')

    plt.gca().yaxis.set_major_locator(plticker.MultipleLocator(base=2.0))
    plt.autoscale()
    plt.savefig('opencv_channels_tight.pdf', format='pdf', bbox_inches='tight')

def diff():
    plt.plot(x, y_diff, 'black')
    plt.gca().yaxis.set_major_locator(plticker.MultipleLocator(base=2.0))
    plt.savefig('opencv_diff.pdf', format='pdf', bbox_inches='tight')

# channels()
diff()
#plt.show()
