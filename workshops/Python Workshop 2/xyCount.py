#!/bin/python3
# How many genes X and Y have

filePath = "./human-genes.gtf"

with open(filePath, 'r') as geneFile:

    xCount = 0
    yCount = 0

    for line in geneFile:
        tmp = line.split("\t")

        if tmp[0].lower() == 'x':
            xCount += 1

        if tmp[0].lower() == 'y':
            yCount += 1

    print(f"The X chromosome has {xCount} genes, and the Y chromosome has {yCount} genes.")

