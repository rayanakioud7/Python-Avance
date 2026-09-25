from Etudiant import Etudiant

e1 = Etudiant(1, "akioud", "rayan", 14.6)
e1.afficher()

e2 = Etudiant(2, "amin", "yama", 17.6)
e2.afficher()

sum = 0
for e in [e1, e2]:
    sum += e.note
print("La somme: ", sum)

if Etudiant.count > 0:
    moyenne = sum / Etudiant.count
    print(f"La moyenne: {moyenne:.2f}")