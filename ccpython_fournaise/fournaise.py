def openFile(filepath):
    try:
        f = open(filepath, 'r')
    except:
        return(-1)
    return(f)

def readFileOne(file):
    match = "volcan"
    idx = 0

    for letter in file.read():
        if letter == match[idx]:
            idx = idx + 1
            if idx == 6:
                print("     Dodo 1: A l’aide, tous aux abris !")
                return(0)
        elif letter != match[idx]:
            idx = 0 
    
def readFileTwo(file):
    content = file.read()
    file.close()
    content = content.split("\n")
    
    for line in content:
        line = line.split(' ')
        for word in line:
            if word == "arbre" or word == "l'arbre":
                print("     " + " ".join(line))


def printFileThree(pasLeft, pasRight, pasForward):
    print("     Pas à gauche : ", pasLeft, " pas.")
    print("     Pas en avant : ", pasForward, " pas.")
    print("     Pas à droite : ", pasRight, " pas.")
    if pasLeft > pasForward and pasLeft > pasRight:
            print("     Le plus de pas effectués est vers la gauche : ", pasLeft, " pas.")
    elif pasRight > pasForward and pasRight > pasLeft:
        print("     Le plus de pas effectués est vers la droite : ", pasRight, " pas.")
    elif pasForward > pasLeft and pasForward > pasRight:
        print("     Le plus de pas effectués est en avant : ", pasForward, " pas.")


def readFileThree(file):
    content = file.read()
    file.close()
    content = content.split("\n")
    pasLeft = 0
    pasRight = 0
    pasForward = 0

    for line in content:
        line = line.split(' ')
        for word in line:
            if "rocher" in word or "rochers" in word:
                pasLeft += 5
            elif "arbre" in word or "arbres" in word:
                pasForward += 10
            elif "dodo" in word or "dodos" in word:
                pasRight += 6
            if pasLeft + pasForward + pasRight >= 100 and word == "lac":            
                printFileThree(pasLeft, pasRight, pasForward)

def deleteDoublon(array):
    array.sort(key = int, reverse = False)
    last_number = 0
    idx = 0

    for number in array:
        if last_number == number:
            array.pop(idx)
        else:
            last_number = number
        idx += 1
    print("     " + " ".join(array))


def readFileFour(file):
    content = file.read()
    file.close()
    content = content.split(" ")
    array = []
    idx = 0

    for number in content:
        if len(number) >= 2 and number[1] == ',':
            array.insert(idx, number[0])
        elif len(number) >= 3 and number[2] == ',':
            array.insert(idx, number[0] + number[1])
        idx += 1
    deleteDoublon(array)

def readFileFive(file):
    content = file.read()
    file.close()
    content = content.split(" ")
    array = []
    majeurs = 0
    mineurs = 0
    idx = 0

    for number in content:
        if len(number) >= 2 and number[1] == ',':
            array.insert(idx, number[0])
        elif len(number) >= 3 and number[2] == ',':
            array.insert(idx, number[0] + number[1])
        idx += 1

    for number in array:
        if int(number) > 5:
            majeurs += 1
        elif int(number) < 5:
            mineurs += 1
    print("     Il y a ", majeurs, "dodo(s) majeurs et ", mineurs, " dodo(s) mineurs !")

print("part 1 - A :")
file = openFile("../messagePourSauverLeMonde.txt")
readFileOne(file)

print("\n" + "part 1 - B :")
file = openFile("../livreDeLaNatureEtDesLacs.txt")
readFileTwo(file)

print("\n" + "part 1 - C :")
file = openFile("../desProjectilesEtDesDodos.txt")
readFileThree(file)

print("\n" + "part 2 - A  :")
file = openFile("../lafamilleDodo.txt")
readFileFour(file)

print("\n" + "part 2 - B  :")
file = openFile("../ageDodo.txt")
readFileFive(file)
