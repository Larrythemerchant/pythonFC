"""
Jesteś szefem firmy technologicznej tworzącej system zarządzania dla międzynarodowego lotniska. System ten ma obsługiwać dane związane z lotami, liniami lotniczymi, pasażerami oraz stewardessami. Każdy lot może mieć przypisanych wielu pasażerów i jedną stewardessę, natomiast linie lotnicze mogą obsługiwać nieograniczoną liczbę lotów. Celem jest stworzenie programu, który pozwoli na efektywne zarządzanie i dostarczanie właściwych informacji na potrzeby logistyki i obsługi klienta lotniska.

**Program do zarządzania danymi lotów na międzynarodowym lotnisku**
Program powinien umożliwić:
1. Dodanie nowych danych do systemu:
   - Pasażera z przypisanym numerem lotu.
   - Stewardessy z przypisanym numerem lotu.
   - Linii lotniczej, która może obsługiwać wiele różnych lotów.
2. Przeglądanie i zarządzanie istniejącymi informacjami:
   - Pobranie listy pasażerów danego lotu.
   - Znalezienie przypisanej linii lotniczej dla wybranego pasażera.
   - Wyświetlenie listy lotów danej linii lotniczej.
   - Otrzymanie listy wszystkich pasażerów dla lotu, którego stewardessą jest wybrana osoba.
**Polecenia programu**
Po uruchomieniu, program powinien wyświetlić menu z następującymi komendami:
- dodaj - przechodzi do menu dodawania nowych danych.
- przeglądaj - przechodzi do menu przeglądania i zarządzania danymi.
- zakończ - kończy działanie programu.
**Menu dodawania danych (dodaj):**
Użytkownik może wybrać:
- pasażer - dodanie pasażera wymaga wprowadzenia imienia i nazwiska, numeru lotu.
- stewardessa - dodanie stewardessy wymaga wprowadzenia imienia i nazwiska, numeru lotu, do którego jest przypisana.
- linia_lotnicza - dodanie linii lotniczej wymaga wprowadzenia jej nazwy.
- zakończ_dodawanie - powrót do głównego menu.
**Menu przeglądania i zarządzania danymi (przeglądaj):**
Użytkownik może wybrać:
- lot - wprowadzenie numeru lotu wyświetla listę pasażerów tego lotu.
- pasażer - wprowadzenie imienia i nazwiska pasażera wyświetla nazwę linii lotniczej.
- linia_lotnicza - wprowadzenie nazwy linii lotniczej wyświetla listę lotów obsługiwanych przez linię.
- stewardessa - wprowadzenie imienia i nazwiska stewardessy wyświetla listę pasażerów jej lotu.
- zakończ_przeglądanie - powrót do głównego menu.
**Zakończenie pracy programu**
Polecenie zakończ powoduje zamknięcie aplikacji.
"""


class Pasazer:
    def __init__(self, imie, nazwisko, numer_lotu, numer_miejsca_w_samolocie=None):
        self.imie = imie
        self.nazwisko = nazwisko
        self.numer_lotu = numer_lotu
        self.numer_miejsca_w_samolocie = numer_miejsca_w_samolocie

    #     self.login = self.imie(0) + self.nazwisko.lower()
    #     self.haslo = self.nazwisko.lower() + "123"
    #
    #
    # def zmien_haslo(self, nowe_haslo):
    #     self.haslo = nowe_haslo
    #
    def __repr__(self):
        return f"Pasazer: {self.imie} {self.nazwisko}, from {self.numer_miejsca_w_samolocie}"


pasazer_1 = Pasazer("jan", "kowalski", "L12112")
# pasazer_1.zmien_haslo("jan")


class linia_lotnicza:
    def __init__(self, nazwa, lista_lotow):
        self.nazwa = nazwa
        self.lista_lotow = lista_lotow

    def dodaj_lot(self, lot):
        self.lot.append(lot)

    def __repr__(self):
        return f"{self.nazwa} {self.lista_lotow}"


class Stewardessa:
    def __init__(self, imie, nazwisko, numer_lot):
        self.imie = imie
        self.nazwisko = nazwisko
        self.numer_lotu = numer_lot

    def __repr__(self):
        return f"{self.imie}, {self.nazwisko},{self.numer_lotu}"

def wyszukaj_pasazerow_dla_lotu(numer_lotu):
    pasazerowie_dla_lotu = []
    for pasazer in lotnisko.get("pasazerowie"):
        if pasazer.numer_lotu == numer_lotu:
            pasazerowie_dla_lotu.append(pasazer)
    return pasazerowie_dla_lotu

def wyszukaj_linie_lotnicze_pasazera(imie, nazwisko):
    for pasazer in lotnisko.get("linie lotnicze"):
        if pasazer.imie == imie and pasazer.nazwisko == nazwisko:
            numer_lotu_pasazera = pasazer.numer_lotu
            break
    if numer_lotu_pasazera:
        for linia in lotnisko.get("linia"):


lotnisko = {
    "pasazerowie": [
        Pasazer("jan", "kowalski", "L12112"),
    ],
    "linie_lotnicze": [linia_lotnicza(nazwa="pies", lista_lotow="lotnisko")],
    "stewardessy": [
        Stewardessa("jan", "kowalski", "L12112"),
    ],
}

while True:
    wybor_uzytkownika = input("Wybierz opcje:1.dodaj\n2.przegladaj\n3.zakoncz\n")
    match wybor_uzytkownika:
        case 1:
            obiekt_do_dodania = input(
                "co chcesz dodac?:1.pasazerowie\n2.stewardessa\n3.linie lotnicze\n"
            )
            if obiekt_do_dodania.strip() in (
                "1",
                "pasazer",
                "pasazera",
                "pasazer",
                "pasazera",
            ):
                imie = input("podaj imie")
                nazwisko = input("podaj nazwisko")
                numer_lotu = input("podaj numero lotu")
                nowy_pasazer = Pasazer(imie, nazwisko, numer_lotu)
                lotnisko("PASAZEROWIE").append(nowy_pasazer)

            elif obiekt_do_dodania.strip() in ("2", "Stewardessa"):
                break

            elif obiekt_do_dodania.strip() in (
                "3",
                "linie_lotnicze",
                "linie_lotnicze",
                "linie_lotnicze",
            ):
                nazwa = input("podaj nazwe linii lotniczej:")
                lista_lotow_linii = []
                while True:
                    numer_lotu = input("podaj numero lotu")
                    if numer_lotu:
                        lista_lotow_linii.append(numer_lotu)
                    else:
                        break
                nowa_linia_lotnicza = linia_lotnicza(nazwa, lista_lotow_linii)
                lotnisko["Linie_lotnicze"].append(nowa_linia_lotnicza)

        case 2:
            opcja_do_przegladania = input ()


            match opcja_do_przegladania:
                case "1":
                    numer_lotu = input("podaj numero lotu")
                    pasazerowie = wyszukaj_pasazerow_dla_lotu(numer_lotu)
                    print()
                case '2':
                    break
                case '3':
                    nazwa_linii = input("podaj nazwe linii lotniczej:")
                    loty_linii = wyszukaj_loty_linii(nazwa_linii)


        case 3:
            break


