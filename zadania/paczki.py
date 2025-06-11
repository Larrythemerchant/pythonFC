"""Napisz program do obsługi ładowarki paczek. Po uruchomieniu, aplikacja pyta ile paczek chcesz wysłać, a następnie wymaga podania wagi dla każdej z nich.
Na koniec działania program powinien wyświetlić w podsumowaniu:
    Liczbę paczek wysłanych
    Liczbę kilogramów wysłanych
    Suma "pustych" - kilogramów (brak optymalnego pakowania). Liczba paczek * 20 - liczba kilogramów wysłanych
    Która paczka miała najwięcej "pustych" kilogramów, jaki to był wynik
Restrykcje:
    Waga elementów musi być z przedziału od 1 do 10 kg.
    Każda paczka może maksymalnie zmieścić 20 kilogramów towaru.
    W przypadku, jeżeli dodawany element przekroczy wagę towaru, ma zostać dodany do nowej paczki, a obecna wysłana.
    W przypadku podania wagi elementu mniejszej od 1kg lub większej od 10kg, dodawanie paczek zostaje zakończone i wszystkie paczki są wysłane. Wyświetlane jest podsumowanie.
Przykład 1:
    Ilość elementów: 2
    Wagi elementów: 7, 9
Podsumowanie:
    Wysłano 1 paczkę (7+9)
    Wysłano 16 kg
    Suma pustych kilogramów: 4kg
    Najwięcej pustych kilogramów ma paczka 1 (4kg)
"""

ilosc_towaru = int(input("podaj ilosc towaru:"))
ilosc_paczek = 0
paczka_z_najwieksza_pusta_waga = 0
numer_paczki_z_najwieksza_pusta_waga = 0
waga_paczki = 0
suma_kg = 0

for element in range(ilosc_towaru):
    waga_towaru = float(input(f"podaj wage towaru {element + 1}:"))
    if waga_towaru < 1 or waga_towaru > 10:
        print("waga przekroczona, paczki wysylane.")
        if waga_paczki > 0:
            ilosc_paczek += 1
            puste = 20 - waga_paczki
            if puste > paczka_z_najwieksza_pusta_waga:
                paczka_z_najwieksza_pusta_waga = puste
                numer_paczki_z_najwieksza_pusta_waga = ilosc_paczek
        break
    if waga_towaru + waga_paczki > 20:
        print("przekroczono maksymalna wage paczki, tworzymy now paczke")
        ilosc_paczek += 1
        puste = 20 - waga_paczki
        if 20 - waga_paczki > paczka_z_najwieksza_pusta_waga:
            paczka_z_najwieksza_pusta_waga = puste
            numer_paczki_z_najwieksza_pusta_waga = ilosc_paczek
        waga_paczki = waga_towaru
    else:
        waga_paczki += waga_towaru
    suma_kg += waga_towaru
if waga_paczki > 0:
    ilosc_paczek += 1
    puste = 20 - waga_paczki
    if puste > paczka_z_najwieksza_pusta_waga:
        paczka_z_najwieksza_pusta_waga = puste
        numer_paczki_z_najwieksza_pusta_waga = ilosc_paczek
if suma_kg > 0:
    print(
        f'Wysłano {ilosc_towaru} towarów w ilosci paczek {ilosc_paczek} o wadze {suma_kg} kg. Suma "pustych" kg {ilosc_paczek * 20 - suma_kg} kg.'
    )
    print(
        f"paczka z najwieksza liczba pustych kg: paczka {numer_paczki_z_najwieksza_pusta_waga}"
    )
else:
    print("nie wyslano zadnej paczki")
