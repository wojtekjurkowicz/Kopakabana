from tkinter import *
from zawodnicy import Druzyna, Zawodnik, Sedziowie, Sedzia
sedziowie = Sedziowie()

glowne_okno = Tk()
glowne_okno.resizable(width=False, height=False)

glowne_okno.title("Rozgrywki na słonecznej plaży Kopakabana")
glowne_okno.geometry("600x480")
bg = PhotoImage(file="kopakabana.ppm")
image_label = Label(glowne_okno, image=bg)
image_label.place(x=0, y=0)

hello_label = Label(image_label, font=('Batang', 16), text="Witamy na słonecznej plaży Kopakabana,\n"
                                                           "gdzie drużyny mogą się sprawdzić w sportach "
                                                           "zespołowych!\n Wybierz opcję")
hello_label.place(y=100)

button = Button(glowne_okno, height=2, width=25, text="Wprowadź własne dane: ")
button.place(x=100, y=300)

button = Button(glowne_okno, height=2, width=25, text="Wybierz dane z pliku: ")
button.place(x=300, y=300)


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