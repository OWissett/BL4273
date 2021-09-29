#!/bin/python3
# All gene names on chromosome 21

filePath = "./human-genes.gtf"

with open(filePath, 'r') as geneFile:

    for line in geneFile:
        tmp = line.split("\t")

        if tmp[0] == '21':
            # This strips out the unwanted characters from the string.
            # It may be possible with regex, but that is a headache...
            print(tmp[8].split(";")[1][10:][2:][:-1])
            