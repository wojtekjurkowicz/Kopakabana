import pickle
import random
from tkinter import *

from rozgrywki import Siatkowka_plazowa, Dwa_ognie, Przeciaganie_liny
from zawodnicy import Druzyna, Sedziowie, Sedzia, Zawodnik

glowne_okno = Tk()
glowne_okno.resizable(width=False, height=False)
glowne_okno.title("Rozgrywki na słonecznej plaży Kopakabana")
glowne_okno.iconbitmap("icon.ico")
glowne_okno.geometry("1024x768")
bg_start = PhotoImage(file="kopakabanastart.ppm")
bg_label = Label(glowne_okno, image=bg_start)
bg_label.place(x=0, y=0)
bg_siatkowka = PhotoImage(file="siata.ppm")
bg_dwa_ognie = PhotoImage(file="zbijak.ppm")
bg_przeciaganie_liny = PhotoImage(file="lina.ppm")


def wybor(dyscyplina):
    if dyscyplina == "siatkowka_plazowa":
        bg_label.configure(image=bg_siatkowka)
    if dyscyplina == "dwa_ognie":
        bg_label.configure(image=bg_dwa_ognie)
    if dyscyplina == "przeciaganie_liny":
        bg_label.configure(image=bg_przeciaganie_liny)

    siatkowka_przycisk.destroy()
    dwa_ognie_przycisk.destroy()
    przeciaganie_liny_przycisk.destroy()

    wybor_label = Label(glowne_okno, height=3,  width=35, text="Czy chcesz wczytać dane z pliku?", font=("Arial", 15))
    wybor_label.place(x=290, y=300)
    wczytaj_przycisk = Button(glowne_okno, text="Wczytaj dane poprzednich rozgrywek!", font=("Arial", 15),
                              command=lambda: [wczytywanie_z_pliku(dyscyplina), wybor_label.destroy(),
                                               wczytaj_przycisk.destroy(), wpisz_przycisk.destroy()])
    wczytaj_przycisk.place(x=310, y=390)
    wpisz_przycisk = Button(glowne_okno, text="Wpisz/wygeneruj nowe dane", font=("Arial", 15), command=lambda: [losuj_sedziow(dyscyplina), wybor_label.destroy(), wczytaj_przycisk.destroy(), wpisz_przycisk.destroy()])
    wpisz_przycisk.place(x=350, y=440)


