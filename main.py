import random
import pickle


epsedo = (input("Antre pseudo lan: "))
if not epsedo.islower():
    epsedo = (input("psedo ou antre a pa korek,tanpri reeseye"))
if ' ' in epsedo:
    epsedo = (input("psedo ou antre a gen espas,eseye antre yon lot"))


#Nou swete joueur a bievini nan jwet la.

print(f"Bonjou, {epsedo} byenvini nan jwet lawoulet la")

# Kreye yon nonb kache
#nou deklare yon varyab non kache, nonb kache a trouvel ant 0 et 100
nonb_kache = random.randint(0, 100)

# Inisyalize kantite chans
# nou bay joeur a 5 chans selman nan jwet la

kantite_chans = 5

# Nou fe yon boucle pou joeur a kapab komnse antre nonb yo
while True:
    while kantite_chans > 0:
        try:
            # Mande itilizatè a antre yon nonb nan entèval la
            guess = int(input(f"Antre yon nonb nan entèval [0, 100]. Ou gen {kantite_chans} chans: "))

            # si nonb itilizate a antre a pa nan boucle la, nap fel konn sa.
            if guess < 0 or guess > 100:
                print("Nonb la dwe nan entèval [0, 100].")
                continue

            # Verifye si nonb la koresponn ak nonb kache a
            if guess < nonb_kache:
                print("Nonb la pi piti.")
            elif guess > nonb_kache:
                print("Nonb la pi gran.")
            else:
                print("BRAVO! Ou genyen!!")
                break

            # Diminye kantite chans
            kantite_chans -= 1

        except ValueError:
            print("Tanpri antre yon nonb valab.")

    # Si itilizatè a pèdi
    if kantite_chans == 0:
        print(f"Ou pèdi. Nonb kache a te {nonb_kache}.")

        # Enregistre skò itilizatè a nan yon fichye pickled
        with open('sko.pkl', 'wb') as sko_fichye:
            pickle.dump(kantite_chans, sko_fichye)
    else:
        # Si itilizatè a jwenn, afiche skò li
        with open('sko.pkl', 'rb') as sko_fichye:
            sko_ansyen = pickle.load(sko_fichye)

        sko_nouvo = sko_ansyen + kantite_chans
        print(f"Skò ansyen: {sko_ansyen}, Nouvo skò: {sko_nouvo}")

    Stop=input((" Peze k pou w kanpe jwet la: "))
    if Stop.lower() == 'k':
        kantite_chans==0
        print("mesi paske ou te jwe ak nou")
        break
    else:
        print(f"Nou renmen peseverans ou{epsedo}")
        nonb_kache = random.randint(0, 100)
        kantite_chans==5
        print(f"Nou renmen peseverans ou{epsedo}, ou genyen {kantite_chans} chans pou jwe ak nou")