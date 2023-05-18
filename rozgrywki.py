import random
from zawodnicy import Druzyna, Zawodnik


class Rozgrywki:
    def __init__(self):
        self.druzyny = {
            "siatkowka_plazowa": [],
            "dwa_ognie": [],
            "przeciaganie_liny": []
        }
        self.dostepne_druzyny = {
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
        self.punkty_druzyny = {
            "siatkowka_plazowa": [],
            "dwa_ognie": [],
            "przeciaganie_liny": []
        }

    def dodaj_druzyne(self, druzyna, dyscyplina):
        if druzyna.liczba_zawodnikow < 6:
            return f"Za malo zawodnikow!"
        else:
            self.druzyny[dyscyplina].append(druzyna)
            self.dostepne_druzyny[dyscyplina].append(druzyna)

    def przeglad_druzyn(self, dyscyplina):
        for druzyna in self.druzyny[dyscyplina]:
            print(druzyna.nazwa, druzyna.lista_zawodnikow)

    def utworz_spotkania(self, dyscyplina):
        for i in range(len(self.druzyny[dyscyplina])):
            for j in range(len(self.druzyny[dyscyplina])):
                if (i == j) \
                        or (self.druzyny[dyscyplina][i] in self.mecze[dyscyplina]) \
                        or (self.druzyny[dyscyplina][j] in self.mecze[dyscyplina]):
                    pass
                else:
                    mecz = [self.druzyny[dyscyplina][i], self.druzyny[dyscyplina][j]]
                    self.mecze[dyscyplina].append(mecz)

        random.shuffle(self.mecze[dyscyplina])

    def symuluj_wyniki(self, druzyna, dyscyplina):
        for mecz in self.mecze[dyscyplina]:
            self.wyniki[dyscyplina].append(random.choice(mecz))
        for wynik in self.wyniki[dyscyplina]:
            if self.wyniki[dyscyplina][wynik] == druzyna.nazwa:
                druzyna.dodaj_punkt()

"""    def organizuj_polfinaly(self, dyscyplina):
        for druzyna in self.druzyny[dyscyplina]:
"""