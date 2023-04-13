#!/usr/bin/env
import matplotlib
matplotlib.use('Agg') # no UI backend
import matplotlib.pyplot as plt
import numpy as np
import math
np.set_printoptions(threshold=np.inf)
import sys

if __name__ ==  "__main__":
    file = open("./llc-kernel-kc", "r")
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

    # half = math.floor(len(a)/2)
    a = a[26500:29000][:]

    plt.imshow(a, interpolation='nearest', aspect='auto')
    ax = plt.gca()
    ax.set_ylim(ax.get_ylim()[::-1])
    plt.colorbar(label='Frequency')
    plt.xlabel("Secret")
    plt.ylabel("Time (Cycles)")
    # plt.yticks([0, 10000, 20000, 30000, 40000, 50000, 60000], [0+half, 10000+half, 20000+half, 30000+half, 40000+half, 50000+half, 60000+half])
    # plt.yticks([0, 100, 200, 300, 400], [0+136500, 100+136500, 200+136500, 300+136500, 400+136500])
    # plt.yticks([0, 50, 100, 150, 200], [0+900, 50+900, 100+900, 150+900, 200+900])
    # plt.yticks([0, 50, 100, 150, 200, 250], [0+3100, 50+3100, 100+3100, 150+3100, 200+3100, 250+3100])
    # plt.yticks([0, 50, 100, 150, 200], [0+1000, 50+1000, 100+1000, 150+1000, 200+1000])
    # plt.yticks([0, 2000, 4000, 6000, 8000, 10000, 12000, 14000, 16000], [0+30000, 2000+30000, 4000+30000, 6000+30000, 8000+30000, 10000+30000, 12000+30000, 14000+30000, 16000+30000])
    # plt.yticks([0, 100, 200, 300, 400, 500, 600], [0+48000, 100+48000, 200+48000, 300+48000, 400+48000, 500+48000, 600+48000])
    # plt.yticks([0, 500, 1000, 1500, 2000], [0+28000, 500+28000, 1000+28000, 1500+28000, 2000+28000])
    plt.yticks([0, 500, 1000, 1500, 2000, 2500], [0+26500, 500+26500, 1000+26500, 1500+26500, 2000+26500, 2500+26500])

    plt.savefig("llc-kernel-kc.png")