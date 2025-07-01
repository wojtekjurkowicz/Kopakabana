# 🏐 Rozgrywki na słonecznej plaży Kopakabana

Gra symulacyjna organizująca turnieje w trzech dyscyplinach:
- Siatkówka plażowa
- Dwa ognie
- Przeciąganie liny

Zawiera zarówno interfejs graficzny (Tkinter), jak i tryb tekstowy.

---

## 📁 Struktura projektu

```

📦 projekt/
├── main.py                # Tryb tekstowy – symulacja rozgrywek w terminalu
├── graficznie.py          # Interfejs graficzny (Tkinter)
├── rozgrywki.py           # Logika gier i zarządzanie turniejami
├── zawodnicy.py           # Klasy Osoba, Zawodnik, Sędzia, Drużyna
├── sedziowie.txt          # Lista imion i nazwisk sędziów do losowania
├── ludzie.txt             # Lista imion i nazwisk zawodników do losowania
├── \*.pickle               # Pliki zapisu danych rozgrywek
└── README.md              # Ten plik

````

---

## ▶️ Uruchamianie

### ✅ Tryb graficzny (zalecany)
Wymaga `Tkinter` (standard w Pythonie).

```bash
python graficznie.py
````

### 🖥️ Tryb tekstowy

```bash
python main.py
```

---

## 🎮 Funkcje

* Tworzenie drużyn ręcznie lub losowo
* Edytowalna lista sędziów
* Automatyczne tworzenie meczów, półfinałów i finału
* Zapisywanie i wczytywanie stanu rozgrywek
* Obsługa 3 dyscyplin z osobną punktacją
* Interfejs graficzny z tłem i grafiką

---

## 💾 Zapisywanie danych

Rozgrywki są zapisywane do plików:

* `siatkowka.pickle`
* `dwa_ognie.pickle`
* `przeciaganie_liny.pickle`

Można je później wczytać i kontynuować grę.

---

## 📌 Wymagania

* Python 3.7+
* Tkinter (wbudowany)
* Pliki: `ludzie.txt`, `sedziowie.txt`, grafiki `.ppm`, `icon.ico` (jeśli używasz GUI)

---

## 📋 Autorzy

Projekt stworzony jako symulacja turniejowa — edukacyjny przykład OOP, GUI i losowości w Pythonie.

---

## ✅ Możliwe usprawnienia

* Refaktoryzacja powielonego kodu
* Obsługa większej liczby dyscyplin
* Historia wyników
* Testy jednostkowe

---