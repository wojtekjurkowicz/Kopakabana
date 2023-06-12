import random
import pickle
from abc import ABC, abstractmethod


class Rozgrywki(ABC):
    def __init__(self, lista_sedziow):
        self.lista_sedziow = lista_sedziow
        self.druzyny = []
        self.mecze = []
        self.wyniki = []
        self.polfinalisci = []
        self.polfinaly = []
        self.final = []
        self.zwyciezca = None

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

    def symuluj_wyniki(self):
        for mecz in self.mecze:
            wynik_meczu = random.choice([mecz["druzyna1"], mecz["druzyna2"]])
            self.wyniki.append(wynik_meczu)

    @abstractmethod
    def zapisz_punkty(self):
        pass

    @abstractmethod
    def organizuj_polfinaly(self):
        pass

    @abstractmethod
    def organizuj_final(self):
        pass


class Siatkowka_plazowa(Rozgrywki):
    def __init__(self, lista_sedziow):
        super().__init__(lista_sedziow)
        self.druzyny = []
        self.mecze = []
        self.wyniki = []
        self.polfinaly = []
        self.final = []
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
                    while True:
                        sedzia_pom1 = random.choice(self.lista_sedziow)
                        if sedzia_pom1 == sedzia:
                            continue
                        else:
                            break

                    while True:
                        sedzia_pom2 = random.choice(self.lista_sedziow)
                        if sedzia_pom1 == sedzia_pom2 or sedzia == sedzia_pom2:
                            continue
                        else:
                            break

                    mecz = {
                        "sedzia": str(sedzia),
                        "sedzia_pom1": str(sedzia_pom1),
                        "sedzia_pom2": str(sedzia_pom2),
                        "druzyna1": self.druzyny[i].nazwa,
                        "druzyna2": self.druzyny[j].nazwa
                    }
                    self.mecze.append(mecz)
                    print(str(mecz))

        random.shuffle(self.mecze)

    def zapisz_punkty(self):
        for druzyna in self.druzyny:
            for wynik in self.wyniki:
                if wynik == druzyna.nazwa:
                    druzyna.dodaj_punkt_siatkowka()

    def organizuj_polfinaly(self):
        if len(self.druzyny) > 3:
            druzyny = self.druzyny
            druzyny.sort(key=lambda druzyna: druzyna.punkty_siatkowka, reverse=True)
            polfinalisci = druzyny[:4]
            random.shuffle(polfinalisci)
            self.polfinalisci = polfinalisci
            print(self.polfinalisci)

        for i in range(len(self.polfinalisci)):
            for j in range(i + 1, len(self.polfinalisci)):
                mecz = {
                    "sedzia": str(random.choice(self.lista_sedziow)),
                    "sedzia_pom1": str(random.choice(self.lista_sedziow)),
                    "sedzia_pom2": str(random.choice(self.lista_sedziow)),
                    "druzyna1": self.polfinalisci[i].nazwa,
                    "druzyna2": self.polfinalisci[j].nazwa
                }
                self.polfinaly.append(mecz)

    def organizuj_final(self):
        for mecz in self.polfinaly:
            finalista = random.choice([mecz["druzyna1"], mecz["druzyna2"]])
            self.final.append(finalista)

        mecz = {
            "sedzia": str(random.choice(self.lista_sedziow)),
            "sedzia_pom1": str(random.choice(self.lista_sedziow)),
            "sedzia_pom2": str(random.choice(self.lista_sedziow)),
            "druzyna1": self.final[0],
            "druzyna2": self.final[1]
        }
        zwyciezca = random.choice([mecz["druzyna1"], mecz["druzyna2"]])
        self.zwyciezca = zwyciezca

