import random
from os import system
from fonctions import verifChoix, verifMise, miser, rejouer
from exception_constantes import VALUE_ERROR, TYPE_ERROR


def main():
    startGame = True
    Argent = 50
    coteDeMise = 2
    while startGame:
        if Argent > 0:
            nbRandom = random.randint(0, 49)
            try:
                UserInput = int(input("veuillez choisir un nombre sur lequel vous voulez misé : "))
            except ValueError:
                print(VALUE_ERROR)
            except TypeError:
                print(TYPE_ERROR)
            else:
                if verifChoix(UserInput):
                    SommeMisée = int(input("veuillez saisir la somme que vous voulez misé : "))
                    laMise = verifMise(SommeMisée, Argent)
                    if laMise:
                        if UserInput != nbRandom:
                            print(f"Résultat : {nbRandom}")
                            Argent = miser(SommeMisée, Argent)
                            print(f"la somme restante sur votre compte : {Argent}")
                            startGame = rejouer(input("Vous avez perdu, souhaiteriez vous rejouer ? O/N "))
                        else:
                            print(f"Résultat : {nbRandom}")
                            print("Bravo! vous avez gagné ")
                            Argent = Argent * coteDeMise
                    else:
                        print(f"Le maximum que vous pouvez miser est de {Argent} !")
                        startGame = rejouer(input("souhaitez vous rejouer ? O/N "))
                else:
                    print("veuillez saisir un choix valide ente 0 et 49")
        else:
            print("Vous n'avez pas assez d'argent pour jouer cette partie !")
            startGame = False


if __name__ == "__main__":
    main()
    system("pause")