import random
import pickle
from abc import ABC, abstractmethod

class Rozgrywki(ABC):
    def __init__(self, lista_sedziow):
        self.lista_sedziow = lista_sedziow
        self.druzyny = []
        self.mecze = []
        self.wyniki = {
            "siatkowka_plazowa": [],
            "dwa_ognie": [],
            "przeciaganie_liny": []
        }
        self.polfinalisci = []
        self.polfinaly = []
        self.finaly = []
        self.zwyciezca = None
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
            return "Za malo zawodnikow!"
        else:
            self.druzyny.append(druzyna)

    def get_druzyny(self):
        return self.druzyny

    def przeglad_druzyn(self):
        for druzyna in self.druzyny:
            print(druzyna)

    @abstractmethod
    def utworz_spotkania(self):
        pass

    def symuluj_wyniki(self, dyscyplina):
        for mecz in self.mecze:
            wynik_meczu = random.choice([mecz["druzyna1"], mecz["druzyna2"]])
            self.wyniki[dyscyplina].append(wynik_meczu)

    def zapisz_punkty(self, dyscyplina):
        for druzyna in self.druzyny:
            for wynik in self.wyniki[dyscyplina]:
                if wynik == druzyna.nazwa:
                    druzyna.dodaj_punkt(dyscyplina)

    def organizuj_polfinaly(self, dyscyplina):
        if len(self.druzyny) > 3:
            druzyny = self.druzyny
            druzyny.sort(key=lambda druzyna: druzyna.punkty[dyscyplina], reverse=True)
            polfinalisci = druzyny[:4]
            random.shuffle(polfinalisci)
            self.polfinalisci = polfinalisci

        for i in range(int(len(self.polfinalisci)/2)):
            druzyna1 = random.choice(self.polfinalisci)
            druzyna2 = random.choice(self.polfinalisci)
            self.polfinalisci.remove(druzyna1)
            self.polfinalisci.remove(druzyna2)
            polfinal = {
                "sedzia": random.choice(self.lista_sedziow),
                "druzyna1": druzyna1,
                "druzyna2": druzyna2
            }
            self.polfinaly.append(polfinal)

        print("Polfinal 1: ", self.polfinaly[0]["druzyna1"], self.polfinaly[0]["druzyna2"])
        print("Polfinal 2: ", self.polfinaly[1]["druzyna1"], self.polfinaly[1]["druzyna2"])


    def organizuj_finaly(self, dyscyplina):
        for i in range(len(self.polfinaly)):
            polfinal = self.polfinaly[i]
            finalista = random.choice([polfinal["druzyna1"], polfinal["druzyna2"]])
            self.finaly.append(finalista)
            print(self.finaly)

        for i in range(len(self.finaly)):
            for j in range(i + 1, len(self.finaly)):
                mecz = {
                    "sedzia": random.choice(self.lista_sedziow),
                    "druzyna1": self.finaly[i],
                    "druzyna2": self.finaly[j]
                }
                self.finaly.append(mecz)


        zwyciezca = random.choice([self.finaly[0]["druzyna1"], self.finaly[0]["druzyna2"]])
        self.zwyciezca = zwyciezca

class Siatkowka_plazowa(Rozgrywki):
    def __init__(self, lista_sedziow):
        super().__init__(lista_sedziow)
        self.druzyny = []
        self.mecze = []
        self.wyniki = []
        self.polfinaly = []
        self.finaly = []
        self.zwyciezca = None

    def utworz_spotkania(self):
        for i in range(len(self.druzyny)):
            for j in range(i + 1, len(self.druzyny)):
                if (i == j) or any(
                        (self.druzyny[i].nazwa == mecz["druzyna1"] and self.druzyny[j].nazwa ==
                         mecz["druzyna2"]) or
                        (self.druzyny[i].nazwa == mecz["druzyna2"] and self.druzyny[j].nazwa ==
                         mecz["druzyna1"])
                        for mecz in self.mecze
                ):
                    continue
                else:
                    sedzia = random.choice(self.lista_sedziow)
                    sedzia = f"{sedzia.imie} {sedzia.nazwisko}"
                    while True:
                        sedzia_pom1 = random.choice(self.lista_sedziow)
                        if sedzia_pom1 == sedzia:
                            continue
                        else:
                            sedzia_pom1 = f"{sedzia.imie} {sedzia.nazwisko}"
                            break

                    while True:
                        sedzia_pom2 = random.choice(self.lista_sedziow)
                        if sedzia_pom1 == sedzia_pom2 or sedzia == sedzia_pom2:
                            continue
                        else:
                            sedzia_pom2 = f"{sedzia.imie} {sedzia.nazwisko}"
                            break

                    mecz = {
                        "sedzia": sedzia,
                        "sedzia_pom1": sedzia_pom1,
                        "sedzia_pom2": sedzia_pom2,
                        "druzyna1": self.druzyny[i].nazwa,
                        "druzyna2": self.druzyny[j].nazwa
                    }
                    self.mecze.append(mecz)
                    print(str(mecz))

        random.shuffle(self.mecze)

    def organizuj_polfinaly(self, dyscyplina):
        if len(self.druzyny[dyscyplina]) > 3:
            druzyny = self.druzyny[dyscyplina]
            druzyny.sort(key=lambda druzyna: druzyna.punkty[dyscyplina], reverse=True)
            polfinalisci = druzyny[:4]
            random.shuffle(polfinalisci)
            self.polfinalisci = polfinalisci
            print(self.polfinalisci)

        for i in range(len(self.polfinalisci)):
            for j in range(i + 1, len(self.polfinalisci)):
                mecz = {
                    "sedzia": random.choice(self.lista_sedziow),
                    "sedzia_pom1": random.choice(self.lista_sedziow),
                    "sedzia_pom2": random.choice(self.lista_sedziow),
                    "druzyna1": self.polfinalisci[i].nazwa,
                    "druzyna2": self.polfinalisci[j].nazwa
                }
                self.polfinaly.append(mecz)

    def organizuj_finaly(self, dyscyplina):
        for mecz in self.polfinaly[dyscyplina]:
            finalista = random.choice([mecz["druzyna1"], mecz["druzyna2"]])
            self.finaly.append(finalista)

        for i in range(len(self.finaly)):
            for j in range(i + 1, len(self.finaly)):
                mecz = {
                    "sedzia": random.choice(self.lista_sedziow),
                    "sedzia_pom1": random.choice(self.lista_sedziow),
                    "sedzia_pom2": random.choice(self.lista_sedziow),
                    "druzyna1": self.finaly[i],
                    "druzyna2": self.finaly[j]
                }
                self.finaly.append(mecz)

        for mecz in self.finaly:
            zwyciezca = random.choice([mecz["druzyna1"], mecz["druzyna2"]])
            self.zwyciezca = zwyciezca

