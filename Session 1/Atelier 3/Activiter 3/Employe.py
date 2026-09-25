from datetime import date



class Employe:

    current_year = 2026

    def __init__(self, id, nom, prenom, DateNaissance, DateEmbauche, Salaire):
        self._id = id
        self._nom = nom
        self._prenom = prenom
        self._DateNaissance = self._parse_date(DateNaissance)
        self._DateEmbauche = self._parse_date(DateEmbauche)
        self._Salaire = Salaire

    @property
    def nom(self) -> str:
        return self._nom

    @nom.setter
    def nom(self, new_nom: str) -> None:
        self._nom = new_nom

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, new_id: int) -> None:
        self._id = new_id

    @property
    def prenom(self) -> str:
        return self._prenom

    @prenom.setter
    def prenom(self, new_prenom: str) -> None:
        self._prenom = new_prenom

    @property
    def DateNaissance(self) -> date:
        return self._DateNaissance

    @DateNaissance.setter
    def DateNaissance(self, new_DateNaissance: str) -> None:
        self._DateNaissance = self._parse_date(new_DateNaissance)
        

    @property
    def DateEmbauche(self) -> date:
        return self._DateEmbauche

    @DateEmbauche.setter
    def DateEmbauche(self, new_DateEmbauche: str) -> None:
        self._DateEmbauche = self._parse_date(new_DateEmbauche)
        
    @property
    def Salaire(self) -> float:
        return self._Salaire

    @Salaire.setter
    def Salaire(self, new_salaire: float) -> None:
        self._Salaire = new_salaire 

    def Age(self) -> int:
        return Employe.current_year - self._DateNaissance.year

    def Anciennete(self) -> int:
        return Employe.current_year - self._DateEmbauche.year

    @staticmethod
    def _parse_date(value):
        if isinstance(value, date):
            return value
        if isinstance(value, str):
            return date.fromisoformat(value)
        raise TypeError(f"Date attendue, recu: {type(value)}")


if __name__ == '__main__':
    e1 = Employe(12, 'aziz', 'akioud', '1975-12-01', '2011-06-18', 56647.98)
    print(type(e1.DateNaissance), e1.Age(), e1.Anciennete())
    e2 = Employe(13, 'test', 't', date(1980, 1, 1), date(2020, 3, 1), 1000.0)
    print(type(e2.DateEmbauche), e2.Age())
