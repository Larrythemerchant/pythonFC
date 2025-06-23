"""
Utwórz program do zarządzania bazą szkolną. Istnieje możliwość tworzenia trzech typów użytkowników (uczeń, nauczyciel, wychowawca) a także zarządzania nimi.
Po uruchomieniu programu można wpisać jedną z następujących komend: utwórz, zarządzaj, koniec.
    Polecenie "utwórz" - Przechodzi do procesu tworzenia użytkowników.
    Polecenie "zarządzaj" - Przechodzi do procesu zarządzania użytkownikami.
    Polecenie "koniec" - Kończy działanie aplikacji.
Proces tworzenia użytkowników:
    Należy wpisać opcję, którą chcemy wybrać: uczeń, nauczyciel, wychowawca, koniec. Po wykonaniu każdej z opcji (oprócz "koniec") wyświetla to menu ponownie.
    Polecenie "uczeń" - Należy pobrać imię i nazwisko ucznia (jako jedna zmienna, można pobrać je jako dwie zmienne, jeżeli zostanie to poprawnie obsłużone) oraz nazwę klasy (np. "3C")
    Polecenie "nauczyciel" - Należy pobrać imię i nazwisko nauczyciela (jako jedna zmienna, labo dwie, jeżeli zostanie to poprawnie obsłużone), nazwę przedmiotu prowadzonego, a następnie w nowych liniach nazwy klas, które prowadzi nauczyciel, aż do otrzymania pustej linii.
    Polecenie "wychowawca" - Należy pobrać imię i nazwisko wychowawcy (jako jedna zmienna, albo dwie, jeżeli zostanie to poprawnie obsłużone), a także nazwę prowadzonej klasy.
    Polecenie "koniec" - Wraca do pierwszego menu.
Proces zarządzania użytkownikami:
    Należy wpisać opcję, którą chcemy wybrać: klasa, uczen, nauczyciel, wychowawca, koniec. Po wykonaniu każdej z opcji (oprócz "koniec") wyświetla to menu ponownie.
    Polecenie "klasa" - Należy pobrać klasę, którą chcemy wyświetlić (np. "3C") program ma wypisać wszystkich uczniów, którzy należą do tej klasy, a także wychowawcę tejże klasy.
    Polecenie "uczeń" - Należy pobrać imię i nazwisko uczenia, program ma wypisać wszystkie lekcje, które ma uczeń a także nauczycieli, którzy je prowadzą.
    Polecenie "nauczyciel" - Należy pobrać imię i nazwisko nauczyciela, program ma wypisać wszystkie klasy, które prowadzi nauczyciel.
    Polecenie "wychowawca" - Należy pobrać imię i nazwisko nauczyciela, a program ma wypisać wszystkich uczniów, których prowadzi wychowawca.
    Polecenie "koniec" - Wraca do pierwszego menu.
"""
class Uczen:
    def __init__(self, imie, nazwisko, klasa):
        self.imie = imie
        self.nazwisko = nazwisko
        self.klasa = klasa
    def pelne_imie(self):
        return f"{self.imie} {self.nazwisko}"
class Nauczyciel:
    def __init__(self, imie, nazwisko, przedmiot, klasy =None):
        self.imie = imie
        self.nazwisko = nazwisko
        self.przedmiot = przedmiot
        self.klasy = klasy if klasy else[]

    def pelne_imie(self):
        return f"{self.imie} {self.nazwisko}"
class Wychowawca:
    def __init__(self, imie, nazwisko, klasa):
        self.imie = imie
        self.nazwisko = nazwisko
        self.klasa = klasa

    def pelne_imie(self):
        return f"{self.imie} {self.nazwisko}"

Uczniowie = []
Nauczyciele = []
Wychowawcy = []

def utworz():
    while True:
        komenda = input("Wybierz typ użytkownika do utworzenia: uczeń, nauczyciel, wychowawca, koniec")
        if komenda == "uczeń":
            imie = input("Podaj imie: ")
            nazwisko = input("Podaj nazwisko: ")
            klasa = input("Podaj klase: ")
            Uczniowie.append(Uczen(imie, nazwisko, klasa))
        elif komenda == "nauczyciel":
            imie = input("Podaj imie: ")
            nazwisko = input("Podaj nazwisko: ")
            przedmiot = input("Podaj przedmiot: ")
            klasy = input("Podaj klasy: ").split(",")
            Nauczyciele.append(Nauczyciel(imie, nazwisko, przedmiot, klasy))
        elif komenda == "wychowawca":
            imie = input("Podaj imie: ")
            nazwisko = input("Podaj nazwisko: ")
            klasa = input("Podaj klase: ")
            Wychowawcy.append(Wychowawca(imie, nazwisko, klasa))
        elif komenda == "koniec":
            break
def zarzadzaj():
    while True:
        komenda = input("Należy wpisać opcję, którą chcemy wybrać: klasa, uczen, nauczyciel, wychowawca, koniec.")
        if komenda == "klasa":
            klasa = input("Podaj klase: ")
            print("Uczniowie")
            for uczen in Uczniowie:
                if uczen.klasa == klasa:
                    print(f"- {uczen.pelne_imie()}")
            print("Wychowawca:")
            for wychowawca in Wychowawcy:
                if wychowawca.klasa == klasa:
                    print(f"- {wychowawca.pelne_imie()}")
                    break
            else:
                print("Brak wychowawcy.")
        elif komenda == "uczen":
            imie = input("Podaj imie: ")
            nazwisko = input("Podaj nazwisko: ")
            znaleziony = None
            for uczen in Uczniowie:
                if uczen.imie == imie and uczen.nazwisko == nazwisko:
                    znaleziony = uczen
                    break
            if not znaleziony:
                print("Nie znaleziono ucznia.")
                continue
            print("lekcje ucznia:")
            for nauczyciel in Nauczyciele:
                if znaleziony.klasa in nauczyciel.klasy:
                    print(f"- {nauczyciel.przedmiot} (prowadzi: {nauczyciel.pelne_imie()})")
        elif komenda == "nauczyciel":
            imie = input("Podaj imie: ")
            nazwisko = input("Podaj nazwisko: ")
            for nauczyciel in Nauczyciele:
                if nauczyciel.imie == imie and nauczyciel.nazwisko == nazwisko:
                    print("prowadzi klasy:")
                    for klasa in nauczyciel.klasy:
                        print(f"- {klasa}")
                    break
            else:
                print("Nie znaleziono nauczyciela.")
        elif komenda == "wychowawca":
            imie = input("Podaj imie: ")
            nazwisko = input("Podaj nazwisko: ")
            for wychowawca in Wychowawcy:
                if wychowawca.imie == imie and wychowawca.nazwisko == nazwisko:
                    print("uczniowie w klasie:")
                    for uczen in Uczniowie:
                        print(f"- {uczen.pelne_imie()}")
            else:
                print("nie znaleziono wychowawcy.")
        elif komenda == "koniec":
            break
def main():
    while True:
        print("Dostępne polecenia: utwórz, zarządzaj, koniec")
        komenda = input("wybierz opcje")
        if komenda == "utwórz":
            utworz()
        if komenda == "zarządzaj":
            zarzadzaj()
        if komenda == "koniec":
            break
if __name__ == "__main__":
    main()