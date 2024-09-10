import fonctions as f
while True:
    try:
   
        b = float(input("Entrez un nombre 1 (ou appuyez sur CTRL-C pour quitter) : "))
        a = float(input("Entrez un nombre 2 (ou appuyez sur CTRL-C pour quitter) : "))

     
        carre1 = a ** 2
        
        
        res = f.puissance(a,b)
        
        print(res)
    except KeyboardInterrupt:

        print("\nInterruption reçue. Fin du programme.")
        break 
