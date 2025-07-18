"""
Stwórz system zarządzania księgozbiorem bibliotecznym, który pozwoli na monitorowanie przepływu książek oraz śledzenie budżetu biblioteki.
Po uruchomieniu systemu użytkownik otrzymuje listę komend do wyboru:
- doładowanie
- wypożycz
- zakup
- bieżący_stan
- zestawienie
- szczegóły_książki
- dziennik
- zakończ
Funkcje po wywołaniu danych komend są następujące:
1. doładowanie - Umożliwia dodanie środków do budżetu biblioteki lub ich odjęcie.
2. wypożycz - Rejestruje wypożyczenie książki przez czytelnika. System żąda podania imienia, nazwiska oraz daty ksiązki. Koszt wypożyczenia jest dodawany do budżetu.
3. zakup - Rejestruje zakup nowych książek dla biblioteki. System pyta o tytuł książki, koszt zakupu i liczbę egzemplarzy. Zakupione książki są dodawane do zbioru, a środki są odprowadzane z budżetu, który nie może być negatywny po transakcji.
4. bieżący_stan - Wyświetla aktualny stan środków finansowych.
5. zestawienie - Podsumowuje cały księgozbiór biblioteki wraz z cenami zakupu i ich ilością.
6. szczegóły_książki - Wyświetla dostępność i dane dotyczące pojedynczej książki po wpisaniu numeru ISBN.
7. dziennik - Przegląd historii transakcji. Podając wartości "od" i "do", system wyświetla zapisane działania w podanym zakresie. W przypadku pustych pól lub wartości spoza zakresu, użytkownik jest informowany o błędzie i wyświetlana jest liczba wszystkich zarejestrowanych transakcji.
8. zakończ - Kończy działanie programu.
**Inne wymagania:**
- System działa do momentu wybrania komendy zakończ.
- Operacje doładowanie, wypożycz oraz zakup są zapisywane dla późniejszej referencji przy użyciu komendy dziennik.
- Po każdej komendzie system wyświetla ponownie listę dostępnych opcji i prosi o wybór kolejnej.
- Ochrona przed błędami użytkownika, takimi jak wpisywanie błędnych danych czy żądanie zakupu na wartości ujemne.
"""

from file_handle import file_handler, save_temporary_data

lista_ksiazek = file_handler.ksiegozbior
saldo = file_handler.saldo
historia = file_handler.historia
print("witaj w systemie ksiegarni")
while True:
    komenda = input("""
    1.doładowanie
    2.wypożycz
    3.zakup
    4.biezacy_stan
    5.zestawienie
    6.szczegoly ksiazki
    7.dziennik
    8.zakoncz
    """)
    match komenda:
        case "1":
            kwota = float(input("podaj kwotle doladowania:"))
            if saldo + kwota < 0:
                print("nie mozesz ustawic salda na wartosc ujemna")
            else:
                saldo += kwota
            print(saldo)
        case "2":
            isbn = input("podaj ISBN: ")
            ksiazka_znaleziona = False
            for ksiazka in lista_ksiazek:
                if ksiazka.get("ISBN") == isbn:
                    if ksiazka("ilosc na stanie") <= 0:
                        print("nie ma takiej ksiazki na stanie")
                    ksiazka["ilosc_na_stanie"] -= 1
                    saldo += 10  # koszt wypozyczenia ksiazki
                    historia.append(
                        ksiazka[
                            f"wypozyczenie ksiazki : {ksiazka['tytuł']}, {ksiazka['autor']}, 1 sztuka"
                        ]
                    )
                    ksiazka_znaleziona = True
                    break
                if not ksiazka_znaleziona:
                    print("taka ksiazka nie istnieje")
        case "3":
            tytul = input("podaj tytu<UNK>: ")
            autor = input("podaj autor<UNK>")
            koszt = float(input("podaj koszt<UNK>: "))
            ilosc = int(input("podaj ilosc<UNK>: "))
            kategoria = input("podaj kategori<UNK>: ")
            isbn = input("podaj ISBN<UNK>: ")

            lista_ksiazek.append(
                {
                    "tytuł": tytul,
                    "autor": autor,
                }
            )
            print(lista_ksiazek)
            saldo -= koszt + ilosc
            historia.append(f"zakup ksiazki: {tytul}, {koszt}, {ilosc} sztuk")
            save_temporary_data(lista_ksiazek, saldo, historia)
        case "5":
            print(f"zestawienie ksiegozbioru:{lista_ksiazek}")
        case "7":
            od = input("podaj wartosc 'od' (numer transakcji): ")
            do = input("podaj wartosc 'od' (numer transakcji): ")
            if od:
                od = int(od)
            else:
                od = 0
            if do:
                do = int(do)
            else:
                do = len(historia)
            print(historia[od:do])
        case "8":
            print("zakonczono dzialanie programu")
            break

# file_handler.ksiegozbior = lista_ksiazek
# file_handler.saldo = saldo
# file_handler.historia = historia
# file_handler.save_ksiegozbior_file()
# file_handler.save_historia_file()
# file_handler.save_saldo_file()
