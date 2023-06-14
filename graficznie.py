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
    def dodawanie_druzyny():
        nazwa_label = Label(glowne_okno, text="Nazwa drużyny: ", font=("Arial", 15))
        nazwa_label.place(x=100, y=300)
        nazwa_field = Entry(glowne_okno)
        nazwa_field.place(x=200, y=325)
        label = Label(glowne_okno, text="Zgłoś zawodnika do drużyny", font=("Arial", 15))
        label.place(x=100, y=300)
        imie_label = Label(glowne_okno, text="Imię: ")
        imie_label.place(x=100, y=325)
        imie_field = Entry(glowne_okno)
        imie_field.place(x=200, y=325)
        nazwisko_label = Label(glowne_okno, text="Nazwisko: ")
        nazwisko_label.place(x=100, y=350)
        nazwisko_field = Entry(glowne_okno)
        nazwisko_field.place(x=200, y=350)
        dodaj = Button(glowne_okno, text="Dodaj", height=2, width=14)
        dodaj.place(x=100, y=350)
        usun = Button(glowne_okno, text="Usuń", height=2, width=14)
        usun.place(x=200, y=350)

        label = Label(glowne_okno, text="Usuń zawodnika z drużyny",
                          font=("Arial", 15))
        label.place(x=230, y=400)

    # if not (komunikat and pytanie and imie_label and imie_field and nazwisko_label and nazwisko_field and dodaj and usun and dalej):
    dodaj = Button(glowne_okno, text="Dodaj drużynę", height=5, width=20, command=dodawanie_druzyny)
    dodaj.place(x=150, y=250)
    generuj = Button(glowne_okno, text="Wygeneruj drużynę", height=5, width=20)
    generuj.place(x=450, y=250)


siatkowka_przycisk = Button(glowne_okno, height=3, width=25, text="Siatkówka plażowa", command=losuj_sedziow)
siatkowka_przycisk.place(x=100, y=450)

dwa_ognie_przycisk = Button(glowne_okno, height=3, width=25, text="Dwa ognie")
dwa_ognie_przycisk.place(x=300, y=450)

przeciaganie_liny_przycisk = Button(glowne_okno, height=3, width=25, text="Przeciąganie liny")
przeciaganie_liny_przycisk.place(x=500, y=450)

glowne_okno.mainloop()
