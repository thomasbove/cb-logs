#!/usr/bin/env
import matplotlib
matplotlib.use('Agg') # no UI backend
import matplotlib.pyplot as plt
import numpy as np
import math
np.set_printoptions(threshold=np.inf)
import sys

if __name__ ==  "__main__":

    # Check for input arguments
    if len(sys.argv) != 3:
        print("Usage: python3 plot.py inputfile outputfile")
        exit()

    # Get arguments
    inputFile = sys.argv[1]
    outputFile = sys.argv[2]

    # Open the input file
    file = open(inputFile, "r")

    # Construct 2D matrix
    x = []
    y = []
    while True:
        line = file.readline()
        if not line:
            break
        split = line.split(" ")
        x.append(int(split[0]))
        y.append(int(split[1]))
    a = np.zeros(shape=(max(y)+50000, max(x)+1), dtype="int32")
    for (secret, time) in zip(x, y):
        a[time][secret] += 1
    # The following is for cutting the channel matrix to remove large areas of empty data
    # half = math.floor(len(a)/2)
    a = a[18000:21000][:]

    # Construct graph
    plt.imshow(a, interpolation='nearest', aspect='auto')
    ax = plt.gca()
    ax.set_ylim(ax.get_ylim()[::-1])
    plt.colorbar(label='Frequency')
    plt.xlabel("Secret")
    plt.ylabel("Time (Cycles)")

    plt.yticks([0, 500, 1000, 1500, 2000, 2500], [0+150, 500+150, 1000+150, 1500+150, 2000+150, 2500+150])
    # plt.yticks([0, 500, 1000, 1500, 2000, 2500], [0+27000, 500+27000, 1000+27000, 1500+27000, 2000+27000, 2500+27000])
    plt.xticks([-0.5, 0.5, 1.5], [0, 1, 2])

    # Output graph
    plt.savefig(outputFile)