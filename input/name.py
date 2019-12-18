# second one


def manage_input():
    in_fullname = input("Please, give your full name")
    names = validate_display(in_fullname)
# function that ask and get the input of the user


def validate_juststring(input):
    """
    Verification that the input isn't empty of with
    character that aren't used in a name. Numbers,etc...
    this function return an error if something not planned is in this string.
    """
    if not len(input):
        return False

    # use of Regex to determine that we have a chain of letters and not something else.
    r = re.match("^[A-Za-z]+$", input)
    print(r)
    return True if r else False


def validate(fullname):
    """ 
    validation et display of the string 
    format Prénom <Milieu> Nom 
    """
    F_FIRST = "firstname"
    F_LAST = "lastname"
    F_MIDDLE = "middlename"
    F_FULL = "fullname"
    F_ERROR = "error"
    # We define the entry of the dictionnary

    names = fullname.split()
    len_listnames = len(names)
    # vérifier sur chaque str de name ne comporte que des lettres de l'alphabet
    type(names)
    for na in names:
        if not validate_juststring(na)
        return{F_ERROR: "Erreur de validation sur" + na}

    d = {}
    if len_listnames == 2:
        d[F_FIRST] = names[0]
        d[F_LAST] = names[1]
    elif len_listnames == 3:
        d[F_FIRST] = names[0]
        d[F_MIDDLE] = names[1]
        d[F_LAST] = names[2]
    elif len_listnames == 1:
        d[F_LAST] = names[0]
    else:
        F_ERROR = "Mauvais format!"
        if len_listnames == 0:
            F_ERROR += "Valeur manquante"
        else:
            F_ERROR += "Que faire de : " + " ".join(names[3:])
    return d


def validate_display(fullname):
    """ validation et affichage du nom rentré sous forme de string, format Prénom <Milieu> Nom"""
    d = {}
    names = fullname.split()
    # print(names)
    # print(type(names))

    len_listnames = len(names)
    print(len_listnames)

    if len_listnames == 2:
        print("Prénom : " + names[0] + " && Nom : " + names[1])
    elif len_listnames == 3:
        print(f"Prénom {names[0]}, Milieu {names[1]}, Nom {names[2]}")
    elif len_listnames == 1:
        print("Nom seul: " + names[0])
    elif len_listnames == 0:
        print("Merci de rentrer quelque chose")
    else:
        error = "Mauvais format!"
        if len_listnames == 0:
            error += "Valeur manquante"
        else:
            error += "Que faire de : " + " ".join(names[3:])

    return d


if __name__ == "__main__":
    manage_input()