class Dwa_ognie(Rozgrywki):
    def __init__(self, lista_sedziow):
        super().__init__(lista_sedziow)
        self.druzyny = []
        self.mecze = []
        self.wyniki = []
        self.polfinaly = []
        self.final = []
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
                    mecz = {
                        "sedzia": str(random.choice(self.lista_sedziow)),
                        "druzyna1": self.druzyny[i].nazwa,
                        "druzyna2": self.druzyny[j].nazwa
                    }
                    self.mecze.append(mecz)
                    print(str(mecz))

        random.shuffle(self.mecze)

    def zapisz_punkty(self):
        for druzyna in self.druzyny:
            for wynik in self.wyniki:
                if wynik == druzyna.nazwa:
                    druzyna.dodaj_punkt_dwa_ognie()

    def organizuj_polfinaly(self):
        if len(self.druzyny) > 3:
            druzyny = self.druzyny
            druzyny.sort(key=lambda druzyna: druzyna.punkty_dwa_ognie, reverse=True)
            polfinalisci = druzyny[:4]
            random.shuffle(polfinalisci)
            self.polfinalisci = polfinalisci
            print(self.polfinalisci)

        for i in range(len(self.polfinalisci)):
            for j in range(i + 1, len(self.polfinalisci)):
                mecz = {
                    "sedzia": str(random.choice(self.lista_sedziow)),
                    "druzyna1": self.polfinalisci[i].nazwa,
                    "druzyna2": self.polfinalisci[j].nazwa
                }
                self.polfinaly.append(mecz)

    def organizuj_final(self):
        for mecz in self.polfinaly:
            finalista = random.choice([mecz["druzyna1"], mecz["druzyna2"]])
            self.final.append(finalista)

        mecz = {
            "sedzia": str(random.choice(self.lista_sedziow)),
            "druzyna1": self.final[0],
            "druzyna2": self.final[1]
        }
        zwyciezca = random.choice([mecz["druzyna1"], mecz["druzyna2"]])
        self.zwyciezca = zwyciezca


class Przeciaganie_liny(Rozgrywki):
    def __init__(self, lista_sedziow):
        super().__init__(lista_sedziow)
        self.druzyny = []
        self.mecze = []
        self.wyniki = []
        self.polfinaly = []
        self.final = []
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
                    mecz = {
                        "sedzia": str(random.choice(self.lista_sedziow)),
                        "druzyna1": self.druzyny[i].nazwa,
                        "druzyna2": self.druzyny[j].nazwa
                    }
                    self.mecze.append(mecz)
                    print(mecz)

        random.shuffle(self.mecze)

    def zapisz_punkty(self):
        for druzyna in self.druzyny:
            for wynik in self.wyniki:
                if wynik == druzyna.nazwa:
                    druzyna.dodaj_punkt_przeciaganie_liny()

    def organizuj_polfinaly(self):
        if len(self.druzyny) > 3:
            druzyny = self.druzyny
            druzyny.sort(key=lambda druzyna: druzyna.punkty_przeciaganie_liny, reverse=True)
            polfinalisci = druzyny[:4]
            random.shuffle(polfinalisci)
            self.polfinalisci = polfinalisci
            print(self.polfinalisci)

        for i in range(len(self.polfinalisci)):
            for j in range(i + 1, len(self.polfinalisci)):
                mecz = {
                    "sedzia": str(random.choice(self.lista_sedziow)),
                    "druzyna1": self.polfinalisci[i].nazwa,
                    "druzyna2": self.polfinalisci[j].nazwa
                }
                self.polfinaly.append(mecz)

    def organizuj_final(self):
        for mecz in self.polfinaly:
            finalista = random.choice([mecz["druzyna1"], mecz["druzyna2"]])
            self.final.append(finalista)

        mecz = {
            "sedzia": str(random.choice(self.lista_sedziow)),
            "druzyna1": self.final[0],
            "druzyna2": self.final[1]
        }
        zwyciezca = random.choice([mecz["druzyna1"], mecz["druzyna2"]])
        self.zwyciezca = zwyciezca


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
            'final': self.final,
            'zwyciezca': self.zwyciezca
        }
        with open(nazwa, 'wb') as plik:
            pickle.dump(dane, plik)

    def odczyt(self, nazwa):
        with open(nazwa, 'rb') as plik:
            dane = pickle.load(plik)
        self.druzyny = dane['druzyny']
        self.mecze = dane['mecze']
        self.wyniki = dane['wyniki']
        self.polfinalisci = dane['polfinalisci']
        self.polfinaly = dane['polfinaly']
        self.final = dane['final']
        self.zwyciezca = dane['zwyciezca']
