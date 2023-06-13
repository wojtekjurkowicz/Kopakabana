# klasa bazowa z ktorej dziedziczy Zawodnik i Sedzia
class Osoba:
    def __init__(self, imie, nazwisko):
        self._imie = imie
        self._nazwisko = nazwisko

    # getter do zwracania imienia
    def get_imie(self):
        return self._imie

    # getter do zwracania nazwiska
    def get_nazwisko(self):
        return self._nazwisko

    # metoda __str__ do sformatowanego wypisania imienia i nazwiska
    def __str__(self):
        return f"{self._imie} {self._nazwisko}"


class Zawodnik(Osoba):
    def __init__(self, imie, nazwisko):
        super().__init__(imie, nazwisko)


class Sedzia(Osoba):
    def __init__(self, imie, nazwisko):
        super().__init__(imie, nazwisko)


class Druzyna:
    def __init__(self, nazwa):
        self.nazwa = nazwa
        self.lista_zawodnikow = []
        self.punkty_siatkowka = 0
        self.punkty_dwa_ognie = 0
        self.punkty_przeciaganie_liny = 0

    # zglaszanie zawodnika do druzyny
    def zglos_zawodnika(self, zawodnik):
        if len(self.lista_zawodnikow) <= 6:
            self.lista_zawodnikow.append(zawodnik)
        else:
            return False

    # wycofywanie zawodnika z druzyny
    def wycofaj_zawodnika(self, zawodnik):
        if len(self.lista_zawodnikow) > 0:
            if zawodnik in self.lista_zawodnikow:
                self.lista_zawodnikow.remove(zawodnik)
            else:
                return f"Nie ma takiego zawodnika jak {zawodnik}"

    # 3 metody do dopisywania punktow dla odpowiednich rozgrywek
    def dodaj_punkt_siatkowka(self):
        self.punkty_siatkowka += 1

    def dodaj_punkt_dwa_ognie(self):
        self.punkty_dwa_ognie += 1

    def dodaj_punkt_przeciaganie_liny(self):
        self.punkty_przeciaganie_liny += 1

    # metoda __repr__ do reprezentowania sformatowanej listy zawodnikow
    def __repr__(self):
        return str([str(zawodnik) for zawodnik in self.lista_zawodnikow])


class Sedziowie:
    def __init__(self):
        self.lista_sedziow = []

    # dodawanie sedziego do rozgrywek
    def dodaj_sedziego(self, sedzia):
        self.lista_sedziow.append(sedzia)

    # usuwanie sedziego z rozgrywek
    def usun_sedziego(self, sedzia):
        if sedzia in self.lista_sedziow:
            self.lista_sedziow.remove(sedzia)
        else:
            return f"Nie ma takiego sedziego jak {sedzia}"

    # metoda __repr__ do reprezentowania sformatowanej listy sedziow
    def __repr__(self):
        return str([str(sedzia) for sedzia in self.lista_sedziow])

