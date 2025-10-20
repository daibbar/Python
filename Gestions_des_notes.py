
#### DAIBBAR MOHAMED, devoir IID1 exercice 06
def menu():
    print("(1) Ajouter une note")
    print("(2) Ajouter plusieurs notes (séparées par des espaces)")
    print("(3) Statistiques (min, max, moyenne, nb d'admis ≥10)")
    print("(4) Afficher l’appréciation d’une note")
    print("(5) Réinitialiser toutes les notes")
    print("(q) Quitter\n")

def statistiques(une_liste):
        nb_admis = 0

        if (len(une_liste) == 0): 
            print("la liste est vide")
            return
        print("Stats! Choisir un option!\n")
        choix = input("(1) note min\n(2) note max\n(3) note moyenne\n(4) nb d'admis (note >= 10)\n")

        match choix:
            case "1":
                print(f"le min est: {min(notes)} ")
            case "2":
                print(f"le max est: {max(notes)}")
            case "3":
                print(f"la moyenne est: {round((sum(notes) / len(notes)), 2)}")
            case "4":
                i = 0
                while (i < len(une_liste)):
                    if (une_liste[i] >= 10): nb_admis += 1
                    i += 1
                print(f"le nombre des admis est: {nb_admis}\n")

notes = []
while (1):
    menu()
    choix = input("entrer une choix:")
    match choix:
        case "1":
            n = int(input("entrer la note: "))
            if n > 20 or n < 0 :
                print("votre choix n'est pas valide!")
            else:
                notes.append(n)
        case "2":
                notes.extend(list(map(int, input("Enter numbers: ").split())))
        case "3":
                statistiques(notes)
        case "4":
            n = int(input("entrer une note: "))
            if (n >= 16) : print("Tres Bien!")
            elif n >= 14 and n < 16 : print("Bien!")
            elif n>= 12 and n <= 14 : print("Assez Bien!")
            elif n >= 10 and n < 12 : print("Passable!")
            else : print("Passable!")
        case "5":
                notes = []
        case "q":
                break
     
