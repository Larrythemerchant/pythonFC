ilosc_towaru = int(input("podaj ilosc towaru:"))
ilosc_paczek = 1
paczka_z_najwieksza_pusta_waga = 20
numer_paczki_z_najwieksza_pusta_waga = None
waga_paczki = 0

for element in range(ilosc_towaru):
    waga_towaru = float(input(f"podaj wage towaru {element + 1}:"))
    if waga_towaru + waga_paczki > 20:
        print("przekroczono maksymalna wage paczki, tworzymy now paczke")
        if 20 - waga_paczki < paczka_z_najwieksza_pusta_waga:
            paczki_z_najwieksza_pusta_waga = waga_paczki
            numer_paczki_z_najwieksza_pusta_waga = ilosc_paczek
        waga_paczki = waga_towaru
        ilosc_paczek += 1
    else:
        waga_paczki += waga_towaru
