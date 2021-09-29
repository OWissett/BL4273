# Hmm, something is wrong?
# Can you find the problem

# This takes an standard input (from the command line), and then casts it
# to the int. This is a throwable event. Good practice would be to perform typechecking.

try:
    number = int(input("Give me a number: "))
except ValueError:
    print("Please only enter numbers!\nProgram exiting.")
    quit();

# This must be before number > 3, else it will be an inaccessible code path.
if number > 7:
    print("Number larger than seven")
elif number > 3:
    print("Number larger than three")
else:
    print("Number smaller or equal to three")