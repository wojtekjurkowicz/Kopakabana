import random


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
                if (i == j) or any(
                        (self.druzyny[dyscyplina][i].nazwa == mecz["druzyna1"] and self.druzyny[dyscyplina][j].nazwa ==
                         mecz["druzyna2"]) or
                        (self.druzyny[dyscyplina][i].nazwa == mecz["druzyna2"] and self.druzyny[dyscyplina][j].nazwa ==
                         mecz["druzyna1"])
                        for mecz in self.mecze[dyscyplina]
                ):
                    pass
                else:
                    mecz = {
                        "sedzia": random.choice(self.lista_sedziow),
                        "druzyna1": self.druzyny[dyscyplina][i].nazwa,
                        "druzyna2": self.druzyny[dyscyplina][j].nazwa
                    }
                    self.mecze[dyscyplina].append(mecz)

        random.shuffle(self.mecze[dyscyplina])

    def symuluj_wyniki(self, druzyna, dyscyplina):
        for mecz in self.mecze[dyscyplina]:
            wynik_meczu = random.choice([mecz["druzyna1"], mecz["druzyna2"]])
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
            self.zwyciezcy[dyscyplina].append(zwyciezca)


class Wyswietl_wyniki(Rozgrywki):
    def __init__(self, lista_sedziow):
        super().__init__(lista_sedziow)

    def wyswietl_wyniki(self, dyscyplina):
        print("Wyniki rozgrywek w dyscyplinie", dyscyplina)
        for mecz, wynik in zip(self.mecze[dyscyplina], self.wyniki[dyscyplina]):
            druzyna1, druzyna2 = mecz
            sedzia = mecz[0]
            zwyciezca = "Remis" if wynik == "Remis" else (druzyna1 if wynik == druzyna1 else druzyna2)
            print("Mecz:", druzyna1, "vs", druzyna2)
            print("Sędzia:", sedzia)
            print("Zwycięzca:", zwyciezca)
            print("----------------------")
