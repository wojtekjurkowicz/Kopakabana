from tkinter import *
from zawodnicy import Druzyna, Sedziowie, Sedzia
from rozgrywki import Siatkowka_plazowa, Dwa_ognie, Przeciaganie_liny
import random

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

def losuj_sedziow(dyscyplina):
    if dyscyplina == "siatkowka_plazowa":
        bg_label.configure(image=bg_siatkowka)
    if dyscyplina == "dwa_ognie":
        bg_label.configure(image=bg_dwa_ognie)
    if dyscyplina == "przeciaganie_liny":
        bg_label.configure(image=bg_przeciaganie_liny)
    siatkowka_przycisk.destroy()
    dwa_ognie_przycisk.destroy()
    przeciaganie_liny_przycisk.destroy()
    plik = open('sedziowie.txt').read()
    plik = plik.split("\n")
    lista_sedziow = []
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
                sedzia_label = Label(glowne_okno, text=sedzia)
                lista.append(str(sedzia))
                lista_labeli.append(sedzia_label)
                sedzia_label.place(x=420, y=d_y)
                d_y += 25

        print(len(lista))
        print(lista)
        print(lista_labeli)

    komunikat = Label(glowne_okno, text="Lista sędziów: ", font=("Arial", 15))
    komunikat.place(x=420, y=50)
    wypisz_sedziow()

    pytanie = Label(glowne_okno, text="Czy chcesz zmodyfikować listę? (max: 10)")
    pytanie.place(x=100, y=450)
    imie_label = Label(glowne_okno, text="Imię: ")
    imie_label.place(x=100, y=475)
    imie_field = Entry(glowne_okno)
    imie_field.place(x=175, y=475)
    nazwisko_label = Label(glowne_okno, text="Nazwisko: ")
    nazwisko_label.place(x=100, y=500)
    nazwisko_field = Entry(glowne_okno)
    nazwisko_field.place(x=175, y=500)

    nie_dla_sedziow = Label(glowne_okno, text="Nie możesz dodać więcej sędziów!")
    def dopisz_sedziego():
        if len(lista) <= 19:
            imie = imie_field.get()
            nazwisko = nazwisko_field.get()
            sedzia = Sedzia(imie, nazwisko)
            sedziowie.dodaj_sedziego(Sedzia(imie, nazwisko))
            print(f"imie: {imie}, nazwisko: {nazwisko}")
            sedzia_label = Label(glowne_okno, text=str(sedzia))
            lista_labeli.append(sedzia_label)
            lista.append(str(sedzia))
            sedzia_label.place(x=420, y=100+((len(lista)-1)*25))
        else:
            pytanie.destroy()
            nie_dla_sedziow.place(x=100, y=450)
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
                print(lista_labeli)
                sedziowie.lista_sedziow.remove(sedzia)
                print(sedziowie.lista_sedziow)
                lista.remove(str(sedzia))
                print(lista)
                lista.clear()
                for sedzia in lista_labeli:
                    sedzia.destroy()
                wypisz_sedziow()
            else:
                nie_ma = Label(glowne_okno, text="Nie ma takiego sędziego na liście!")


    dodaj = Button(glowne_okno, text="Dodaj", height=2, width=12, command=dopisz_sedziego)
    dodaj.place(x=100, y=525)
    usun = Button(glowne_okno, text="Usuń", height=2, width=12, command=usun_sedziego)
    usun.place(x=175, y=525)

    def przejdz_dalej():
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


    dalej = Button(glowne_okno, text="Przejdź dalej", height=5, width=20, command=przejdz_dalej)
    dalej.place(x=525, y=475)

