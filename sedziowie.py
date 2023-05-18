class Kolegium:
    def __init__(self):
        self.lista_sedziow = []

    def dodaj_sedziego(self, sedzia):
        self.lista_sedziow.append(sedzia)

    def usun_sedziego(self, sedzia):
        if sedzia in self.lista_sedziow:
            self.lista_sedziow.remove(sedzia)
        else:
            return f"Nie ma takiego sedziego jak {sedzia}"

    def sedziowie(self):
        return self.lista_sedziow


class Sedzia:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def __str__(self):
        return f"{self.imie} {self.nazwisko}"
