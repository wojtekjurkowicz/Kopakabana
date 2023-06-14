from tkinter import *
from zawodnicy import Druzyna, Zawodnik, Sedziowie, Sedzia
from rozgrywki import Siatkowka_plazowa, Dwa_ognie, Przeciaganie_liny
import random

glowne_okno = Tk()
glowne_okno.resizable(width=False, height=False)
glowne_okno.title("Rozgrywki na słonecznej plaży Kopakabana")
glowne_okno.iconbitmap("icon.ico")
glowne_okno.geometry("800x600")
bg = PhotoImage(file="kopakabanastart.ppm")
bg1 = PhotoImage(file="kopakabana.ppm")
bg_label1 = Label(glowne_okno, image=bg1)
bg_label1.place(x=0, y=0)
bg_label = Label(glowne_okno, image=bg)
bg_label.place(x=0, y=0)


def losuj_sedziow():
    bg_label.destroy()
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
        d_y = 150
        for sedzia in sedziowie.lista_sedziow:
            if str(sedzia) not in lista:
                sedzia_label = Label(glowne_okno, text=sedzia)
                lista.append(str(sedzia))
                lista_labeli.append(sedzia_label)
                sedzia_label.place(x=450, y=d_y)
                d_y += 25
        print(lista)
        print(lista_labeli)

    komunikat = Label(glowne_okno, text="Lista sędziów: ", font=("Arial", 15))
    komunikat.place(x=450, y=100)
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
            sedzia_label.place(x=600, y=150+(len(lista)-11)*25)
        else:
            pytanie.destroy()
            nie_dla_sedziow.place(x=100, y=450)
            dodaj.destroy()

    def usun_sedziego():
        if len(lista) >= 5:
            imie = imie_field.get()
            nazwisko = nazwisko_field.get()
            sedzia = Sedzia(imie, nazwisko)
            print(f"imie: {imie}, nazwisko: {nazwisko}")
            if str(sedzia) in lista:
                ind = lista.index(str(sedzia))
                print(ind)
                print(lista_labeli[ind])
                lista_labeli[ind].destroy()
                lista_labeli.pop(ind)
                sedziowie.usun_sedziego(sedzia)
                lista.remove(str(sedzia))
                print(lista_labeli)
                print(lista)
                lista.clear()
                lista_labeli.clear()
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

        siatkowka_plazowa(sedziowie.lista_sedziow)


    dalej = Button(glowne_okno, text="Przejdź dalej", height=5, width=20, command=przejdz_dalej)
    dalej.place(x=525, y=475)

def siatkowka_plazowa(sedziowie):
    rozgrywki = Siatkowka_plazowa(sedziowie)
    druzyny_label = Label(glowne_okno, text="Ile chcesz drużyn w rozgrywkach(4-16)", font=("Arial", 15))
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
        generowanie_label.place(x=230, y=100)

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






siatkowka_przycisk = Button(glowne_okno, height=3, width=25, text="Siatkówka plażowa", command=losuj_sedziow)
siatkowka_przycisk.place(x=100, y=450)

dwa_ognie_przycisk = Button(glowne_okno, height=3, width=25, text="Dwa ognie")
dwa_ognie_przycisk.place(x=300, y=450)

przeciaganie_liny_przycisk = Button(glowne_okno, height=3, width=25, text="Przeciąganie liny")
przeciaganie_liny_przycisk.place(x=500, y=450)

glowne_okno.mainloop()
