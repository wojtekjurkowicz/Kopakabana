from rozgrywki import Wyswietl_wyniki, Dwa_ognie, Przeciaganie_liny
# from sedziowie import Sedziowie, Sedzia
from zawodnicy import Druzyna, Zawodnik, Sedziowie, Sedzia

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
for i in range(6):
    nazwa_druzyny = f"Drużyna {i+1}"
    druzyna = Druzyna(nazwa_druzyny)
    for j in range(6):
        zawodnik = Zawodnik(f"Zawodnik {j+1}", f"Drużyna {i+1}")
        druzyna.zglos_zawodnika(zawodnik)
    druzyny.append(druzyna)

siatkowka = Przeciaganie_liny(sedziowie.lista_sedziow)

for druzyna in druzyny:
    siatkowka.dodaj_druzyne(druzyna)

siatkowka.przeglad_druzyn()
print(sedziowie)

siatkowka.utworz_spotkania()

siatkowka.symuluj_wyniki()
siatkowka.zapisz_punkty()

siatkowka.organizuj_polfinaly()

siatkowka.organizuj_final()

print("##############################################################")

siatkowka1 = Dwa_ognie(sedziowie.lista_sedziow)

for druzyna in druzyny:
    siatkowka1.dodaj_druzyne(druzyna)

siatkowka1.przeglad_druzyn()
print(sedziowie)

siatkowka1.utworz_spotkania()

siatkowka1.symuluj_wyniki()
siatkowka1.zapisz_punkty()

siatkowka1.organizuj_polfinaly()

siatkowka1.organizuj_final()