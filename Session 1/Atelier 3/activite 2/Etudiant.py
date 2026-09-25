class Etudiant:
    count = 0
    def __init__(self, matricule, nom, prenom, note):
        self.matricule = matricule
        self.nom = nom
        self.prenom = prenom
        self.note = note
        Etudiant.count +=1

    def afficher(self):
        print(
            f"Les informations:\n"
            f"  Matricule: {self.matricule}\n"
            f"  Nom:       {self.nom}\n"
            f"  Prénom:    {self.prenom}\n"
            f"  Note:      {self.note:.2f}"
        )

if __name__ == "__main__":
    e1 = Etudiant(1, "akioud", "rayan", 14.6)
    e1.afficher()

    e2 = Etudiant(2, "yama", "amine", 17.6)
    e2.afficher()

    sum = 0
    for e in [e1, e2]:
        sum += e.note
    print("La somme: ", sum)

    if Etudiant.count > 0:
        print("Nombre des etudiants: ", Etudiant.count)
        moyenne = sum / Etudiant.count
        print(f"La moyenne: {moyenne:.2f}")