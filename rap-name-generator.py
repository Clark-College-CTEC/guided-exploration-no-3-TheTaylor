# Guided Exploration No. 3
# Author: Robert 3. Taylor
# Date: 08/14/2020

# This pulls the 'random' library for use later in the program.
import random

# Declares an empty list. Holds elements from the rap-names.txt
possible_names = []

# Opens new file. Holds new names.
outputFile = open('rap-names-output.txt', 'w')

# Acesses 'rap-names.txt' file as a data source to run a For Loop through. Applies the variable name 'dataFile' to it.
with open('rap-names.txt', 'r') as dataFile:
    # This the afore mentioned For Loop.
    for name in dataFile:
        # This removes the line-feed off each element in 'dataFile' then slides the element to the 'possible-names' variable.
        possible_names.append(name.rstrip())

# This requests input on how many time the program will run in succesion.
count = int(input('How many rap names would you like to create? '))
# This requests input on how many list elements will be included in the output.
parts = int(input('How many parts should the name contain? '))

# This For Loop will run through as many iterations as the user inputed on line 22 as per the variable 'count'.
for i in range(count):
    # Declares new empty list asigned to variable 'name_parts'.
    name_parts = []
    # This For Loop will run through as many iterations as the user inputed on line 24 as per the variable 'parts'.
    for j in range(parts):
        # Accesses the 'posible-names' list and randomly selects elements.  Elements are dropped into 'name-parts'.
        name_parts.append(
            possible_names[random.randint(0, len(possible_names)-1)])

        # This creates seperate file to store the results of the program. The 'write' meathod uses the line methon for joinining elements from the 'name_parts' variable. The carage return is added at the end.
        outputFile.write(f"{' '.join(name_parts)}\n")
        # This prints the results in-terminal rather than creating a seperate file. The 'write' meathod uses the line methon for joinining elements from the 'name_parts' variable. The carage return is added at the end.
        print(f"{' '.join(name_parts)}")


# Utilizes the file method 'close' to end program.
outputFile.close()
