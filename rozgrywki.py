import random

from projekt.zawodnicy import Druzyna


class Rozgrywki:
    def __init__(self):
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
                        or (self.druzyny[dyscyplina][i] in self.mecze[dyscyplina]) and (self.druzyny[dyscyplina][j] in self.mecze[dyscyplina]):
                    pass
                else:
                    mecz = [self.druzyny[dyscyplina][i], self.druzyny[dyscyplina][j]]
                    self.mecze[dyscyplina].append(mecz)

        random.shuffle(self.mecze[dyscyplina])

    def symuluj_wyniki(self, druzyna, dyscyplina):
        for mecz in self.mecze[dyscyplina]:
            wynik_meczu = random.choice(mecz)
            self.wyniki[dyscyplina].append(wynik_meczu)
            if wynik_meczu == druzyna:
                druzyna.dodaj_punkt(dyscyplina)

    def organizuj_polfinaly(self, dyscyplina):
        if len(self.druzyny[dyscyplina]) > 3:
            druzyny = self.druzyny[dyscyplina]
            druzyny.sort(key=lambda druzyna: druzyna.punkty[dyscyplina], reverse=True)
            polfinaly = druzyny[:4]
            self.polfinaly[dyscyplina] = polfinaly



druzyna1 = Druzyna("FC Po Nalewce")
druzyna1.zglos_zawodnika("Wojtek Jurkowicz")
druzyna1.zglos_zawodnika("Adam Kowalski")
druzyna1.zglos_zawodnika("Adam Nowak")
druzyna1.zglos_zawodnika("Adam Kowal")
druzyna1.zglos_zawodnika("Jozef Kowal")
druzyna1.zglos_zawodnika("Andrzej Kowal")
druzyna1.wycofaj_zawodnika("Adam Nowak")
druzyna1.zglos_zawodnika("Mateusz Ziom")


druzyna2 = Druzyna("Orły Spod Budki")
druzyna2.zglos_zawodnika("Mateusz Ziom")
druzyna2.zglos_zawodnika("Piotr Nowak")
druzyna2.zglos_zawodnika("Marcin Kowalski")
druzyna2.zglos_zawodnika("Jan Nowak")
druzyna2.zglos_zawodnika("Kamil Kowal")
druzyna2.zglos_zawodnika("Bartek Kowal")


# Tworzenie rozgrywek
rozgrywki = Rozgrywki()

# Dodawanie drużyn do rozgrywek
rozgrywki.dodaj_druzyne(druzyna1)
rozgrywki.dodaj_druzyne(druzyna2)

# Wyświetlanie drużyn w rozgrywkach
rozgrywki.przeglad_druzyn()

# Tworzenie meczy
rozgrywki.utworz_spotkania("dwa_ognie")

# Symulacja wyników
rozgrywki.symuluj_wyniki(druzyna1, "dwa_ognie")
rozgrywki.symuluj_wyniki(druzyna2, "dwa_ognie")

# Organizowanie półfinałów
rozgrywki.organizuj_polfinaly("dwa_ognie")


