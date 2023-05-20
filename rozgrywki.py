import random
from zawodnicy import Druzyna, Zawodnik

class Rozgrywki:
    def __init__(self):
        self.druzyny = []
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

    def dodaj_druzyne(self, druzyna):
        if len(druzyna.lista_zawodnikow) < 6:
            return f"Za malo zawodnikow!"
        else:
            self.druzyny.append(druzyna)

    def przeglad_druzyn(self):
        for druzyna in self.druzyny:
            print(druzyna.nazwa, druzyna.lista_zawodnikow)

    def utworz_spotkania(self, dyscyplina):
        for i in range(len(self.druzyny)):
            for j in range(len(self.druzyny)):
                if (i == j) \
                        or (self.druzyny[i] in self.mecze[dyscyplina]) and (self.druzyny[j] in self.mecze[dyscyplina]):
                    pass
                else:
                    mecz = [self.druzyny[i], self.druzyny[j]]
                    self.mecze[dyscyplina].append(mecz)

        random.shuffle(self.mecze[dyscyplina])

    def symuluj_wyniki(self, druzyna, dyscyplina):
        for mecz in self.mecze[dyscyplina]:
            self.wyniki[dyscyplina].append(random.choice(mecz))
        for wynik in self.wyniki[dyscyplina]:
            if self.wyniki[dyscyplina][wynik] == druzyna.nazwa:
                druzyna.dodaj_punkt(dyscyplina)

    def organizuj_polfinaly(self, dyscyplina):
        for
