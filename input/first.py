# First traitement

# We ask the user to enter his name, and then print it to make it appear
fullname = input("What's your first and last name?")
print(fullname)

# The string we got from the input is split at every space.
# then we print the array we got, the type of data (here a list) and then the number of entry in the array
names = fullname.split()
print(names)
print(type(names))
print(len(names))

# we got all the entry in the array and then display them
len_listnames = len(names)
print(len_listnames)

# the code react to how many entries he got. Only a name, full name, if the person got a middle name
# and if the person enter more than one middle name.
if len_listnames == 2:
    print("Prénom : " + names[0] + " && Nom : " + names[1])
elif len_listnames == 3:
    print(f"Prénom {names[0]}, Milieu {names[1]}, Nom {names[2]}")
elif len_listnames == 1:
    print("Nom seul: " + names[0])
else:
    print("Format: Prénom <Milieu> Nom")
    print("Que faire de : " + " ".join(names[3:]))