def wczytywanie_z_pliku(dyscyplina):
    if dyscyplina == "siatkowka_plazowa":
        plik = "siatkowka.pickle"
    if dyscyplina == "dwa_ognie":
        plik = "dwa_ognie.pickle"
    if dyscyplina == "przeciaganie_liny":
        plik = "przeciaganie_liny.pickle"

    with open(plik, 'rb') as p:
        dane = pickle.load(p)
        druzyny = dane["druzyny"]
        lista_sedziow = dane["lista_sedziow"]
        mecze = dane["mecze"]
        wyniki = dane["wyniki"]
        polfinalisci = dane["polfinalisci"]
        polfinaly = dane["polfinaly"]
        final = dane["final"]
        zwyciezca = dane["zwyciezca"]

    print(final)


    sedziowie = Sedziowie()
    for sedzia in lista_sedziow:
        sedziowie.dodaj_sedziego(sedzia)

    if dyscyplina == "siatkowka_plazowa":
        rozgrywki = Siatkowka_plazowa(sedziowie.lista_sedziow)
    if dyscyplina == "dwa_ognie":
        rozgrywki = Dwa_ognie(sedziowie.lista_sedziow)
    if dyscyplina == "przeciaganie_liny":
        rozgrywki = Przeciaganie_liny(sedziowie.lista_sedziow)
    for druzyna in druzyny:
        rozgrywki.dodaj_druzyne(druzyna)

    lista_labeli = []

    def wypisz_sedziow():
        d_y = 100
        for sedzia in sedziowie.lista_sedziow:
            sedzia_label = Label(glowne_okno, text=sedzia, font=("Arial", 12))
            lista_labeli.append(sedzia_label)
            sedzia_label.place(x=50, y=d_y)
            d_y += 25

    komunikat = Label(glowne_okno, text="Lista sędziów: ", font=("Arial", 15))
    komunikat.place(x=50, y=50)
    lista_labeli.append(komunikat)
    wypisz_sedziow()

    def wypisz_druzyny():
        d_y = 100
        for druzyna in druzyny:
            druzyna_label = Label(glowne_okno, text=druzyna.nazwa, font=("Arial", 12))
            lista_labeli.append(druzyna_label)
            druzyna_label.place(x=250, y=d_y)
            d_y += 25

    komunikat1 = Label(glowne_okno, text="Lista drużyn: ", font=("Arial", 15))
    komunikat1.place(x=250, y=50)
    lista_labeli.append(komunikat1)
    wypisz_druzyny()

    def do_polfinalow():
        print(polfinaly)
        for i in range(len(lista_labeli)):
            lista_labeli[i].destroy()
        lista_labeli.clear()

        d_y = 50
        polfinaly_label = Label(glowne_okno,
                                   text=f"Półfinaliści: ")
        polfinaly_label.place(x=50, y=25)
        lista_labeli.append(polfinaly_label)
        if dyscyplina == "siatkowka_plazowa":
            polfinalisci.sort(key=lambda druzyna: druzyna.punkty_siatkowka, reverse=True)
            for polfinalista in polfinalisci:
                polfinalista_label = Label(glowne_okno,
                                           text=f"{polfinalista.nazwa}, liczba zdobytych punktów: {polfinalista.punkty_siatkowka}")
                polfinalista_label.place(x=50, y=d_y)
                lista_labeli.append(polfinalista_label)
                d_y += 25
            d_y = 250
            for polfinal in polfinaly:
                polfinal_label = Label(glowne_okno,
                                       text=f"Mecz {polfinal['druzyna1']} vs {polfinal['druzyna2']}, "
                                            f"sędzia: {polfinal['sedzia']}, sędziowie pomocniczy: {polfinal['sedzia_pom1']}, {polfinal['sedzia_pom2']}")
                polfinal_label.place(x=25, y=d_y)
                lista_labeli.append(polfinal_label)
                d_y += 25
        elif dyscyplina == "dwa_ognie":
            polfinalisci.sort(key=lambda druzyna: druzyna.punkty_dwa_ognie, reverse=True)
            for polfinalista in polfinalisci:
                polfinalista_label = Label(glowne_okno,
                                           text=f"{polfinalista.nazwa}, liczba zdobytych punktów: {polfinalista.punkty_dwa_ognie}")
                polfinalista_label.place(x=50, y=d_y)
                lista_labeli.append(polfinalista_label)
                d_y += 25
            d_y = 250
            for polfinal in polfinaly:
                polfinal = dict(polfinal)
                polfinal_label = Label(glowne_okno,
                                        text=f"Mecz {polfinal['druzyna1']} vs {polfinal['druzyna2']}, "
                                            f"sędzia: {polfinal['sedzia']}")
                polfinal_label.place(x=25, y=d_y)
                lista_labeli.append(polfinal_label)
                d_y += 25
        elif dyscyplina == "przeciaganie_liny":
            polfinalisci.sort(key=lambda druzyna: druzyna.punkty_przeciaganie_liny, reverse=True)
            for polfinalista in polfinalisci:
                polfinalista_label = Label(glowne_okno,
                                   text=f"{polfinalista.nazwa}, liczba zdobytych punktów: {polfinalista.punkty_przeciaganie_liny}")
                polfinalista_label.place(x=50, y=d_y)
                lista_labeli.append(polfinalista_label)
                d_y += 25
            d_y = 250
            for polfinal in polfinaly:
                polfinal_label = Label(glowne_okno, text=f"Mecz {polfinal['druzyna1']} vs {polfinal['druzyna2']}, "
                                                 f"sędzia: {polfinal['sedzia']}")
                polfinal_label.place(x=25, y=d_y)
                lista_labeli.append(polfinal_label)
                d_y += 25

        przycisk_do_finalu.place(x=875, y=680)

    def przejdz_do_meczow():
        for label in lista_labeli:
            label.destroy()
        d_y = 50
        lista_labeli.clear()
        mecze_label = Label(glowne_okno,
                            text=f"Mecze: ", font=("Arial", 15))
        mecze_label.place(x=30, y=20)
        lista_labeli.append(mecze_label)
        for mecz in mecze:
            if dyscyplina == "siatkowka_plazowa":
                mecz_label = Label(glowne_okno, font=("Arial", 10), text=f"{mecz['druzyna1']} vs {mecz['druzyna2']}, "
                                                                         f"sędzia: {mecz['sedzia']}, pomocniczy: {mecz['sedzia_pom1']}, {mecz['sedzia_pom2']}")
                mecz_label.place(x=30, y=d_y)
                lista_labeli.append(mecz_label)
                d_y += 25
            else:
                mecz_label = Label(glowne_okno, font=("Arial", 10), text=f"{mecz['druzyna1']} vs {mecz['druzyna2']}, "
                                                                         f"sędzia: {mecz['sedzia']}")
                mecz_label.place(x=30, y=d_y)
                lista_labeli.append(mecz_label)
                d_y += 25
        for wynik in wyniki:
            wynik_label = Label(glowne_okno, font=("Arial", 10),
                                text=f"Zwyciężyła: {wynik}")
            wynik_label.place(x=730, y=d_y)
            lista_labeli.append(wynik_label)
            d_y += 25

    przycisk_do_polfinalow = Button(text="Dalej", command=lambda: [do_polfinalow(), przycisk_do_polfinalow.destroy()], height=2, width=10, font=("Arial", 15))
    przycisk_do_polfinalow.place(x=875, y=680)

    def do_finalu():
        for i in range(len(lista_labeli)):
            lista_labeli[i].destroy()
        lista_labeli.clear()
        final = rozgrywki.final
        zwyciezca = rozgrywki.zwyciezca
        if dyscyplina == "siatkowka_plazowa":
            final_label = Label(glowne_okno,
                                text=f"Finał: {final['druzyna1']} vs {final['druzyna2']}, sędzia: {final['sedzia']}, "
                                    f"sędziowie pomocniczy: {final['sedzia_pom1']}, {final['sedzia_pom2']}")
            final_label.place(x=100, y=260)
            zwyciezca_label = Label(glowne_okno, text=f"ZWYCIĘŻA: {zwyciezca}!!!", font=("Arial", 30))
            zwyciezca_label.place(x=180, y=360)
            lista_labeli.append(final_label)
        elif dyscyplina == "dwa_ognie":
            final_label = Label(glowne_okno,
                               text=f"Finał: {final['druzyna1']} vs {final['druzyna2']}, sędzia: {final['sedzia']}")
            final_label.place(x=100, y=260)
            zwyciezca_label = Label(glowne_okno, text=f"ZWYCIĘŻA: {zwyciezca}!!!", font=("Arial", 30))
            zwyciezca_label.place(x=180, y=360)
            lista_labeli.append(final_label)
        elif dyscyplina == "przeciaganie_liny":
            final_label = Label(glowne_okno,
                               text=f"Finał: {final['druzyna1']} vs {final['druzyna2']}, sędzia: {final['sedzia']}")
            final_label.place(x=100, y=260)
            zwyciezca_label = Label(glowne_okno, text=f"ZWYCIĘŻA: {zwyciezca}!!!", font=("Arial", 30))
            zwyciezca_label.place(x=180, y=360)
            lista_labeli.append(final_label)


    przycisk_do_finalu = Button(text="Dalej", command=lambda: [do_finalu(), przycisk_do_finalu.destroy()], height=2, width=10, font=("Arial", 15))


    przejdz_do_meczow_button = Button(glowne_okno, text="Dalej", height=2, width=10, command=lambda: [przejdz_do_meczow(), przejdz_do_meczow_button.destroy()], font=("Arial", 15))
    przejdz_do_meczow_button.place(x=850, y=680)

