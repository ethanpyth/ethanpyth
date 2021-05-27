import random


argent = 1000


def separator():
    car = "="
    car *= 70
    return car


def zero(y):
    """
    :type y: integer
    """
    if y == 0:
        y -= y
    return "Merci d'avoir joué vous repartez avec", argent, "$."


def oui_non(x, argent=argent):
    """
    :param argent:
    :rtype: basestring
    """
    while x != "o" or x != "n":
        return "saisissez pour oui ,o, et pour non ,n."
    if x == 'o':
        return True
    elif x == 'n':
        zero(argent)
        return false


def etat():
    """
demande à l'utilisateur si il est pret a jouer
    :rtype: basestring
    """
    pret = input("Etes-vous pret?")
    if pret == 'n':
        print(f"{' Voulez vous quitter? ':=^70}")
        quitter = str(input())
        if oui_non(quitter):
            zero(argent)
            return not oui_non(pret)
    else:
        return oui_non(pret)


separator()
print(f"{' Casino win a million. ':=^70}")
print(f"{' Bienvenu au casino win a million. ':=^70}")
nom = input("Entrez votre nom : ")
older = int(input("Entrez votre age : "))
mineur = 18
separator()
if older < mineur:
    print(f"{nom} vous ne pouvez pas acceder au casino. Car vous avez moins de {mineur}")
    separator()
while (etat()) and (argent > 0):
    print(f"{nom} vous avez recu {argent} $ pour miser et jouer.")
    separator()
    mise = int(input("Quelle est votre mise? "))
    nbre_choisi = int(input("Choisissez un nombre entre 1 et 20 : "))
    while 0 > nbre_choisi or 20 < nbre_choisi:
        print("Vous devez choisir un nombre entre 0 et 20")
        nbre_choisi = int(input("Choisissez un nombre entre 1 et 20 : "))
        separator()
    if 0 < nbre_choisi <= 20:
        ng = random.randint(0, 19)
        print(f"{nom} le nombre gagnant est : {ng}")
        separator()
        if ng == nbre_choisi:
            argent -= mise
            mise *= 3
            argent += mise
            print(f"{nom} vous avez gagné {mise} $. votre cagnotte actuel est de {argent}")
            rg = str(input("voulez vous rejouer? "))
            verify = oui_non(rg)
            if verify:
                etat()
                separator()
            else:
                zero(argent)
        elif ng % 2 != 0 and nbre_choisi % 2 != 0:
            argent -= mise
            mise *= 2
            argent += mise
            print(f"{nom} vous avez gagné {mise} $. Votre cagnotte actuel est de {argent}")
            rg = str(input("Voulez vous rejouer? "))
            verify = oui_non(rg)
            etat()
            separator()
        elif ng % 2 == 0 and nbre_choisi % 2 == 0:
            argent -= mise
            mise *= 2
            argent += mise
            print(f"{nom} vous avez gagné {mise} $.votre cagnotte actuel est de {argent} $.")
            rg = str(input("Voulez vous rejouer? "))
            verify = oui_non(rg)
            separator()
        elif nbre_choisi != ng:
            argent -= mise
            print(f"{nom} vous avez perdu, il vous reste {argent} $ a misé.")
            zero(argent)
            if argent != 0:
                rg = str(input("Voulez vous rejouer? "))
                separator()
    elif "n" == rg:
        bye = zero(argent)
    separator()
