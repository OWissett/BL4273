#!/usr/bin/python3
# Task: count genes per chromosome
#       print for every chromosome the number of genes starting with the
#       chromosome having the fewest genes and ending with the chromosome having
#       the most genes.

def getGeneCount():

    # Declare the location of the human-genes.gtf file
    filePath = "./human-genes.gtf"

    # Open the file with error handling
    with open(filePath, 'r') as geneFile:

        # Create an empty dictionary to store the chromosome names
        # and number of genes.
        genes = {}

        # Read the geneFile line by line
        for line in geneFile:

            # Split each line by tabs.
            tmp = line.split("\t")
            
            # Check if the key for the given chromosome exists in the dictionary
            if str(tmp[0]) in genes:
                # If the key exists, then increment the count by 1. This works
                # because each line in the file is a single gene.
                genes[str(tmp[0])] += 1
            else:
                # If the key does not exist, create one and set the count to 1.
                genes[str(tmp[0])] = 1

        # Return the dictionary of gene counts to the caller.
        return genes


# Use dictionary comprehension to sort the output of the getGeneCount function.
geneCount = {chromosome: count for chromosome, count in sorted(getGeneCount().items(), key = lambda item: item[1])}

def printGeneCount(countDict):
    for key in countDict:
        print(f"Chromosome {key} has {countDict[key]} genes")

printGeneCount(geneCount)