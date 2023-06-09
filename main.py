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
lista_sedziow = sedziowie.lista_sedziow
# Tworzenie drużyn
for i in range(8):
    nazwa_druzyny = f"Drużyna {i+1}"
    druzyna = Druzyna(nazwa_druzyny)
    for j in range(6):
        zawodnik = Zawodnik(f"Zawodnik {j+1}", f"Drużyna {i+1}")
        druzyna.zglos_zawodnika(zawodnik)
    druzyny.append(druzyna)

rozgrywki = Rozgrywki(sedziowie.lista_sedziow)

# Dodawanie drużyn do rozgrywek
for druzyna in druzyny:
    rozgrywki.dodaj_druzyne(druzyna)

# Utworzenie spotkań dla każdej dyscypliny
dyscypliny = ["siatkowka_plazowa", "dwa_ognie", "przeciaganie_liny"]
for dyscyplina in dyscypliny:
    rozgrywki.utworz_spotkania(dyscyplina)

# Symulacja wyników dla każdej drużyny w każdej dyscyplinie
for dyscyplina in dyscypliny:
    for druzyna in druzyny:
        rozgrywki.symuluj_wyniki(druzyna, dyscyplina)

# Organizacja półfinałów dla każdej dyscypliny
for dyscyplina in dyscypliny:
    rozgrywki.organizuj_polfinaly(dyscyplina)

# Organizacja finałów dla każdej dyscypliny
for dyscyplina in dyscypliny:
    rozgrywki.organizuj_finaly(dyscyplina)

# Wyświetlanie wyników
for dyscyplina in dyscypliny:
    print(f"Wyniki {dyscyplina}:")
    for i, mecz in enumerate(rozgrywki.finaly[dyscyplina]):
        print(f"Final {i+1}: {mecz}")
    print("")

rozgrywki = Wyswietl_wyniki(lista_sedziow)
rozgrywki.wyswietl_wyniki("siatkowka_plazowa")
