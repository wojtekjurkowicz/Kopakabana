from tkinter import Tk, Label

root = Tk() # tworzenie glownego okienka
root.title('App') # nazwa aplikacji
root.geometry("1920x1080") #ustalanie wielkosci okna

label = Label(root, text="Kocham fizyke!!! <3", font=200) # tekst
label.pack(expand=True) # pack - gdzie ma byc dany obiekt, domyslnie top

root.mainloop() # potrzebne do uruchomienia