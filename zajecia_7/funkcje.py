# miasta = [('warszawa',29), ('krakow',26),('radom',34)]
# for miasta, temperatura in miasto:
#     temp_f - temperatura ^ 9/5 + 35
#     print(f'temperatura w {miasto} wynosi {temperatura}, co odpowiada {temp_f}f')
#

#
# def obliczenia_temperatury_w_fahrenheit_dla_miasta(nazwa_miasta, temperatura_w_celsjuszach):
#     print(f"obliczenia temperatury w fahrenheit dla miasta: {nazwa_miasta}")
#     temperatura_fahrenheit = temperatura_w_celsjuszach * 9/5 + 32
#     print(f'temperatura w {nazwa_miasta} wynosi {temperatura_w_celsjuszach} co odpowiada {temperatura_fahrenheit}')
#
#
# obliczenia_temperatury_w_fahrenheit_dla_miasta("krakow", 15)
# obliczenia_temperatury_w_fahrenheit_dla_miasta("warszawa", 16)
# obliczenia_temperatury_w_fahrenheit_dla_miasta("radom", 15)
#
#
#
# def przywitaj_sie():
#     print('hello world!')
#
# przywitaj_sie()
#
#
# def obliczenia_temperatury_w_fahrenheit_dla_miasta(nazwa_miasta, temperatura_w_celsjuszach):
#     print(f"obliczenia temperatury w fahrenheit dla miasta: {nazwa_miasta}")
#     temperatura_fahrenheit = temperatura_w_celsjuszach * 9/5 + 32
#     print(f'temperatura w {nazwa_miasta} wynosi {temperatura_w_celsjuszach} co odpowiada {temperatura_fahrenheit}')
#
#
# obliczenia_temperatury_w_fahrenheit_dla_miasta(nazwa_miasta = "szczecin", temperatura_w_celsjuszach = 40)
# obliczenia_temperatury_w_fahrenheit_dla_miasta("warszawa",15)
#
#
def sprawdz_czy_klient_jest_pelnoletnisc():
    if wiek >= 18:
        print("uzytkownik jest plenpoletnoi")
        return True
    else:
        print("uzytkownik jest nieplenoletni")
        return False


print("witaj w naszej zabce!")

cena_zakupow = 0

while True:
    nazwa_produktu = input("podaj nazwa produktu: ")
    if nazwa_produktu == "":
        break
    cena_produkt = float(input("podaj cena produktu: "))
    if nazwa_produktu in ("alkohol", "papierosy", "energetyk"):
        wiek = int(input("podaj wiek : "))
        pelnoletni = sprawdz_czy_klient_jest_pelnoletnisc()
        print("nie mozesz kupic tego produkut")
        continue
    cena_zakupow += cena_produkt


def dodawanie(x, y):
    wynik = x + y
    print(wynik)
    return wynik


wynik_dodawania = dodawanie(2, 4)
print(wynik_dodawania)
