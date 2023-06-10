from zawodnicy import Osoba
class Sedziowie:
    def __init__(self):
        self.lista_sedziow = []

    def dodaj_sedziego(self, sedzia):
        self.lista_sedziow.append(sedzia)

    def usun_sedziego(self, sedzia):
        if sedzia in self.lista_sedziow:
            self.lista_sedziow.remove(sedzia)
        else:
            return f"Nie ma takiego sedziego jak {sedzia}"

    def przeglad_sedziow(self):
        for sedzia in self.lista_sedziow:
            print(sedzia, end=", ")
    def __repr__(self):
        return str(repr(self.przeglad_sedziow()))


class Sedzia(Osoba):
    def __init__(self, imie, nazwisko):
        super().__init__(imie, nazwisko)

