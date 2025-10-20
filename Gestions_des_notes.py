
notes = []
nb_saisies = 0
nb_valides = 0

print("(1) Ajouter une note")
print("(2) Ajouter plusieurs notes (séparées par des espaces)")
print("(3) Statistiques (min, max, moyenne, nb d'admis ≥10)")
print("(4) Afficher l’appréciation d’une note")
print("(5) Réinitialiser toutes les notes")
print("(q) Quitter\n")


choix = input("entrer une choix:")

def statistiques(une_liste):
        if (len(une_liste) == 0): 
            print("la liste est vide")
            return
        print("Stats! Choisir un option!\n")
        choix = input("(1) note min\n(2) note max\n(3) note moyenne\n(4) nb d'admis (note >= 10)\n")

        match choix:
            case "1":
                print(f"le min is {} ")
        

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
    case "5":
        notes = []
    case "4":
        n = int(input("entrer une note: "))
        if (n >= 16) : print("Tres Bien!")
        elif n >= 14 and n < 16 : print("Bien!")
        elif n>= 12 and n <= 14 : print("Assez Bien!")
        elif n >= 10 and n < 12 : print("Passable!")
        else : print("Passable!")

    
     
