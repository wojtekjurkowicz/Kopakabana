import random # biblioteka do randomizacji
import pickle # biblioteka do zapisywania/odcytywania z pliku
from abc import ABC, abstractmethod # biblioteka do klas i metod abstrakcyjnych


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

    # dodawanie druzyn do rozgrywek
    def dodaj_druzyne(self, druzyna):
        if len(druzyna.lista_zawodnikow) < 6:
            return "Za malo zawodnikow!"
        else:
            self.druzyny.append(druzyna)

    # zwracanie listy druzyn
    def get_druzyny(self):
        return self.druzyny

    # wypisywanie listy druzyn
    def przeglad_druzyn(self):
        for druzyna in self.druzyny:
            print(druzyna)

    # metoda abstrakcyjna do tworzenia spotkan
    @abstractmethod
    def utworz_spotkania(self):
        pass

    # symulowanie wynikow meczu
    def symuluj_wyniki(self):
        for mecz in self.mecze:
            wynik_meczu = random.choice([mecz["druzyna1"], mecz["druzyna2"]])
            self.wyniki.append(wynik_meczu)

    # metoda abstrakcyjna do zapisywania punktow
    @abstractmethod
    def zapisz_punkty(self):
        pass

    # metoda abstrakcyjna do organizowania polfinalow
    # na podstawie ilosci zdobytych punktow
    @abstractmethod
    def organizuj_polfinaly(self):
        pass

    # metoda abstrakcyjna do organizowania finalow
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
        self.finalisci = []
        self.final = {}
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
                    print(druzyna)

    def organizuj_polfinaly(self):
        polfinalisci = []
        if len(self.druzyny) > 3:
            for druzyna in self.druzyny:
                print(druzyna.punkty_siatkowka)
            druzyny = self.druzyny
            druzyny.sort(key=lambda druzyna: druzyna.punkty_siatkowka, reverse=True)
            polfinalisci = druzyny[:4]
            random.shuffle(polfinalisci)
            self.polfinalisci = polfinalisci
            print(self.polfinalisci)


        polfinalisci_kopia = polfinalisci.copy()
        druzyna1 = random.choice(polfinalisci_kopia)
        polfinalisci_kopia.remove(druzyna1)
        druzyna2 = random.choice(polfinalisci_kopia)
        polfinalisci_kopia.remove(druzyna2)
        polfinal1 = {
            "sedzia": str(random.choice(self.lista_sedziow)),
            "sedzia_pom1": str(random.choice(self.lista_sedziow)),
            "sedzia_pom2": str(random.choice(self.lista_sedziow)),
            "druzyna1": druzyna1.nazwa,
            "druzyna2": druzyna2.nazwa
        }
        self.polfinaly.append(polfinal1)
        druzyna1 = polfinalisci_kopia[0]
        druzyna2 = polfinalisci_kopia[1]
        polfinal2 = {
            "sedzia": str(random.choice(self.lista_sedziow)),
            "sedzia_pom1": str(random.choice(self.lista_sedziow)),
            "sedzia_pom2": str(random.choice(self.lista_sedziow)),
            "druzyna1": druzyna1.nazwa,
            "druzyna2": druzyna2.nazwa
        }
        self.polfinaly.append(polfinal2)

    def organizuj_final(self):
        for mecz in self.polfinaly:
            finalista = random.choice([mecz["druzyna1"], mecz["druzyna2"]])
            self.finalisci.append(finalista)

        mecz = {
            "sedzia": str(random.choice(self.lista_sedziow)),
            "sedzia_pom1": str(random.choice(self.lista_sedziow)),
            "sedzia_pom2": str(random.choice(self.lista_sedziow)),
            "druzyna1": self.finalisci[0],
            "druzyna2": self.finalisci[1]
        }
        self.final = mecz
        zwyciezca = random.choice([self.final["druzyna1"], self.final["druzyna2"]])
        self.zwyciezca = zwyciezca

