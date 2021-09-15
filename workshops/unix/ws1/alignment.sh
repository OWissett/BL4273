#!/bin/bash
# The use of a hashbang tag (#!/bin/bash) is good practice. Its tells the terminal to run the script in the context of bash, however, it may be used to indicate another shell or intepreter such as python or ruby. This means that if the script is run from zsh or sh, it should be executed in bash instead.

# Create a directory to store the aligned sequences
mkdir output

# Loop over all files ending in .fasta
for SEQ_FILE in *.fasta
do
	# Get the name of the fasta file without the suffix
	SEQ_NAME=${SEQ_FILE%%.fasta}

	# Create a new variable to store the alignment
	ALIGN_NAME=$SEQ_NAME.align

	# Read the current SEQ_FILE, send the output to muscle (alignment tool), and store the alignment
	cat $SEQ_FILE | /scratch/bioinf/BL4237/muscle -maxiters 2 > output/$ALIGN_NAME 2>/dev/null

	# Inform the user that the file has been written to the given output.
	echo Alignment of $SEQ_FILE written to output/$ALIGN_NAME
done

