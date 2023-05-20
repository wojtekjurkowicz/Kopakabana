import random

from zawodnicy import Druzyna, Zawodnik
from sedziowie import Sedziowie, Sedzia


class Rozgrywki:
    def __init__(self, lista_sedziow):
        self.lista_sedziow = lista_sedziow
        self.druzyny = {
            "siatkowka_plazowa": [],
            "dwa_ognie": [],
            "przeciaganie_liny": []
        }
        self.mecze = {
            "siatkowka_plazowa": [],
            "dwa_ognie": [],
            "przeciaganie_liny": []
        }
        self.wyniki = {
            "siatkowka_plazowa": [],
            "dwa_ognie": [],
            "przeciaganie_liny": []
        }
        self.polfinaly = {
            "siatkowka_plazowa": [],
            "dwa_ognie": [],
            "przeciaganie_liny": []
        }
        self.finaly = {
            "siatkowka_plazowa": [],
            "dwa_ognie": [],
            "przeciaganie_liny": []
        }
        self.zwyciezcy = {
            "siatkowka_plazowa": None,
            "dwa_ognie": None,
            "przeciaganie_liny": None
        }

    def dodaj_druzyne(self, druzyna):
        if len(druzyna.lista_zawodnikow) < 6:
            return f"Za malo zawodnikow!"
        else:
            for i in self.druzyny:
                self.druzyny[i].append(druzyna)

    def przeglad_druzyn(self):
        for druzyna in self.druzyny["dwa_ognie"]:
            print(druzyna.nazwa, druzyna.lista_zawodnikow)

    def utworz_spotkania(self, dyscyplina):
        for i in range(len(self.druzyny[dyscyplina])):
            for j in range(len(self.druzyny[dyscyplina])):
                if (i == j) \
                        or any((self.druzyny[dyscyplina][i].nazwa in mecz) and \
                               (self.druzyny[dyscyplina][j].nazwa in mecz) for mecz in self.mecze[dyscyplina]):
                    pass
                else:
                    mecz = [self.druzyny[dyscyplina][i].nazwa, self.druzyny[dyscyplina][j].nazwa]
                    self.mecze[dyscyplina].append(mecz)

        random.shuffle(self.mecze[dyscyplina])
        self.mecze[dyscyplina] = [random.choice(self.lista_sedziow), self.mecze[dyscyplina]]

    def symuluj_wyniki(self, druzyna, dyscyplina):
        for mecz in self.mecze[dyscyplina]:
            wynik_meczu = random.choice(mecz)
            self.wyniki[dyscyplina].append(wynik_meczu)
            if wynik_meczu == druzyna.nazwa:
                druzyna.dodaj_punkt(dyscyplina)

    def organizuj_polfinaly(self, dyscyplina):
        if len(self.druzyny[dyscyplina]) > 3:
            druzyny = self.druzyny[dyscyplina]
            druzyny.sort(key=lambda druzyna: druzyna.punkty[dyscyplina], reverse=True)
            polfinaly = druzyny[:4]
            self.polfinaly[dyscyplina] = polfinaly
        # wyniki półfinałów
        for mecz in self.polfinaly[dyscyplina]:
            finalista = random.choice(mecz)
            self.finaly[dyscyplina].append(finalista)

    def organizuj_finaly(self, dyscyplina):
        for mecz in self.finaly[dyscyplina]:
            zwyciezca = random.choice(mecz)
            self.zwyciezcy[dyscyplina] = zwyciezca


# Utworzenie obiektu sedziów
sedziowie = Sedziowie()

# Dodawanie sędziów
sedzia1 = Sedzia("Jan", "Kowalski")
sedziowie.dodaj_sedziego(sedzia1)

sedzia2 = Sedzia("Adam", "Nowak")
sedziowie.dodaj_sedziego(sedzia2)

sedzia3 = Sedzia("Anna", "Kwiatkowska")
sedziowie.dodaj_sedziego(sedzia3)

sedzia4 = Sedzia("Piotr", "Wójcik")
sedziowie.dodaj_sedziego(sedzia4)

sedzia5 = Sedzia("Maria", "Lewandowska")
sedziowie.dodaj_sedziego(sedzia5)

sedzia6 = Sedzia("Krzysztof", "Jankowski")
sedziowie.dodaj_sedziego(sedzia6)

sedzia7 = Sedzia("Magdalena", "Witkowska")
sedziowie.dodaj_sedziego(sedzia7)

druzyny = []

# Tworzenie drużyn
for i in range(16):
    nazwa_druzyny = f"Drużyna {i+1}"
    druzyna = Druzyna(nazwa_druzyny)
    for j in range(6):
        zawodnik = Zawodnik(f"Zawodnik {j+1}", f"Drużyna {i+1}")
        druzyna.zglos_zawodnika(zawodnik)
    druzyny.append(druzyna)

rozgrywki = Rozgrywki(sedziowie.lista_sedziow)

# Dodawanie drużyn do rozgrywek
for druzyna in druzyny:
    rozgrywki.dodaj_druzyne(druzyna)

# Utworzenie spotkań dla każdej dyscypliny
dyscypliny = ["siatkowka_plazowa", "dwa_ognie", "przeciaganie_liny"]
for dyscyplina in dyscypliny:
    rozgrywki.utworz_spotkania(dyscyplina)

# Symulacja wyników dla każdej drużyny w każdej dyscyplinie
for dyscyplina in dyscypliny:
    for druzyna in druzyny:
        rozgrywki.symuluj_wyniki(druzyna, dyscyplina)

# Organizacja półfinałów dla każdej dyscypliny
for dyscyplina in dyscypliny:
    rozgrywki.organizuj_polfinaly(dyscyplina)

# Organizacja finałów dla każdej dyscypliny
for dyscyplina in dyscypliny:
    rozgrywki.organizuj_finaly(dyscyplina)

# Wyświetlanie wyników
for dyscyplina in dyscypliny:
    print(f"Wyniki {dyscyplina}:")
    for i, mecz in enumerate(rozgrywki.finaly[dyscyplina]):
        print(f"Final {i+1}: {mecz}")
    print("")