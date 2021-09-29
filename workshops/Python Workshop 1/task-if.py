# Hint 1: I only want to have one output line
# Hint 2: The most accurate description of my number

number = int(input("Give me a number: "))

intro = "Your number is "
    
if number > 8:
    print(f"{intro} larger than eight")

elif number > 6:
    print(f"{intro} larger than six")
    
elif number > 4:
    print(f"f{intro} larger than four")

elif number > 2:
    print(f"{intro} larger than two")

else:
    print(f"{intro} smaller than two")