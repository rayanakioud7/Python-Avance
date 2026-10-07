class Personne:

    def __init__(self, nom, address):
        self._nom = nom
        self._adress = address

    def afficher(self):
        print(f"Nom: {self._nom}, Adress: {self._adress},", end=" ")

class Employe(Personne):

    def __init__(self, nom, address, cnss):
        super().__init__(nom, address)
        self._cnss = cnss

    def afficher(self):
        super().afficher()
        print(f"CNSS: {self._cnss}")

class Enseignant(Personne):

    def __init__(self, nom, address, cnops):
        super().__init__(nom, address)
        self._cnops = cnops

    def afficher(self):
        super().afficher()
        print(f"CNOPS: {self._cnops}")

class Etudiant(Personne):

    def __init__(self, nom, address, cne):
        super().__init__(nom, address)
        self._cne = cne

    def afficher(self):
        super().afficher()
        print(f"CNE: {self._cne}")

if __name__ == '__main__':

    p1 = Personne("jone", "casa")
    p2 = Personne("Kirk", "rabat")

    em1 = Employe("jimmi","casa", "dh789")
    em2 = Employe("dimebag","tangier", "dg579")

    en1 = Enseignant("Ozzy", "agadir", "jkhf09")
    en2 = Enseignant("Tony", "marakech", "rth554")

    et1 = Etudiant("james", "laayoun", "R867598765")
    et2 = Etudiant("randy", "usa", "R867456764")

    for personne in [p1, p2, em1, em2, en1, en2, et1,et2]:
        personne.afficher()
        print()


# on se basant sur les activites d'aujourdhui, les exception, les heritage les fichier propser une activite simple et pedagogique
# exemple dentre l'agregation et la composition
# dimonstartion de scraping