import fonctions as f

while True:
    try:
        b = int(input("Entrez un nombre 1 (ou appuyez sur CTRL-C pour quitter) : "))
        a = int(input("Entrez un nombre 2 (ou appuyez sur CTRL-C pour quitter) : "))


        res = f.puissance(a, b)
        
        print(f"Le résultat de {a} élevé à la puissance {b} est : {res}")

    except KeyboardInterrupt:
        print("\nInterruption reçue. Fin du programme.")
        break
    except ValueError:
        print("Veuillez entrer des nombres entiers valides.")
    except TypeError as e:
        print(f"Erreur de type : {e}")