class Dwa_ognie(Rozgrywki):
    def __init__(self, lista_sedziow):
        super().__init__(lista_sedziow)
        self.druzyny = []
        self.mecze = []
        self.wyniki = []
        self.polfinaly = []
        self.finalisci = []
        self.final = {}
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
        polfinalisci = []
        if len(self.druzyny) > 3:
            for druzyna in self.druzyny:
                print(druzyna.punkty_siatkowka)
            druzyny = self.druzyny
            druzyny.sort(key=lambda druzyna: druzyna.punkty_dwa_ognie, reverse=True)
            polfinalisci = druzyny[:4]
            random.shuffle(polfinalisci)
            self.polfinalisci = polfinalisci
            print(self.polfinalisci)

        polfinalisci_kopia = polfinalisci.copy()
        druzyna1 = random.choice(polfinalisci_kopia)
        polfinalisci_kopia.remove(druzyna1)
        druzyna2 = random.choice(polfinalisci_kopia)
        polfinalisci_kopia.remove(druzyna2)
        polfinal1 = {
            "sedzia": str(random.choice(self.lista_sedziow)),
            "druzyna1": druzyna1.nazwa,
            "druzyna2": druzyna2.nazwa
        }
        self.polfinaly.append(polfinal1)
        druzyna1 = polfinalisci_kopia[0]
        druzyna2 = polfinalisci_kopia[1]
        polfinal2 = {
            "sedzia": str(random.choice(self.lista_sedziow)),
            "druzyna1": druzyna1.nazwa,
            "druzyna2": druzyna2.nazwa
        }
        self.polfinaly.append(polfinal2)

    def organizuj_final(self):
        for mecz in self.polfinaly:
            finalista = random.choice([mecz["druzyna1"], mecz["druzyna2"]])
            self.finalisci.append(finalista)

        mecz = {
            "sedzia": str(random.choice(self.lista_sedziow)),
            "druzyna1": self.finalisci[0],
            "druzyna2": self.finalisci[1]
        }
        self.final = mecz
        zwyciezca = random.choice([self.final["druzyna1"], self.final["druzyna2"]])
        self.zwyciezca = zwyciezca


class Przeciaganie_liny(Rozgrywki):
    def __init__(self, lista_sedziow):
        super().__init__(lista_sedziow)
        self.druzyny = []
        self.mecze = []
        self.wyniki = []
        self.polfinaly = []
        self.finalisci = []
        self.final = {}
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
        polfinalisci = []
        if len(self.druzyny) > 3:
            for druzyna in self.druzyny:
                print(druzyna.punkty_siatkowka)
            druzyny = self.druzyny
            druzyny.sort(key=lambda druzyna: druzyna.punkty_przeciaganie_liny, reverse=True)
            polfinalisci = druzyny[:4]
            random.shuffle(polfinalisci)
            self.polfinalisci = polfinalisci
            print(self.polfinalisci)

        polfinalisci_kopia = polfinalisci.copy()
        druzyna1 = random.choice(polfinalisci_kopia)
        polfinalisci_kopia.remove(druzyna1)
        druzyna2 = random.choice(polfinalisci_kopia)
        polfinalisci_kopia.remove(druzyna2)
        polfinal1 = {
            "sedzia": str(random.choice(self.lista_sedziow)),
            "druzyna1": druzyna1.nazwa,
            "druzyna2": druzyna2.nazwa
        }
        self.polfinaly.append(polfinal1)
        druzyna1 = polfinalisci_kopia[0]
        druzyna2 = polfinalisci_kopia[1]
        polfinal2 = {
            "sedzia": str(random.choice(self.lista_sedziow)),
            "druzyna1": druzyna1.nazwa,
            "druzyna2": druzyna2.nazwa
        }
        self.polfinaly.append(polfinal2)

    def organizuj_final(self):
        for mecz in self.polfinaly:
            finalista = random.choice([mecz["druzyna1"], mecz["druzyna2"]])
            self.finalisci.append(finalista)

        mecz = {
            "sedzia": str(random.choice(self.lista_sedziow)),
            "druzyna1": self.finalisci[0],
            "druzyna2": self.finalisci[1]
        }
        self.final = mecz
        zwyciezca = random.choice([self.final["druzyna1"], self.final["druzyna2"]])
        self.zwyciezca = zwyciezca

class Wyswietl_wyniki:
    def __init__(self, rozgrywki):
        self.rozgrywki = rozgrywki

    # tworzenie tablicy wynikow
    def generuj_tablice_wynikow(self):
        tablica = {}
        for druzyna in self.rozgrywki.get_druzyny():
            tablica[druzyna.nazwa] = {
                'siatkowka_plazowa': druzyna.punkty['siatkowka_plazowa'],
                'dwa_ognie': druzyna.punkty['dwa_ognie'],
                'przeciaganie_liny': druzyna.punkty['przeciaganie_liny']
            }
        return tablica

    # wyswietlanie tablicy wynikow
    def wyswietl_tablice_wynikow(self):
        tablica = self.generuj_tablice_wynikow()
        print("Tablica wynikow:")
        for druzyna, punkty in tablica.items():
            print(f"{druzyna}: {punkty}")


class Zapis_Odczyt:
    # zapisywanie do pliku
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

    # odczytywanie z pliku
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
