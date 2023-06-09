import random


class Rozgrywki:
    def __init__(self, lista_sedziow):
        self.lista_sedziow = lista_sedziow
        self.druzyny = []
        self.mecze = []
        self.wyniki = []
        """self.druzyny = {
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
"""
    def dodaj_druzyne(self, druzyna):
        if len(druzyna.lista_zawodnikow) < 6:
            return f"Za malo zawodnikow!"
        else:
            for i in self.druzyny:
                self.druzyny[i].append(druzyna)

    def przeglad_druzyn(self):
        for druzyna in self.druzyny:
            print(druzyna.nazwa, druzyna.lista_zawodnikow)

    def utworz_spotkania(self):
        for i in range(len(self.druzyny)):
            for j in range(len(self.druzyny)):
                if (i == j) or any(
                        (self.druzyny[i].nazwa == mecz["druzyna1"] and self.druzyny[j].nazwa ==
                         mecz["druzyna2"]) or
                        (self.druzyny[i].nazwa == mecz["druzyna2"] and self.druzyny[j].nazwa ==
                         mecz["druzyna1"])
                        for mecz in self.mecze
                ):
                    pass
                else:
                    mecz = {
                        "sedzia": random.choice(self.lista_sedziow),
                        "druzyna1": self.druzyny[i].nazwa,
                        "druzyna2": self.druzyny[j].nazwa
                    }
                    self.mecze.append(mecz)
                    print(mecz)

        random.shuffle(self.mecze)

    def symuluj_wyniki(self, druzyna, dyscyplina):
        for mecz in self.mecze:
            wynik_meczu = random.choice([mecz["druzyna1"], mecz["druzyna2"]])
            self.wyniki.append(wynik_meczu)
            if wynik_meczu == druzyna.nazwa:
                druzyna.dodaj_punkt(dyscyplina)



    def organizuj_polfinaly(self, dyscyplina):
        if len(self.druzyny[dyscyplina]) > 3:
            druzyny = self.druzyny[dyscyplina]
            druzyny.sort(key=lambda druzyna: druzyna.punkty[dyscyplina], reverse=True)
            polfinaly = druzyny[:4]
            self.polfinaly[dyscyplina] = polfinaly
            print(self.polfinaly)
        # wyniki półfinałów
        for mecz in self.polfinaly[dyscyplina]:
            finalista = self.symuluj_wyniki(druzyna, dyscyplina)
            self.finaly[dyscyplina].append(finalista)

    def organizuj_finaly(self, dyscyplina):
        for mecz in self.finaly[dyscyplina]:
            zwyciezca = random.choice(mecz)
            self.zwyciezcy[dyscyplina].append(zwyciezca)

class Siatkowka_plazowa(Rozgrywki):
    def __init__(self, lista_sedziow):
        super().__init__(lista_sedziow)
        self.druzyny = []


    def utworz_spotkania(self):
        for i in range(len(self.druzyny)):
            for j in range(len(self.druzyny)):
                if (i == j) or any(
                        (self.druzyny[i].nazwa == mecz["druzyna1"] and self.druzyny[j].nazwa ==
                         mecz["druzyna2"]) or
                        (self.druzyny[i].nazwa == mecz["druzyna2"] and self.druzyny[j].nazwa ==
                         mecz["druzyna1"])
                        for mecz in self.mecze
                ):
                    pass
                else:
                    mecz = {
                        "sedzia": random.choice(self.lista_sedziow),
                        "sedzia_pom1": random.choice(self.lista_sedziow),
                        "sedzia_pom2": random.choice(self.lista_sedziow),
                        "druzyna1": self.druzyny[i].nazwa,
                        "druzyna2": self.druzyny[j].nazwa
                    }
                    self.mecze.append(mecz)
                    print(mecz)

        random.shuffle(self.mecze)

class Dwa_ognie(Rozgrywki):
    def __init__(self, lista_sedziow):
        super().__init__(lista_sedziow)
        self.druzyny = []


class Przeciaganie_liny:
    def __init__(self, lista_sedziow):
        super().__init__(lista_sedziow)
        self.druzyny = []



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
