class Zawodnik:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def __str__(self):
        return f"{self.imie} {self.nazwisko}"


class Druzyna:
    def __init__(self, nazwa, dyscyplina):
        self.nazwa = nazwa
        self.dyscyplina = dyscyplina
        self.liczba_zawodnikow = 0
        self.lista_zawodnikow = []
        self.punkty = 0

    def zglos_zawodnika(self, zawodnik):
        if self.liczba_zawodnikow < 6:
            self.lista_zawodnikow.append(zawodnik)
            self.liczba_zawodnikow += 1
        else:
            return False

    def wycofaj_zawodnika(self, zawodnik):
        if self.liczba_zawodnikow > 0:
            if zawodnik in self.lista_zawodnikow:
                self.lista_zawodnikow.remove(zawodnik)
                self.liczba_zawodnikow -= 1
            else:
                return f"Nie ma takiego zawodnika jak {zawodnik}"

    def dodaj_punkt(self):
        self.punkty += 1
    def przeglad_druzyny(self):
        return f"{self.nazwa}({self.dyscyplina}): {self.lista_zawodnikow}"

druzyna = Druzyna("FC Po Nalewce", "siatkowka_plazowa")
druzyna.zglos_zawodnika("Wojtek Jurkowicz")
druzyna.zglos_zawodnika("Adam Kowalski")
druzyna.zglos_zawodnika("Adam Nowak")
druzyna.zglos_zawodnika("Adam Kowal")
druzyna.zglos_zawodnika("Jozef Kowal")
druzyna.zglos_zawodnika("Andrzej Kowal")
druzyna.wycofaj_zawodnika("Adam Nowak")
druzyna.zglos_zawodnika("Mateusz Ziom")
print(druzyna.przeglad_druzyny())