def rozgrywki(sedziowie, dyscyplina):
    if dyscyplina == "siatkowka_plazowa":
        rozgrywki = Siatkowka_plazowa(sedziowie)
    if dyscyplina == "dwa_ognie":
        rozgrywki = Dwa_ognie(sedziowie)
    if dyscyplina == "przeciaganie_liny":
        rozgrywki = Przeciaganie_liny(sedziowie)
    druzyny_label = Label(glowne_okno, text="Ile chcesz drużyn w rozgrywkach(4-8)", font=("Arial", 15))
    druzyny_label.place(x=230, y=100)
    zla_liczba = Label()
    def get_number():
        number = int(entry.get())
        if 4 <= number <= 16:
            dalej(number)
        else:
            druzyny_label.destroy()
            zla_liczba = Label(glowne_okno, text="Podaj liczbę jeszcze raz", font=("Arial", 15))
            zla_liczba.place(x=230, y=100)
            ok = Button(glowne_okno, text="OK", command=get_number)
            ok.place(x=370, y=200)


    entry = Entry(glowne_okno)
    entry.place(x=340, y=150)

    ok = Button(glowne_okno, text="OK", command=get_number, width=5, height=1)
    ok.place(x=380, y=190)

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
        generowanie_label.place(x=230, y=200)

        def wypisywanie_wynikow():
            dalej_przycisk.destroy()
            rozgrywki.utworz_spotkania()
            d_y = 50
            labels = []
            mecze_label = Label(glowne_okno,
                               text=f"Mecze: ")
            mecze_label.place(x=30, y=25)
            labels.append(mecze_label)
            for mecz in rozgrywki.mecze:
                if dyscyplina == "siatkowka_plazowa":
                    mecz_label = Label(glowne_okno, text=f"{mecz['druzyna1']} vs {mecz['druzyna2']}, "
                                                         f"sędzia: {mecz['sedzia']}, pomocniczy: {mecz['sedzia_pom1']}, {mecz['sedzia_pom2']}")
                    mecz_label.place(x=30, y=d_y)
                    labels.append(mecz_label)
                    d_y+=25
                else:
                    mecz_label = Label(glowne_okno, text=f"{mecz['druzyna1']} vs {mecz['druzyna2']}, "
                                                         f"sędzia: {mecz['sedzia']}")
                    mecz_label.place(x=30, y=d_y)
                    labels.append(mecz_label)
                    d_y += 25
            rozgrywki.symuluj_wyniki()
            d_y = 50
            wyniki_label = Label(glowne_okno,
                                text=f"Wyniki: ")
            wyniki_label.place(x=625, y=25)
            labels.append(wyniki_label)
            for wynik in rozgrywki.wyniki:
                wynik_label = Label(glowne_okno,
                                   text=f"Zwyciężyła: {wynik}")
                wynik_label.place(x=625, y=d_y)
                labels.append(wynik_label)
                d_y += 25
            rozgrywki.zapisz_punkty()
            rozgrywki.organizuj_polfinaly()
            rozgrywki.organizuj_final()
            print(rozgrywki.zwyciezca)
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
                przycisk_do_finalu.place(x=500, y=500)

            przycisk_do_polfinalow = Button(text="Dalej",
                                            command=lambda: [do_polfinalow(), przycisk_do_polfinalow.destroy()])
            przycisk_do_polfinalow.place(x=500, y=500)
            def do_finalu():
                for i in range(len(labels)):
                    labels[i].destroy()
                labels.clear()
                final = rozgrywki.final
                zwyciezca = rozgrywki.zwyciezca
                if dyscyplina == "siatkowka_plazowa":
                    final_label = Label(glowne_okno,
                                       text=f"Finał: {final['druzyna1']} vs {final['druzyna2']}, sędzia: {final['sedzia']}, "
                                            f"sędziowie pomocniczy: {mecz['sedzia_pom1']}, {mecz['sedzia_pom2']}")
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
                                            command=lambda: [do_finalu(), przycisk_do_finalu.destroy()])
        dalej_przycisk = Button(text="Dalej", command=lambda: [wypisywanie_wynikow(), generowanie_label.destroy(), dalej_przycisk.destroy()])
        dalej_przycisk.place(x=230, y=250)



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
        if zla_liczba:
            zla_liczba.destroy()
        entry.destroy()
        ok.destroy()
        druzyny_label.destroy()
        pytanie_label = Label(glowne_okno, text="Generowanie / Wpisywanie", font=("Arial", 15), width=30)
        pytanie_label.place(x=230, y=100)
        generowanie_przycisk = Button(glowne_okno, text="Generowanie", font=("Arial", 15), width=20, command=lambda: generuj_druzyny(number, pytanie_label, generowanie_przycisk, wpisywanie_przycisk))
        generowanie_przycisk.place(x=100, y=500)
        wpisywanie_przycisk = Button(glowne_okno, text="Wpisywanie", font=("Arial", 15), width=20, command=lambda: wpisuj_druzyny(number))
        wpisywanie_przycisk.place(x=470, y=500)

        print(number)
        print(len(rozgrywki.druzyny))
        if len(rozgrywki.druzyny) == number:
            pytanie_label.destroy()
            generowanie_przycisk.destroy()
            wpisywanie_przycisk.destroy()





siatkowka_przycisk = Button(glowne_okno, height=3, width=25, text="Siatkówka plażowa", command=lambda: [losuj_sedziow("siatkowka_plazowa")])
siatkowka_przycisk.place(x=100, y=450)

dwa_ognie_przycisk = Button(glowne_okno, height=3, width=25, text="Dwa ognie", command=lambda: [losuj_sedziow("dwa_ognie")])
dwa_ognie_przycisk.place(x=300, y=450)

przeciaganie_liny_przycisk = Button(glowne_okno, height=3, width=25, text="Przeciąganie liny", command=lambda: [losuj_sedziow("przeciaganie_liny")])
przeciaganie_liny_przycisk.place(x=500, y=450)

glowne_okno.mainloop()
