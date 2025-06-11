"""Program po uruchomieniu wyświetla informację o dostępnych komendach:

    saldo
    sprzedaż
    zakup
    konto
    lista
    magazyn
    przegląd
    koniec


Po wprowadzeniu odpowiedniej komendy, aplikacja zachowuje się w unikalny sposób dla każdej z nich:

    saldo - Program pobiera kwotę do dodania lub odjęcia z konta.
    sprzedaż - Program pobiera nazwę produktu, cenę oraz liczbę sztuk. Produkt musi znajdować się w magazynie. Obliczenia respektuje względem konta i magazynu (np. produkt "rower" o cenie 100 i jednej sztuce spowoduje odjęcie z magazynu produktu "rower" oraz dodanie do konta kwoty 100).
    zakup - Program pobiera nazwę produktu, cenę oraz liczbę sztuk. Produkt zostaje dodany do magazynu, jeśli go nie było. Obliczenia są wykonane odwrotnie do komendy "sprzedaz". Saldo konta po zakończeniu operacji „zakup” nie może być ujemne.
    konto - Program wyświetla stan konta.
    lista - Program wyświetla całkowity stan magazynu wraz z cenami produktów i ich ilością.
    magazyn - Program wyświetla stan magazynu dla konkretnego produktu. Należy podać jego nazwę.
    przegląd - Program pobiera dwie zmienne „od” i „do”, na ich podstawie wyświetla wszystkie wprowadzone akcje zapisane pod indeksami od „od” do „do”. Jeżeli użytkownik podał pustą wartość „od” lub „do”, program powinien wypisać przegląd od początku lub/i do końca. Jeżeli użytkownik podał zmienne spoza zakresu, program powinien o tym poinformować i wyświetlić liczbę zapisanych komend (żeby pozwolić użytkownikowi wybrać odpowiedni zakres).
    koniec - Aplikacja kończy działanie.


Dodatkowe wymagania:

    Aplikacja od uruchomienia działa tak długo, aż podamy komendę "koniec".
    Komendy saldo, sprzedaż i zakup są zapamiętywane przez program, aby móc użyć komendy "przeglad".
    Po wykonaniu dowolnej komendy (np. "saldo") aplikacja ponownie wyświetla informację o dostępnych komendach, a także prosi o wprowadzenie jednej z nich.
    Zadbaj o błędy, które mogą się pojawić w trakcie wykonywania operacji (np. przy komendzie "zakup" jeśli dla produktu podamy ujemną kwotę, aplikacja powinna wyświetlić informację o niemożności wykonania operacji i jej nie wykonać). Zadbaj też o prawidłowe typy danych.


"""

saldo = 1000
magazyn = [{"Nazwa produktu": "Rower", "Cena": 799, "Liczba Sztuk": 5}]
historia = []
while True:
    komenda = input("""
    1.Saldo
    2.Sprzedaż
    3.Zakup
    4.Konto
    5.Lista
    6.Magazyn
    7.Przegląd
    8.Koniec""")
    match komenda:
        case "1":
            kwota = float(input("Podaj kwotę którą chcesz odjąć lub dodać:"))
            if saldo + kwota < 0:
                print("Nie można ustawić kwoty na wartość ujemną.")
            else:
                saldo += kwota
                historia.append(("saldo", kwota))
        case "2":
            nazwa_produktu = input("Podaj nazwę produktu:")
            liczba = int(input("Podaj liczbę sztuk: "))

            produkt_znaleziony = False
            for produkt in magazyn:
                if produkt["Nazwa produktu"] == nazwa_produktu:
                    produkt_znaleziony = True
                    if produkt["Liczba Sztuk"] < liczba:
                        print(
                            print(
                                f"Nie ma wystarczającej liczby sztuk w magazynie. Dostępne: {produkt['Liczba Sztuk']}"
                            )
                        )
                    else:
                        cena = produkt["Cena"]
                        produkt["Liczba Sztuk"] -= liczba
                        kwota = cena * liczba
                        saldo += kwota
                        historia.append(("sprzedaż", nazwa_produktu, cena, liczba))
                        print(
                            f"Sprzedano {liczba} sztuk '{nazwa_produktu}' za {kwota} zł."
                        )
                        print(f"Nowe saldo: {saldo}")
            if not produkt_znaleziony:
                print(f"Produkt '{nazwa_produktu}' nie znajduje się w magazynie.")
        case "3":
            nazwa_produktu = input("Podaj nazwę produktu do zakupu: ")
            cena = float(input("Podaj cenę zakupu za sztukę: "))
            liczba = int(input("Podaj liczbę sztuk do zakupu: "))
            koszt = cena * liczba
            if saldo - koszt < 0:
                print("Nie wystarczające środki na koncie.")
                continue
            if cena < 0 or liczba <= 0:
                print("Cena i liczba sztuk muszą być dodatnie.")
                continue
            saldo -= koszt
            for produkt in magazyn:
                if produkt["Nazwa produktu"] == nazwa_produktu:
                    produkt["Liczba Sztuk"] += liczba
                    produkt["Cena"] += cena
                    break
                else:
                    magazyn.append(
                        {
                            "Nazwa produktu": nazwa_produktu,
                            "Liczba Sztuk": liczba,
                            "Cena": cena,
                        }
                    )
                historia.append(("zakup", nazwa_produktu, cena, liczba))
                print(
                    f"Zakupiono {liczba} szt. produktu '{nazwa_produktu}' za {koszt} zł."
                )
        case "4":
            print(f"Stan twojego konta wynosi: {saldo}")
            continue
        case "5":
            for produkt in magazyn:
                print(f"Nazwa: {produkt['Nazwa produktu']}")
                print(f"  Cena za sztukę: {produkt['Cena']} zł.")
                print(f"  Liczba sztuk: {produkt['Liczba Sztuk']}")
        case "6":
            nazwa = input("Podaj nazwę produktu")
            znaleziono = False
            for produkt in magazyn:
                if produkt["Nazwa produktu"].lower() == nazwa.lower():
                    print(f"Nazwa: {produkt['Nazwa produktu']}")
                    print(f"  Cena: {produkt['Cena']} zł.")
                    print(f"Liczba sztuk: {produkt['Liczba Sztuk']}")
                    znaleziono = True
                    break
        case "7":
            od = input("Podaj indeks początkowy: ")
            do = input("Podaj indeks końcowy: ")
            if od:
                od = int(od)
            else:
                od = 0

            if do:
                do = int(do)
            else:
                do = len(historia)

            if od < 0 or do > len(historia) or od > do:
                print(f"Niepoprawny zakres. Historia ma {len(historia)} wpisów.")
            else:
                print(historia[od:do])
        case "8":
            print("Zakończono działanie programu.")
            break
