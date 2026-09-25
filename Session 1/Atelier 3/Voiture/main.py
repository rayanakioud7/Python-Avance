from Voiture import Voiture

vol = Voiture(152, "volvo", "15 chv", 15000)
vol.afficher()

vol.mod_kilo(300)
vol.mod_puiss("21 chv")
vol.afficher()

vo2= Voiture(134, "dacia", "17 chv", 60000)
vo2.afficher()

vo3= Voiture(15, "audi", "25 chv", 170000)
vo3.afficher()
