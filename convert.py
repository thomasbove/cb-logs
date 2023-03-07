#!/usr/bin/env

import sys

if __name__ ==  "__main__":

    if len(sys.argv) != 3:
        print("Usage: python convert.py inputfile outputfile")
        exit()

    inputName = sys.argv[1]
    outputName = sys.argv[2]

    inputFile = open(inputName, "r")
    outputFile = open(outputName, "w")
    while True:
        line = inputFile.readline()
        if not line:
            break

        stripped = line.strip()
        split = stripped.split(" ")

        s = split[0]
        o = split[1]

        outputFile.write("(" + s + "," + o + ")\n")

    inputFile.close()
    outputFile.close()
        