class Dwa_ognie(Rozgrywki):
    def __init__(self, lista_sedziow):
        super().__init__(lista_sedziow)
        self.druzyny = []
        self.mecze = []
        self.wyniki = []
        self.polfinaly = []
        self.finaly = []
        self.zwyciezca = None

    def utworz_spotkania(self):
        for i in range(len(self.druzyny)):
            for j in range(i + 1, len(self.druzyny)): # i + 1 aby ostatnia druzyna nie byla porownywana z sama soba
                if (i == j) or any(
                        (self.druzyny[i].nazwa == mecz["druzyna1"] and self.druzyny[j].nazwa ==
                         mecz["druzyna2"]) or
                        (self.druzyny[i].nazwa == mecz["druzyna2"] and self.druzyny[j].nazwa ==
                         mecz["druzyna1"])
                        for mecz in self.mecze
                ):
                    continue
                else:
                    sedzia = random.choice(self.lista_sedziow)
                    sedzia = f"{sedzia.imie} {sedzia.nazwisko}"
                    mecz = {
                        "sedzia": sedzia,
                        "druzyna1": self.druzyny[i].nazwa,
                        "druzyna2": self.druzyny[j].nazwa
                    }
                    self.mecze.append(mecz)
                    print(mecz)

        random.shuffle(self.mecze)

class Przeciaganie_liny(Rozgrywki):
    def __init__(self, lista_sedziow):
        super().__init__(lista_sedziow)
        self.druzyny = []
        self.mecze = []
        self.wyniki = []
        self.polfinaly = []
        self.finaly = []
        self.zwyciezca = None

    def utworz_spotkania(self):
        for i in range(len(self.druzyny)):
            for j in range(i + 1, len(self.druzyny)): # i + 1 aby ostatnia druzyna nie byla porownywana z sama soba
                if (i == j) or any(
                        (self.druzyny[i].nazwa == mecz["druzyna1"] and self.druzyny[j].nazwa ==
                         mecz["druzyna2"]) or
                        (self.druzyny[i].nazwa == mecz["druzyna2"] and self.druzyny[j].nazwa ==
                         mecz["druzyna1"])
                        for mecz in self.mecze
                ):
                    continue
                else:
                    sedzia = random.choice(self.lista_sedziow)
                    sedzia = f"{sedzia.imie} {sedzia.nazwisko}"
                    mecz = {
                        "sedzia": sedzia,
                        "druzyna1": self.druzyny[i].nazwa,
                        "druzyna2": self.druzyny[j].nazwa
                    }
                    self.mecze.append(mecz)
                    print(mecz)

        random.shuffle(self.mecze)


class Wyswietl_wyniki:
    def __init__(self, rozgrywki):
        self.rozgrywki = rozgrywki

    def generuj_tablice_wynikow(self):
        tablica = {}
        for druzyna in self.rozgrywki.get_druzyny():
            tablica[druzyna.nazwa] = {
                'siatkowka_plazowa': druzyna.punkty['siatkowka_plazowa'],
                'dwa_ognie': druzyna.punkty['dwa_ognie'],
                'przeciaganie_liny': druzyna.punkty['przeciaganie_liny']
            }
        return tablica

    def wyswietl_tablice_wynikow(self):
        tablica = self.generuj_tablice_wynikow()
        print("Tablica wynikow:")
        for druzyna, punkty in tablica.items():
            print(f"{druzyna}: {punkty}")


class Zapis_Odczyt:
    def zapisz(self, nazwa):
        dane = {
            'druzyny': self.druzyny,
            'mecze': self.mecze,
            'wyniki': self.wyniki,
            'polfinalisci': self.polfinalisci,
            'polfinaly': self.polfinaly,
            'finaly': self.finaly,
            'zwyciezca': self.zwyciezca
        }
        with open(nazwa, 'wb') as plik:
            pickle.dump(dane, plik)

    def zapisz_stan(self, nazwa):
        with open(nazwa, 'rb') as plik:
            dane = pickle.load(plik)
        self.druzyny = dane['druzyny']
        self.mecze = dane['mecze']
        self.wyniki = dane['wyniki']
        self.polfinalisci = dane['polfinalisci']
        self.polfinaly = dane['polfinaly']
        self.finaly = dane['finaly']
        self.zwyciezca = dane['zwyciezca']
