class Voiture:
    def __init__(self, code, marque, puissance, kilometrage):
        self.code = code
        self.marque = marque
        self.puissance = puissance
        self.kilometrage = kilometrage

    def mod_puiss(self, puiss):
        self.puissance = puiss

    def mod_kilo(self, kilo):
        self.kilometrage = kilo

    def afficher(self):
        print("code = ", self.code,
              ", marque = ", self.marque,
              ", puissance = ", self.puissance,
              ", kilometrage", self.kilometrage)

if __name__ == "__main__":
  vol = Voiture(152, "volvo", "15 chv", 15000)
  vol.afficher()

  vol.mod_kilo(300)
  vol.mod_puiss("21 chv")
  vol.afficher()

  vo2 = Voiture(134, "dacia", "17 chv", 60000)
  vo2.afficher()

  vo3 = Voiture(15, "audi", "25 chv", 170000)
  vo3.afficher()