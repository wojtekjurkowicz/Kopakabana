from rozgrywki import Rozgrywki, Wyswietl_wyniki
from sedziowie import Sedziowie, Sedzia
from zawodnicy import Druzyna, Zawodnik

sedziowie = Sedziowie()

# Dodawanie sędziów
sedzia1 = Sedzia("Jan", "Kowalski")
sedziowie.dodaj_sedziego(sedzia1)

sedzia2 = Sedzia("Adam", "Nowak")
sedziowie.dodaj_sedziego(sedzia2)

sedzia3 = Sedzia("Anna", "Kwiatkowska")
sedziowie.dodaj_sedziego(sedzia3)

sedzia4 = Sedzia("Piotr", "Wójcik")
sedziowie.dodaj_sedziego(sedzia4)

sedzia5 = Sedzia("Maria", "Lewandowska")
sedziowie.dodaj_sedziego(sedzia5)

sedzia6 = Sedzia("Krzysztof", "Jankowski")
sedziowie.dodaj_sedziego(sedzia6)

sedzia7 = Sedzia("Magdalena", "Witkowska")
sedziowie.dodaj_sedziego(sedzia7)


druzyny = []
# Tworzenie drużyn
for i in range(8):
    nazwa_druzyny = f"Drużyna {i+1}"
    druzyna = Druzyna(nazwa_druzyny)
    for j in range(6):
        zawodnik = Zawodnik(f"Zawodnik {j+1}", f"Drużyna {i+1}")
        druzyna.zglos_zawodnika(zawodnik)
    druzyny.append(druzyna)

rozgrywki = Rozgrywki(sedziowie.lista_sedziow)

for druzyna in druzyny:
    rozgrywki.dodaj_druzyne(druzyna)

rozgrywki.przeglad_druzyn()

rozgrywki.utworz_spotkania()

rozgrywki.symuluj_wyniki("siatkowka_plazowa")
rozgrywki.zapisz_punkty("siatkowka_plazowa")
rozgrywki.symuluj_wyniki("dwa_ognie")
rozgrywki.symuluj_wyniki("przeciaganie_liny")

rozgrywki.organizuj_polfinaly("siatkowka_plazowa")

rozgrywki.organizuj_finaly("siatkowka_plazowa")
