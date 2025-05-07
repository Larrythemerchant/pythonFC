# # lista_uczniow = ( 'jan', 'kasia', 'antek')
# # print(isinstance(lista_uczniow, Iterable))
# # for uczen in lista_uczniow:
# #     print(uczen)
from collections.abc import Iterable
print(isinstance(range(20), Iterable))
print(isinstance('michal', Iterable))
# # for number in range(20):
# #     print(number)
# ilosc_paczek = int(input('podaj ilosc paczek: '))
# waga_wszystkich_paczek = 0
# for paczka in range(ilosc_paczek):
#     print(paczka)
#     waga_paczki = float(input('podaj waga paczki: '))
#     waga_wszystkich_paczek += waga_paczki
# print(f'waga_wszystkich_paczek: {waga_wszystkich_paczek}')
# ################



for char in 'michal':
    print(char)
"""
for (tymczasowa zmienna in (interowalny obiekt)
    (blok kodu)
"""