def losuj_sedziow(dyscyplina):
    plik = open('sedziowie.txt').read()
    plik = plik.split("\n")
    lista_sedziow = []
    smietnik = []
    for i in plik:
        lista_sedziow.append(i)

    sedziowie = Sedziowie()
    for i in range(10):
        sedzia = random.choice(lista_sedziow)
        sedziowie.dodaj_sedziego(sedzia)
        lista_sedziow.remove(sedzia)

    lista = []
    lista_labeli = []
    def wypisz_sedziow():
        d_y = 100
        for sedzia in sedziowie.lista_sedziow:
            if str(sedzia) not in lista:
                sedzia_label = Label(glowne_okno, text=sedzia, font=("Arial", 12))
                lista.append(str(sedzia))
                lista_labeli.append(sedzia_label)
                sedzia_label.place(x=50, y=d_y)
                d_y += 25

    komunikat = Label(glowne_okno, text="Lista sędziów: ", font=("Arial", 15))
    komunikat.place(x=50, y=50)
    wypisz_sedziow()

    pytanie = Label(glowne_okno, text="Czy chcesz zmodyfikować listę? (max: 10)", font=("Arial", 15))
    pytanie.place(x=430, y=550)
    imie_label = Label(glowne_okno, text="Imię: ", font=("Arial", 12))
    imie_label.place(x=450, y=600)
    imie_field = Entry(glowne_okno, font=("Arial", 12))
    imie_field.place(x=550, y=600)
    nazwisko_label = Label(glowne_okno, text="Nazwisko: ", font=("Arial", 12))
    nazwisko_label.place(x=450, y=650)
    nazwisko_field = Entry(glowne_okno, font=("Arial", 12))
    nazwisko_field.place(x=550, y=650)

    nie_dla_sedziow = Label(glowne_okno, text="Nie możesz dodać więcej sędziów!", font=("Arial", 15))
    def dopisz_sedziego():
        print(len(lista))
        if len(lista) <= 19:
            imie = imie_field.get()
            nazwisko = nazwisko_field.get()
            sedzia = Sedzia(imie, nazwisko)
            sedziowie.dodaj_sedziego(str(Sedzia(imie, nazwisko)))
            print(f"imie: {imie}, nazwisko: {nazwisko}")
            sedzia_label = Label(glowne_okno, text=str(sedzia), font=("Arial", 12))
            lista_labeli.append(sedzia_label)
            lista.append(str(sedzia))
            sedzia_label.place(x=50, y=350+((len(lista)-11)*25))
        else:
            pytanie.destroy()
            nie_dla_sedziow.place(x=450, y=550)
            dodaj.destroy()

    def usun_sedziego():
        if len(lista) >= 5:
            imie = imie_field.get()
            nazwisko = nazwisko_field.get()
            sedzia = Sedzia(imie, nazwisko)
            print(f"imie: {sedzia.get_imie()}, nazwisko: {sedzia.get_nazwisko()}")
            if str(sedzia) in lista:
                ind = lista.index(str(sedzia))
                print(ind)
                print(lista_labeli[ind])
                lista_labeli[ind].destroy()
                lista_labeli.remove(lista_labeli[ind])
                print("labele ",lista_labeli)
                sedziowie.usun_sedziego(str(sedzia))
                lista.remove(str(sedzia))
                print("lista ",lista)
                lista.clear()
                pytanie1 = Label(glowne_okno, text="Czy chcesz zmodyfikować listę? (max: 10)", font=("Arial", 15))
                pytanie1.place(x=430, y=550)
                smietnik.append(pytanie1)
                dodaj1 = Button(glowne_okno, text="Dodaj", height=2, width=14, command=dopisz_sedziego,
                               font=("Arial", 12))
                dodaj1.place(x=450, y=700)
                smietnik.append(dodaj1)
                for sedzia in lista_labeli:
                    sedzia.destroy()
                wypisz_sedziow()

    dodaj = Button(glowne_okno, text="Dodaj", height=2, width=14, command=dopisz_sedziego, font=("Arial", 12))
    dodaj.place(x=450, y=700)
    usun = Button(glowne_okno, text="Usuń", height=2, width=14, command=usun_sedziego, font=("Arial", 12))
    usun.place(x=600, y=700)

    def przejdz_dalej():
        for trash in smietnik:
            trash.destroy()
        nie_dla_sedziow.destroy()
        komunikat.destroy()
        pytanie.destroy()
        imie_label.destroy()
        imie_field.destroy()
        nazwisko_label.destroy()
        nazwisko_field.destroy()
        dodaj.destroy()
        usun.destroy()
        dalej.destroy()
        for sedzia in lista_labeli:
            sedzia.destroy()
        if dyscyplina == "siatkowka_plazowa":
            rozgrywki(sedziowie.lista_sedziow, dyscyplina)
        if dyscyplina == "dwa_ognie":
            rozgrywki(sedziowie.lista_sedziow, dyscyplina)
        if dyscyplina == "przeciaganie_liny":
            rozgrywki(sedziowie.lista_sedziow, dyscyplina)


    dalej = Button(glowne_okno, text="Dalej", height=2, width=10, command=przejdz_dalej, font=("Arial", 15))
    dalej.place(x=850, y=680)


