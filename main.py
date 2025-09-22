
#### Fonction secondaire isprime()


"""
Module principal pour l'affichage des nombres premiers inférieurs à 100.
"""
def isprime(p):

    """
    Détermine si p est un nombre premier.
    >>> isprime(0)
    False
    >>> isprime(1)
    False
    >>> isprime(2)
    True
    >>> isprime(3)
    True
    >>> isprime(4)
    False
    >>> isprime(5)
    True
    """
    if p < 2:
        return False
    for i in range(2, int(p ** 0.5) + 1):
        if p % i == 0:
            return False
    return True

#### Fonction principale


def main():

    """Affiche les nombres premiers inférieurs à 100."""
    for n in range(100):
        if isprime(n):
            print(n, end=", ")
    print()


if __name__ == "__main__":
    main()
