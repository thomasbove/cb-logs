#!/usr/bin/env
import matplotlib
matplotlib.use('Agg') # no UI backend
import matplotlib.pyplot as plt
import numpy as np
np.set_printoptions(threshold=np.inf)
import sys

if __name__ ==  "__main__":
    file = open("../cva6-fencet-btb-invoke", "r")
    x = []
    y = []

    while True:
        line = file.readline()
        if not line:
            break
        split = line.split(" ")
        x.append(int(split[0]))
        y.append(int(split[1]))

    a = np.zeros(shape=(2*max(y), max(x)+1), dtype="int32")
    for (secret, time) in zip(x, y):
        a[time][secret] += 1

    plt.imshow(a, interpolation='nearest', aspect='auto')
    ax = plt.gca()
    ax.set_ylim(ax.get_ylim()[::-1])
    plt.colorbar(label='Frequency')
    plt.xlabel("Secret")
    plt.ylabel("Time (Cycles)")

    plt.savefig("cva6-fencet-btb-invoke.png")