from tkinter import *
from zawodnicy import Druzyna, Zawodnik, Sedziowie, Sedzia
from rozgrywki import Siatkowka_plazowa, Dwa_ognie, Przeciaganie_liny
import random

glowne_okno = Tk()
glowne_okno.resizable(width=False, height=False)
glowne_okno.title("Rozgrywki na słonecznej plaży Kopakabana")
glowne_okno.iconbitmap("icon.ico")
glowne_okno.geometry("800x600")

frameCnt = 12
frames = [PhotoImage(file='kopakabana.gif', format = 'gif -index %i' % i) for i in range(frameCnt)]


def update(ind):  # tylko i wyłącznie do gifa na poczatku
    frame = frames[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    gif.configure(image=frame)
    glowne_okno.after(100, update, ind)

gif = Label(glowne_okno)
gif.pack()
glowne_okno.after(0, update, 0)


def losuj_sedziow():
    d_y = 150
    gif.destroy()
    bg = PhotoImage(file="kopakabana.png")
    bg_label = Label(glowne_okno, image=bg)
    bg_label.place(x=0, y=0)

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

    print(sedziowie)
    lista = []
    lista_labeli = []
    def wypisz_sedziow():
        d_y = 150
        for sedzia in sedziowie.lista_sedziow:
            sedzia_label = Label(glowne_okno, text=sedzia)
            lista.append(sedzia)
            lista_labeli.append(sedzia_label)
            sedzia_label.place(x=450, y=d_y)
            d_y += 25

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
                lista_labeli[ind].destroy()
                lista_labeli.pop(ind)
                sedziowie.usun_sedziego(sedzia)
                lista.remove(str(sedzia))
                wypisz_sedziow()
                print(lista_labeli)
                print(lista)
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

        return sedziowie

    dalej = Button(glowne_okno, text="Przejdź dalej", height=5, width=20, command=przejdz_dalej)
    dalej.place(x=525, y=475)


def siatkowka_plazowa():
    sedziowie = losuj_sedziow()

    rozgrywki = Siatkowka_plazowa(sedziowie.lista_sedziow)
    druzyny_label = Label(glowne_okno, text="Dodaj, usuń lub wygeneruj drużyny do rozpoczęcia rozgrywek!",
                  font=("Arial", 15))
    druzyny_label.place(x=230, y=100)
    def dodawanie_druzyny():
        nazwa_label = Label(glowne_okno, text="Nazwa drużyny: ",
                      font=("Arial", 15))
        nazwa_label.place(x=100, y=300)
        nazwa_field = Entry(glowne_okno)
        nazwa_field.place(x=200, y=325)
        label = Label(glowne_okno, text="Zgłoś zawodnika do drużyny",
                      font=("Arial", 15))
        label.place(x=100, y=300)
        imie_label = Label(glowne_okno, text="Imię: ")
        imie_label.place(x=100, y=325)
        imie_field = Entry(glowne_okno)
        imie_field.place(x=200, y=325)
        nazwisko_label = Label(glowne_okno, text="Nazwisko: ")
        nazwisko_label.place(x=100, y=350)
        nazwisko_field = Entry(glowne_okno)
        nazwisko_field.place(x=200, y=350)
        dodaj = Button(glowne_okno, text="Dodaj", height=2, width=14,
                       command=(Sedzia(imie_field, nazwisko_field)))
        dodaj.place(x=100, y=350)
        usun = Button(glowne_okno, text="Usuń", height=2, width=14,
                      command=sedziowie.dodaj_sedziego(Sedzia(imie_field, nazwisko_field)))
        usun.place(x=200, y=350)

        label = Label(glowne_okno, text="Usuń zawodnika z drużyny",
                      font=("Arial", 15))
        label.place(x=230, y=400)

    # if not (komunikat and pytanie and imie_label and imie_field and nazwisko_label and nazwisko_field and dodaj and usun and dalej):
    dodaj = Button(glowne_okno, text="Dodaj drużynę", height=5, width=20, command=dodawanie_druzyny)
    dodaj.place(x=150, y=250)
    generuj = Button(glowne_okno, text="Wygeneruj drużynę", height=5, width=20)
    generuj.place(x=450, y=250)

def dwa_ognie():
    sedziowie = losuj_sedziow()

    rozgrywki = Siatkowka_plazowa(sedziowie.lista_sedziow)
    druzyny_label = Label(glowne_okno, text="Dodaj, usuń lub wygeneruj drużyny do rozpoczęcia rozgrywek!",
                  font=("Arial", 15))
    druzyny_label.place(x=230, y=100)
    def dodawanie_druzyny():
        nazwa_label = Label(glowne_okno, text="Nazwa drużyny: ",
                      font=("Arial", 15))
        nazwa_label.place(x=100, y=300)
        nazwa_field = Entry(glowne_okno)
        nazwa_field.place(x=200, y=325)
        label = Label(glowne_okno, text="Zgłoś zawodnika do drużyny",
                      font=("Arial", 15))
        label.place(x=100, y=300)
        imie_label = Label(glowne_okno, text="Imię: ")
        imie_label.place(x=100, y=325)
        imie_field = Entry(glowne_okno)
        imie_field.place(x=200, y=325)
        nazwisko_label = Label(glowne_okno, text="Nazwisko: ")
        nazwisko_label.place(x=100, y=350)
        nazwisko_field = Entry(glowne_okno)
        nazwisko_field.place(x=200, y=350)
        dodaj = Button(glowne_okno, text="Dodaj", height=2, width=14,
                       command=(Sedzia(imie_field, nazwisko_field)))
        dodaj.place(x=100, y=350)
        usun = Button(glowne_okno, text="Usuń", height=2, width=14,
                      command=sedziowie.dodaj_sedziego(Sedzia(imie_field, nazwisko_field)))
        usun.place(x=200, y=350)

        label = Label(glowne_okno, text="Usuń zawodnika z drużyny",
                      font=("Arial", 15))
        label.place(x=230, y=400)

    # if not (komunikat and pytanie and imie_label and imie_field and nazwisko_label and nazwisko_field and dodaj and usun and dalej):
    dodaj = Button(glowne_okno, text="Dodaj drużynę", height=5, width=20, command=dodawanie_druzyny)
    dodaj.place(x=150, y=250)
    generuj = Button(glowne_okno, text="Wygeneruj drużynę", height=5, width=20)
    generuj.place(x=450, y=250)


def przeciaganie_liny():
    sedziowie = losuj_sedziow()

    rozgrywki = Siatkowka_plazowa(sedziowie.lista_sedziow)
    druzyny_label = Label(glowne_okno, text="Dodaj, usuń lub wygeneruj drużyny do rozpoczęcia rozgrywek!",
                  font=("Arial", 15))
    druzyny_label.place(x=230, y=100)
    def dodawanie_druzyny():
        nazwa_label = Label(glowne_okno, text="Nazwa drużyny: ",
                      font=("Arial", 15))
        nazwa_label.place(x=100, y=300)
        nazwa_field = Entry(glowne_okno)
        nazwa_field.place(x=200, y=325)
        label = Label(glowne_okno, text="Zgłoś zawodnika do drużyny",
                      font=("Arial", 15))
        label.place(x=100, y=300)
        imie_label = Label(glowne_okno, text="Imię: ")
        imie_label.place(x=100, y=325)
        imie_field = Entry(glowne_okno)
        imie_field.place(x=200, y=325)
        nazwisko_label = Label(glowne_okno, text="Nazwisko: ")
        nazwisko_label.place(x=100, y=350)
        nazwisko_field = Entry(glowne_okno)
        nazwisko_field.place(x=200, y=350)
        dodaj = Button(glowne_okno, text="Dodaj", height=2, width=14,
                       command=(Sedzia(imie_field, nazwisko_field)))
        dodaj.place(x=100, y=350)
        usun = Button(glowne_okno, text="Usuń", height=2, width=14,
                      command=sedziowie.dodaj_sedziego(Sedzia(imie_field, nazwisko_field)))
        usun.place(x=200, y=350)

        label = Label(glowne_okno, text="Usuń zawodnika z drużyny",
                      font=("Arial", 15))
        label.place(x=230, y=400)

    # if not (komunikat and pytanie and imie_label and imie_field and nazwisko_label and nazwisko_field and dodaj and usun and dalej):
    dodaj = Button(glowne_okno, text="Dodaj drużynę", height=5, width=20, command=dodawanie_druzyny)
    dodaj.place(x=150, y=250)
    generuj = Button(glowne_okno, text="Wygeneruj drużynę", height=5, width=20)
    generuj.place(x=450, y=250)



siatkowka_przycisk = Button(glowne_okno, height=3, width=25, text="Siatkówka plażowa", command=siatkowka_plazowa)
siatkowka_przycisk.place(x=100, y=450)

dwa_ognie_przycisk = Button(glowne_okno, height=3, width=25, text="Dwa ognie", command=dwa_ognie)
dwa_ognie_przycisk.place(x=300, y=450)

przeciaganie_liny_przycisk = Button(glowne_okno, height=3, width=25, text="Przeciąganie liny", command=przeciaganie_liny)
przeciaganie_liny_przycisk.place(x=500, y=450)

glowne_okno.mainloop()

"""
def donothing():
    nowe_okno = Toplevel(glowne_okno)
    label = Label(nowe_okno)
    button = Button(nowe_okno, text="Nacisnij", command=label.pack)
    button.pack()

# nie dziala
def przeglad_sedziow_graficznie():
    nowe_okno = Toplevel(glowne_okno)
    nowe_okno.title("Lista sędziów")
    nowe_okno.geometry("400x250")
    print(sedziowie.lista_sedziow)
    for sedzia in sedziowie.lista_sedziow:
        sedzia_label = Label(nowe_okno, text=f"Imię: {sedzia.get_imie()}, nazwisko: {sedzia.get_nazwisko()}")
        print(sedzia)
        sedzia_label.pack()

def dodaj_sedziego_graficznie():
    nowe_okno = Toplevel(glowne_okno)
    nowe_okno.title("Dodaj sędziego")
    nowe_okno.geometry("400x250")
    nowe_okno.columnconfigure(0, weight=1)
    nowe_okno.columnconfigure(1, weight=1)

    imie_label = Label(nowe_okno, text="Imię: ")
    imie_label.grid(column=0, row=3)
    imie_field = Entry(nowe_okno)
    imie_field.grid(column=1, row=3)

    nazwisko_label = Label(nowe_okno, text="Nazwisko: ")
    nazwisko_label.grid(column=0, row=5)
    nazwisko_field = Entry(nowe_okno)
    nazwisko_field.grid(column=1, row=5)

    imie = imie_field.get()
    nazwisko = nazwisko_field.get()
    sedzia = Sedzia(str(imie), str(nazwisko))
    zatwierdz = Button(nowe_okno, text="Dodaj sędziego", command=lambda: [sedziowie.dodaj_sedziego(sedzia), nowe_okno.destroy()])
    zatwierdz.grid(column=0, row=6)
    print(sedzia)


    anuluj = Button(nowe_okno, text="Anuluj", command=nowe_okno.destroy)
    anuluj.grid(column=1, row=6)

def usun_sedziego_graficznie():
    nowe_okno = Toplevel(glowne_okno)
    nowe_okno.title("Usuń sędziego")
    nowe_okno.geometry("400x250")
    nowe_okno.columnconfigure(0, weight=1)
    nowe_okno.columnconfigure(1, weight=1)

    imie_label = Label(nowe_okno, text="Imię: ")
    imie_label.grid(column=0, row=3)
    imie_field = Entry(nowe_okno)
    imie_field.grid(column=1, row=3)

    nazwisko_label = Label(nowe_okno, text="Nazwisko: ")
    nazwisko_label.grid(column=0, row=5)
    nazwisko_field = Entry(nowe_okno)
    nazwisko_field.grid(column=1, row=5)

    imie = imie_field.get()
    nazwisko = nazwisko_field.get()
    zatwierdz = Button(nowe_okno, text="Usuń sędziego", command=lambda: [sedziowie.usun_sedziego(Sedzia(imie, nazwisko)), nowe_okno.destroy()])
    zatwierdz.grid(column=0, row=6)

    anuluj = Button(nowe_okno, text="Anuluj", command=nowe_okno.destroy)
    anuluj.grid(column=1, row=6)


def dodaj_druzyne():
    nowe_okno = Toplevel(glowne_okno)
    nowe_okno.title("Dodaj drużynę")
    nowe_okno.geometry("400x250")
    nowe_okno.columnconfigure(0, weight=1)
    nowe_okno.columnconfigure(1, weight=1)

    nazwa_label = Label(nowe_okno, text="Nazwa drużyny: ")
    nazwa_label.grid(column=0, row=3)
    nazwa_field = Entry(nowe_okno)
    nazwa_field.grid(column=1, row=3)

    def dodaj_druzyne_przycisk():
        nazwa = nazwa_field.get()
        druzyna = Druzyna(nazwa)
        print(druzyna)
        druzyna_label = Label(nowe_okno, text="Druzyna została dodana")
        druzyna_label.grid(column=0, row=5)

    zatwierdz = Button(nowe_okno, text="Dodaj drużynę", command=dodaj_druzyne_przycisk)
    zatwierdz.grid(column=0, row=6)

    anuluj = Button(nowe_okno, text="Anuluj", command=nowe_okno.destroy)
    anuluj.grid(column=1, row=6)
"""

"""
pasek_menu = Menu(glowne_okno)
menu_rozgrywki = Menu(pasek_menu, tearoff=0)
menu_rozgrywki.add_command(label="Siatkówka plażowa", command=donothing)
menu_rozgrywki.add_command(label="Dwa ognie", command=donothing)
menu_rozgrywki.add_command(label="Przeciąganie liny", command=donothing)
menu_rozgrywki.add_separator()
menu_rozgrywki.add_command(label="Wyjdź z programu", command=glowne_okno.quit)
pasek_menu.add_cascade(label="Rozgrywki", menu=menu_rozgrywki)


menu_sedziowie = Menu(pasek_menu, tearoff=0)
menu_sedziowie.add_command(label="Przegląd sędziów", command=przeglad_sedziow_graficznie)
menu_sedziowie.add_command(label="Dodaj sędziego", command=dodaj_sedziego_graficznie)
menu_sedziowie.add_command(label="Usuń sędziego", command=usun_sedziego_graficznie)
pasek_menu.add_cascade(label="Sędziowie", menu=menu_sedziowie)


menu_druzyny = Menu(pasek_menu, tearoff=0)
menu_druzyny.add_command(label="Dodaj drużynę", command=dodaj_druzyne)
menu_druzyny.add_command(label="Przegląd drużyny", command=donothing)
menu_druzyny.add_command(label="Zgłoś zawodnika", command=donothing)
menu_druzyny.add_command(label="Usuń zawodnika", command=donothing)
pasek_menu.add_cascade(label="Drużyny", menu=menu_druzyny)

glowne_okno.config(menu=pasek_menu)
"""