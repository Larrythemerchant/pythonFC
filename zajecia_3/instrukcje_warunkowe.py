# # = "Krystian"
# #(imie)
#
# print('symulacja sklepu żabka: ')
# print('witaj w sklepie zabka!')
#
# nazwa_produktu = input('podaj nazwe produktu: ')
# cena_produktu = float(input('podaj cene produktu: '))
# #wiek_klienta = int(input ('podaj swoj wiek'))
#
#
#
#
# # if wiek_klienta >= 18:
# #     print('warunek wieku zostal spelniony.')
# #     print('dalej jestesmy w bloku kodu')
# #
# #
# # if wiek_klienta < 18:
# #     print('warunek wieku nie zostal spelniony.')
# # if wiek_klienta >= 18:
# #     print('mozesz kupic produkt.')
# # else:
# #     print('warunek wieku nie zostal spelniony.')
# #
# #
#
# # print('jestesmy poza instrukcja warunkowa')
# if nazwa_produktu.lower() == 'piwo' or nazwa_produktu.lower() == 'papierosy' or nazwa_produktu.lower() == 'energetyk':
#     print('ten produkt jest przeznaczony dla osob pelnoletnich')
#     wiek_klienta = int(input('podaj swoj wiek'))
#     if wiek_klienta >= 18:
#         print('masz 18 lat lub wiecej mozesz kupic ten produkt')
#         print(f'kupiles produkt{nazwa_produktu} o cenie: {cena_produktu}zł')
#     else:
#         print('nie masz 18 lat nie mozesz kupic tego produktu')
# else:
#     print('ten produkt nie wymaga podwania wieku')
#     print(f'kupiles produkt{nazwa_produktu} o cenie: {cena_produktu}zł')

zawod = input("podaj swoj zawod: ")
wiek = int(input("podaj wiek: "))

if zawod == "policjant":
    print(f"do emerytury zostalo ci {45 - wiek} lat")
elif zawod == "zolnierz":
    print(f"do emerytury zostalo ci {50 - wiek} lat")
elif zawod == "nauczyciel":
    print(f"do emerytury zostalo ci {60 - wiek} lat")
elif zawod == "praca biurowa":
    print(f"do emerytury zostalo ci {65 - wiek} lat")
elif zawod == "programista":
    print("nie ma dla ciebie emerytury")
else:
    print(f"do twojej emerytury prawdopodobnie zostalo ci {65 - wiek} lat")


"""
warunek_logiczny = wyrazenie ktore zwroci wartosc typu boolean (true/false)
if {warunek_logiczny}: 
    {blok kodu}
elif {warunek_logiczny}:
    {blok kodu}
else
"""