def rozgrywki(sedziowie, dyscyplina):
    if dyscyplina == "siatkowka_plazowa":
        rozgrywki = Siatkowka_plazowa(sedziowie)
    if dyscyplina == "dwa_ognie":
        rozgrywki = Dwa_ognie(sedziowie)
    if dyscyplina == "przeciaganie_liny":
        rozgrywki = Przeciaganie_liny(sedziowie)
    druzyny_label = Label(glowne_okno, text="Ile chcesz drużyn w rozgrywkach(4-8)", font=("Arial", 15))
    druzyny_label.place(x=340, y=250)
    def get_number():
        number = int(entry.get())
        if 4 <= number <= 8:
            dalej(number)
            ok.destroy()
            druzyny_label.destroy()
        else:
            druzyny_label.configure(text="Podaj liczbę jeszcze raz")
            druzyny_label.place(x=390, y=250)
            ok.configure(text="OK", command=get_number, width=10, height=2)
            ok.place(x=470, y=350)


    entry = Entry(glowne_okno, font=("Arial", 15), width=20)
    entry.place(x=390, y=300)

    ok = Button(glowne_okno, text="OK", command=get_number, width=10, height=2)
    ok.place(x=470, y=350)

    def inne_wpisuj_druzyny(liczba_druzyn, pytanie_label, generowanie_przycisk, wpisywanie_przycisk):    # numero 1
        pytanie_label.destroy()
        generowanie_przycisk.destroy()
        wpisywanie_przycisk.destroy()
        napotem_label = []
        lista_druzyn = [] # DO ZROBIENIA JESZCZE ALE NA LUZIE MYŚLĘ
        powpisuj_druzyny(0, liczba_druzyn, napotem_label)

    def przycisk(imie, nazwisko, druzyna, numerzawodnika, napotem_label, numerdruzyny, liczba_druzyn):
        jakieimie = imie.get()
        jakienazwisko = nazwisko.get()
        zawodnik_label = Label(glowne_okno, text=f"{jakieimie} {jakienazwisko}", font=("Arial", 10))
        zawodnik_label.place(x=20, y=70 + 30 * numerzawodnika)
        napotem_label.append(zawodnik_label)
        jakizawodnik = Zawodnik(jakieimie, jakienazwisko)
        druzyna.zglos_zawodnika(jakizawodnik)
        dodajdruzyne(numerzawodnika + 1, napotem_label, druzyna, numerdruzyny, liczba_druzyn)

    def dodajdruzyne(numerzawodnika, napotem_label, druzyna, numerdruzyny, liczba_druzyn):             # numero 5
        if numerzawodnika <= 5:
            ktoryto = Label(glowne_okno, text=f"Zawodnik Nr.{numerzawodnika + 1}", font=("Arial", 18))
            ktoryto.place(x=480, y=50)
            napotem_label.append(ktoryto)
            imie_label = Label(glowne_okno, text=f"Podaj imię", font=("Arial", 15))
            imie_label.place(x=415, y=100)
            imie = Entry(glowne_okno, width=20)
            imie.place(x=400, y=140)
            nazwisko_label = Label(glowne_okno, text=f"Podaj nazwisko", font=("Arial", 15))
            nazwisko_label.place(x=575, y=100)
            nazwisko = Entry(glowne_okno, width=20)
            nazwisko.place(x=582, y=140)
            napotem_label.append(imie_label)
            napotem_label.append(imie)
            napotem_label.append(nazwisko_label)
            napotem_label.append(nazwisko)
            przyciskzawodnik = Button(glowne_okno, text="Zatwierdź zawodnika"
                                    , command=lambda: przycisk(imie, nazwisko, druzyna, numerzawodnika, napotem_label,
                                                               numerdruzyny, liczba_druzyn))
            przyciskzawodnik.place(x=450, y=180)
            napotem_label.append(przyciskzawodnik)
        else:
            powpisuj_druzyny(numerdruzyny + 1, liczba_druzyn, napotem_label)

    def dodajzawodnikow(liczba_druzyn, napotem_label, jakanazwa, numerdruzyny):        # numero 4
        for k in napotem_label:
            k.destroy()
        druzyna = Druzyna(jakanazwa)
        nazwadruzyny = Label(glowne_okno, text=f"Nazwa drużyny : {jakanazwa}", font=("Arial", 12))
        nazwadruzyny.place(x=20, y=20)
        podnazwa_label = Label(glowne_okno, text="Lista zawodników :", font=("Arial", 10))
        podnazwa_label.place(x=20, y=45)
        napotem_label.append(podnazwa_label)
        napotem_label.append(nazwadruzyny)

        if numerdruzyny <= liczba_druzyn:
            dodajdruzyne(0, napotem_label, druzyna, numerdruzyny, liczba_druzyn)

    def dodajnazwedruzyny(liczba_druzyn, napotem_label, nazwa, numerdruzyny):        # numero 3
        jakanazwa = nazwa.get()
        print(jakanazwa)
        dodajzawodnikow(liczba_druzyn, napotem_label, jakanazwa, numerdruzyny)

    def powpisuj_druzyny(numerdruzyny, liczba_druzyn, napotem_label):        # numero 2
        if numerdruzyny < liczba_druzyn:
            for k in napotem_label:
                k.destroy()
            nazwa = Entry(glowne_okno, width=60)
            nazwa.place(x=220, y=300)
            napotem_label.append(nazwa)
            nazwa_label = Label(glowne_okno, text=f"Podaj nazwę drużyny Nr.{numerdruzyny + 1}:", font=("Arial", 25))
            nazwa_label.place(x=210, y=250)
            napotem_label.append(nazwa_label)
            przyciskdruzyna = Button(glowne_okno, text="Zatwierdź nazwę drużyny"
                                    , command=lambda: dodajnazwedruzyny(liczba_druzyn, napotem_label, nazwa, numerdruzyny))
            przyciskdruzyna.place(x=325, y=360)
            napotem_label.append(przyciskdruzyna)
        else:
            for w in napotem_label:
                w.destroy()
            noisuper = Label(glowne_okno, text="Zawodnicy zostali zapisani :)", font=("Arial", 30))
            noisuper.place(x=40, y=500)
            napotem_label.append(noisuper)
    def generuj_druzyny(liczba_druzyn, pytanie_label, generowanie_przycisk, wpisywanie_przycisk):
        plik = open('ludzie.txt').read()
        plik = plik.split("\n")
        lista_zawodnikow = []
        for i in plik:
            lista_zawodnikow.append(i)

        druzyny = []
        for i in range(liczba_druzyn):
            nazwa_druzyny = f"Drużyna {i + 1}"
            druzyna = Druzyna(nazwa_druzyny)
            for j in range(6):
                zawodnik = random.choice(lista_zawodnikow)
                lista_zawodnikow.remove(zawodnik)
                druzyna.zglos_zawodnika(zawodnik)
            druzyny.append(druzyna)
            print(druzyna)
            rozgrywki.dodaj_druzyne(druzyna)

        pytanie_label.destroy()
        generowanie_przycisk.destroy()
        wpisywanie_przycisk.destroy()
        generowanie_label = Label(glowne_okno, text="Pomyślnie wygenerowano", font=("Arial", 15), width=30)
        generowanie_label.place(x=125, y=400)

        def wypisywanie_wynikow():
            dalej_przycisk.destroy()
            rozgrywki.utworz_spotkania()
            d_y = 50
            labels = []
            mecze_label = Label(glowne_okno,
                               text=f"Mecze: ", font=("Arial", 15))
            mecze_label.place(x=30, y=20)
            labels.append(mecze_label)
            for mecz in rozgrywki.mecze:
                if dyscyplina == "siatkowka_plazowa":
                    mecz_label = Label(glowne_okno, font=("Arial", 10), text=f"{mecz['druzyna1']} vs {mecz['druzyna2']}, "
                                                         f"sędzia: {mecz['sedzia']}, pomocniczy: {mecz['sedzia_pom1']}, {mecz['sedzia_pom2']}")
                    mecz_label.place(x=30, y=d_y)
                    labels.append(mecz_label)
                    d_y+=25
                else:
                    mecz_label = Label(glowne_okno, font=("Arial", 10), text=f"{mecz['druzyna1']} vs {mecz['druzyna2']}, "
                                                         f"sędzia: {mecz['sedzia']}")
                    mecz_label.place(x=30, y=d_y)
                    labels.append(mecz_label)
                    d_y += 25
            rozgrywki.symuluj_wyniki()
            d_y = 50
            wyniki_label = Label(glowne_okno, font=("Arial", 15),
                                text=f"Wyniki: ")
            wyniki_label.place(x=730, y=20)
            labels.append(wyniki_label)
            for wynik in rozgrywki.wyniki:
                wynik_label = Label(glowne_okno, font=("Arial", 10),
                                   text=f"Zwyciężyła: {wynik}")
                wynik_label.place(x=730, y=d_y)
                labels.append(wynik_label)
                d_y += 25
            rozgrywki.zapisz_punkty()
            rozgrywki.organizuj_polfinaly()
            rozgrywki.organizuj_final()
            print(rozgrywki.zwyciezca)
            status = {
                "druzyny": rozgrywki.druzyny,
                "lista_sedziow": rozgrywki.lista_sedziow,
                "mecze": rozgrywki.mecze,
                "wyniki": rozgrywki.wyniki,
                "polfinalisci": rozgrywki.polfinalisci,
                "polfinaly": rozgrywki.polfinaly,
                "final": rozgrywki.final,
                "zwyciezca": rozgrywki.zwyciezca
            }
            if dyscyplina == "siatkowka_plazowa":
                plik = "siatkowka.pickle"
            if dyscyplina == "dwa_ognie":
                plik = "dwa_ognie.pickle"
            if dyscyplina == "przeciaganie_liny":
                plik = "przeciaganie_liny.pickle"

            with open(plik, "wb") as p:
                pickle.dump(status, p)

            def do_polfinalow():
                for i in range(len(labels)):
                    labels[i].destroy()
                labels.clear()

                d_y = 50
                polfinaly_label = Label(glowne_okno,
                                       text=f"Półfinaliści: ")
                polfinaly_label.place(x=50, y=25)
                labels.append(polfinaly_label)
                if dyscyplina == "siatkowka_plazowa":
                    rozgrywki.polfinalisci.sort(key=lambda druzyna: druzyna.punkty_siatkowka, reverse=True)
                    for polfinalista in rozgrywki.polfinalisci:
                        polfinalista_label = Label(glowne_okno,
                                                   text=f"{polfinalista.nazwa}, liczba zdobytych punktów: {polfinalista.punkty_siatkowka}")
                        polfinalista_label.place(x=50, y=d_y)
                        labels.append(polfinalista_label)
                        d_y += 25
                    d_y = 250
                    for polfinal in rozgrywki.polfinaly:
                        polfinal_label = Label(glowne_okno,
                                               text=f"Mecz {polfinal['druzyna1']} vs {polfinal['druzyna2']}, "
                                                    f"sędzia: {polfinal['sedzia']}, sędziowie pomocniczy: {polfinal['sedzia_pom1']}, {polfinal['sedzia_pom2']}")
                        polfinal_label.place(x=25, y=d_y)
                        labels.append(polfinal_label)
                        d_y += 25
                elif dyscyplina == "dwa_ognie":
                    rozgrywki.polfinalisci.sort(key=lambda druzyna: druzyna.punkty_dwa_ognie, reverse=True)
                    for polfinalista in rozgrywki.polfinalisci:
                        polfinalista_label = Label(glowne_okno,
                                                   text=f"{polfinalista.nazwa}, liczba zdobytych punktów: {polfinalista.punkty_dwa_ognie}")
                        polfinalista_label.place(x=50, y=d_y)
                        labels.append(polfinalista_label)
                        d_y += 25
                    d_y = 250
                    for polfinal in rozgrywki.polfinaly:
                        polfinal_label = Label(glowne_okno,
                                               text=f"Mecz {polfinal['druzyna1']} vs {polfinal['druzyna2']}, "
                                                    f"sędzia: {polfinal['sedzia']}")
                        polfinal_label.place(x=25, y=d_y)
                        labels.append(polfinal_label)
                        d_y += 25
                elif dyscyplina == "przeciaganie_liny":
                    rozgrywki.polfinalisci.sort(key=lambda druzyna: druzyna.punkty_przeciaganie_liny, reverse=True)
                    for polfinalista in rozgrywki.polfinalisci:
                        polfinalista_label = Label(glowne_okno,
                                           text=f"{polfinalista.nazwa}, liczba zdobytych punktów: {polfinalista.punkty_przeciaganie_liny}")
                        polfinalista_label.place(x=50, y=d_y)
                        labels.append(polfinalista_label)
                        d_y += 25
                    d_y = 250
                    for polfinal in rozgrywki.polfinaly:
                        polfinal_label = Label(glowne_okno, text=f"Mecz {polfinal['druzyna1']} vs {polfinal['druzyna2']}, "
                                                         f"sędzia: {polfinal['sedzia']}")
                        polfinal_label.place(x=25, y=d_y)
                        labels.append(polfinal_label)
                        d_y += 25
                przycisk_do_finalu.place(x=875, y=680)

            przycisk_do_polfinalow = Button(text="Dalej", command=lambda: [do_polfinalow(), przycisk_do_polfinalow.destroy()], height=2, width=10, font=("Arial", 15))
            przycisk_do_polfinalow.place(x=875, y=680)

            def do_finalu():
                for i in range(len(labels)):
                    labels[i].destroy()
                labels.clear()
                final = rozgrywki.final
                zwyciezca = rozgrywki.zwyciezca
                if dyscyplina == "siatkowka_plazowa":
                    final_label = Label(glowne_okno,
                                       text=f"Finał: {final['druzyna1']} vs {final['druzyna2']}, sędzia: {final['sedzia']}, "
                                            f"sędziowie pomocniczy: {final['sedzia_pom1']}, {final['sedzia_pom2']}")
                    final_label.place(x=100, y=260)
                    zwyciezca_label = Label(glowne_okno, text=f"ZWYCIĘŻA: {zwyciezca}!!!", font=("Arial", 30))
                    zwyciezca_label.place(x=180, y=360)
                    labels.append(mecz_label)
                elif dyscyplina == "dwa_ognie":
                    final_label = Label(glowne_okno,
                                       text=f"Finał: {final['druzyna1']} vs {final['druzyna2']}, sędzia: {final['sedzia']}")
                    final_label.place(x=100, y=260)
                    zwyciezca_label = Label(glowne_okno, text=f"ZWYCIĘŻA: {zwyciezca}!!!", font=("Arial", 30))
                    zwyciezca_label.place(x=180, y=360)
                    labels.append(mecz_label)
                elif dyscyplina == "przeciaganie_liny":
                    final_label = Label(glowne_okno,
                                       text=f"Finał: {final['druzyna1']} vs {final['druzyna2']}, sędzia: {final['sedzia']}")
                    final_label.place(x=100, y=260)
                    zwyciezca_label = Label(glowne_okno, text=f"ZWYCIĘŻA: {zwyciezca}!!!", font=("Arial", 30))
                    zwyciezca_label.place(x=180, y=360)
                    labels.append(mecz_label)


            przycisk_do_finalu = Button(text="Dalej",
                                            command=lambda: [do_finalu(), przycisk_do_finalu.destroy()], height=2, width=10, font=("Arial", 15))

        dalej_przycisk = Button(text="Dalej", font=("Arial", 15), width=14, command=lambda: [wypisywanie_wynikow(), generowanie_label.destroy(), dalej_przycisk.destroy()])
        dalej_przycisk.place(x=210, y=450)



    def wpisuj_druzyny(liczba_druzyn):
        lista_zawodnikow = []
        druzyny = []
        for i in range(liczba_druzyn):
            nazwa_druzyny = f"Drużyna {i + 1}"
            druzyna = Druzyna(nazwa_druzyny)
            for j in range(6):
                zawodnik = random.choice(lista_zawodnikow)
                lista_zawodnikow.remove(zawodnik)
                druzyna.zglos_zawodnika(zawodnik)
            druzyny.append(druzyna)
            print(druzyna)
            rozgrywki.dodaj_druzyne(druzyna)


    def dalej(number):
        entry.destroy()
        ok.destroy()
        druzyny_label.destroy()
        pytanie_label = Label(glowne_okno, text="Jakie chcesz drużyny?", font=("Arial", 15), width=30)
        pytanie_label.place(x=125, y=400)
        generowanie_przycisk = Button(glowne_okno, text="Generowane", font=("Arial", 15), width=14, command=lambda: generuj_druzyny(number, pytanie_label, generowanie_przycisk, wpisywanie_przycisk))
        generowanie_przycisk.place(x=125, y=500)
        wpisywanie_przycisk = Button(glowne_okno, text="Wpisywane", font=("Arial", 15), width=14, command=lambda: inne_wpisuj_druzyny(number, pytanie_label, generowanie_przycisk, wpisywanie_przycisk))
        wpisywanie_przycisk.place(x=300, y=500)

        print(number)
        print(len(rozgrywki.druzyny))
        if len(rozgrywki.druzyny) == number:
            pytanie_label.destroy()
            generowanie_przycisk.destroy()
            wpisywanie_przycisk.destroy()





siatkowka_przycisk = Button(glowne_okno, height=4, width=30, text="Siatkówka plażowa", font=("Arial", 15), command=lambda: [wybor("siatkowka_plazowa")])
siatkowka_przycisk.place(x=0, y=625)

dwa_ognie_przycisk = Button(glowne_okno, height=4, width=31, text="Dwa ognie", font=("Arial", 15), command=lambda: [wybor("dwa_ognie")])
dwa_ognie_przycisk.place(x=336, y=625)

przeciaganie_liny_przycisk = Button(glowne_okno, height=4, width=30, text="Przeciąganie liny",  font=("Arial", 15), command=lambda: [wybor("przeciaganie_liny")])
przeciaganie_liny_przycisk.place(x=685, y=625)

glowne_okno.mainloop()
