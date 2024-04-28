
def miser(LaMise: int, argent: int):
    """Fonction qui gére la deduction d'argent apres la mise et retourne un resultat entier
    Arguments:
    LaMise(int) : la somme misée
    argent(int) : le solde d'argent restant

    """
    resultat = argent - LaMise
    return resultat


def verifMise(LaMise: int, argent: int) -> bool:
    """Fonction qui verifie la validité de la mise et retoune un boolean
    Arguments:
    LaMise(int) : la somme misée
    argent(int) : le solde d'argent restant
    
    """
    if LaMise > argent:
        return False
    else:
        return True


def verifChoix(nbChoix: int) -> bool:
    """Fonction qui verifie le choix (le nombre) saisie par l'utilisateur et retourne un boolean
    Arguments:
    nbChoix(int) : le choix saisi par l'utilisateur

    """
    if nbChoix not in range(0, 50):
        return False
    else:
        return True


def rejouer(response: str) -> bool:
    """Fonction qui qui gere le choix ( O | N ) saisie par l'utilisateur et retourne un boolean
    Arguments:
    response(str) : le choix saisi par l'utilisateur ( O | N )
    
    """
    if response == "O":
        return True
    elif response == "N":
        return False
