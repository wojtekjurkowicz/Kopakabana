class Osoba:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def __str__(self):
        return f"{self.imie} {self.nazwisko}"

class Zawodnik(Osoba):
    def __init__(self, imie, nazwisko):
        super().__init__(imie, nazwisko)


class Druzyna:
    def __init__(self, nazwa):
        self.nazwa = nazwa
        self.lista_zawodnikow = []
        self.punkty = {
            "siatkowka_plazowa": 0,
            "dwa_ognie": 0,
            "przeciaganie_liny": 0
        }

    def zglos_zawodnika(self, zawodnik):
        if len(self.lista_zawodnikow) <= 6:
            self.lista_zawodnikow.append(zawodnik)
        else:
            return False

    def wycofaj_zawodnika(self, zawodnik):
        if len(self.lista_zawodnikow) > 0:
            if zawodnik in self.lista_zawodnikow:
                self.lista_zawodnikow.remove(zawodnik)
            else:
                return f"Nie ma takiego zawodnika jak {zawodnik}"

    def dodaj_punkt(self, dyscyplina):
        self.punkty[dyscyplina] += 1

    def przeglad_zawodnikow(self):
        for zawodnik in self.lista_zawodnikow:
            print(zawodnik, end=", ")

    def __repr__(self):
        return str(repr(self.nazwa)) + ": " + str(repr(self.przeglad_zawodnikow()))
