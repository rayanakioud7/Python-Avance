class Personne:

    def __init__(self, nom, address):
        self._nom = nom
        self._prenom = address

    def afficher(self):
        print(f"Nom: {self._nom}, Prenom: {self._prenom}")

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

    p1 = Personne("jone", "doe")
    p2 = Personne("Kirk", "Hammet")

    em1 = Employe("jimmi","Hendrix", "dh789")
    em2 = Employe("dimebag","darrel", "dg579")

    en1 = Enseignant("Ozzy", "Osbourne", "jkhf09")
    en2 = Enseignant("Tony", "Iommi", "rth554")

    et1 = Etudiant("james", "Hatefield", "R867598765")
    et2 = Etudiant("randy", "rhoades", "R867456764")

    for personne in [p1, p2, em1, em2, en1, en2, et1,et2]:
        personne.afficher()
        print('*'*20)

