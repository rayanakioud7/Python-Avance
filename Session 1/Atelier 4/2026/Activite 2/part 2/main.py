import re

def compter_mots(text):
    mots = re.findall(r'[a-zA-Z]+',text)
    return len(mots)


def creer_fichier(nom_fichier):
    try:
        with open(nom_fichier, 'w+') as f:
            pass
        print(f"Le fichier {nom_fichier} a ete cree avec succes")
    except Exception as e:
        print(f"Erreur: {e}")


def ajouter_lignes(nom_fichier):
    with open(nom_fichier, "a+") as file:

        ligne =input("enter une nouveau ligne: ")
        file.write(ligne+"\n")

def afficher(nom_fichier):
    with open(nom_fichier, "r+") as f:
        print(f.read())
        f.close()

def afficher_proprietes(nom_fichier):
    with open(nom_fichier, 'r') as f:
        contenu = f.read()
    nb_ligne = len(contenu.splitlines())
    nb_mot = compter_mots(contenu)
    nb_caracter = len(contenu)
    print(f"nombre des lignes: {nb_ligne}")
    print(f"nombre des mots: {nb_mot}")
    print(f"nombre des caracteres: {nb_caracter}")

if __name__ == '__main__':
    print(compter_mots("hey, everyone, how are you"))
    creer_fichier("test.txt")
    ajouter_lignes("test.txt")
    afficher("test.txt")
    afficher_proprietes("test.txt")