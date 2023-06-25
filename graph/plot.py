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

    ar = []
    while True:
        line = file.readline()
        if not line:
            break
        split = line.split(" ")
        ar.append((int(split[0]), int(split[1])))

    maxTime = max(ar, key=lambda item: item[1])[1]+5000
    maxSecret = max(ar, key=lambda item: item[0])[0]+1
    a = np.zeros(shape=(maxTime, maxSecret), dtype="int32")
    for (x,y) in ar:
        a[y][x] += 1
    a = a[28000:32000][:]

    # Construct graph
    plt.imshow(a, interpolation='nearest', aspect='auto')
    ax = plt.gca()
    ax.set_ylim(ax.get_ylim()[::-1])
    plt.colorbar(label='Frequency')
    plt.xlabel("Secret")
    plt.ylabel("Time (Cycles)")

    plt.yticks([0, 500, 1000, 1500, 2000, 2500, 3000, 3500], [0+28000, 500+28000, 1000+28000, 1500+28000, 2000+28000, 2500+28000, 3000+28000, 3500+28000])
    # plt.yticks([0, 10, 20, 30, 40, 50], [0+640, 10+640, 20+640, 30+640, 40+640, 50+640])
    # plt.yticks([0, 10, 20, 30, 40], [0+1000, 10+1000, 20+1000, 30+1000, 40+1000])
    # plt.yticks([0, 20, 40, 60, 80], [0+24550, 20+24550, 40+24550, 60+24550, 80+24550])
    # plt.yticks([0, 25, 50, 75, 100, 125, 150, 175], [0+900, 25+900, 50+900, 75+900, 100+900, 125+900, 150+900, 175+900])
    # plt.yticks([0, 20, 40, 60, 80], [0+300, 20+300, 40+300, 60+300, 80+300])
    # plt.yticks([0, 500, 1000, 1500, 2000, 2500], [0+27000, 500+27000, 1000+27000, 1500+27000, 2000+27000, 2500+27000])
    plt.xticks([-0.5, 0.5, 1.5], [0, 1, 2])

    # Output graph
    plt.savefig(outputFile)