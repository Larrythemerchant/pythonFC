"""
Treść zadania

Napisz program do obsługi rezerwacji biletów grupowych na wydarzenie.

Działanie programu:

    Program pyta o liczbę osób w grupie.

    Dla każdej osoby pobiera liczbę biletów, które chce kupić (od 1 do 5).

    Jeśli użytkownik poda wartość spoza zakresu 1–5 lub wprowadzi nieprawidłową wartość, program kończy wprowadzanie danych.

    Na koniec program wyświetla podsumowanie:

        Łączną liczbę biletów,

        Kwotę do zapłaty (20 zł za bilet, zniżka do 15 zł za bilet obowiązuje, jeśli liczba osób w grupie jest co najmniej 5 i łączna liczba biletów wynosi co najmniej 10),

        Największą pojedynczą transakcję biletową,

        Liczbę błędnych wpisów (czyli ile razy wprowadzono nieprawidłową wartość).

Przykłady

Przykład 1:

text
Liczba osób: 5
Bilety: 3, 2, 4, 1, 5

Podsumowanie:
Łączna liczba biletów: 15
Kwota do zapłaty: 225 zł (zniżka)
Największa transakcja: 5
Liczba błędnych wpisów: 0

Przykład 2:

text
Liczba osób: 6
Bilety: 2, 1, 0 (błąd)

Podsumowanie:
Łączna liczba biletów: 3
Kwota do zapłaty: 60 zł
Największa transakcja: 2
Liczba błędnych wpisów: 1

Przykład 3:

text
Liczba osób: 3
Bilety: 5, 6 (błąd)

Podsumowanie:
Łączna liczba biletów: 5
Kwota do zapłaty: 100 zł
Największa transakcja: 5
Liczba błędnych wpisów: 1

"""

liczba_gosci_w_grupie = int(input("podaj liczbe gosci w grupie: "))
laczna_liczba_biletow = 0
najwieksza_ilosc_biletow_w_transakcji = 0
transakcja_z_najwieksza_iloscia_biletow = 0


for transakcja in range(liczba_gosci_w_grupie):
    liczba_biletow_transakcji = int(
        input(f"podaj liczbe biletow dla osoby {transakcja + 1}: ")
    )
    if liczba_biletow_transakcji < 1 or liczba_biletow_transakcji > 5:
        print("nieprawidlwa wartosc")
        break
    laczna_liczba_biletow += liczba_biletow_transakcji
    if liczba_biletow_transakcji > najwieksza_ilosc_biletow_w_transakcji:
        najwieksza_ilosc_biletow_w_transakcji = liczba_biletow_transakcji
        transakcja_z_najwieksza_iloscia_biletow = transakcja + 1

if liczba_gosci_w_grupie >= 5 and laczna_liczba_biletow >= 10:
    cena_biletu = 15
else:
    cena_biletu = 20
print(f"liczba biletow: {laczna_liczba_biletow}")
print(f"laczna cena biletow to {laczna_liczba_biletow * cena_biletu}")
print(f"najwieksza transakcja: {najwieksza_ilosc_biletow_w_transakcji}")
print(
    f"transakcja z najwieksza iloscia biletow: {transakcja_z_najwieksza_iloscia_biletow}"
)
