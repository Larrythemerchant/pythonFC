# wiek = int(input('podaj wiek'))
#
# if wiek >= 18:
#     pelnoletni = True
# else:
#     pelnoletni = False
#
# pelnoletni_skrot = True if wiek >= 18 else False
#
# #nazwa zmiennej = <pierwsza_wartosc> if <warunek na pierwsza wartosc> else <druga_wartosc>
# print(pelnoletni)

#### listcomprehension

lista_uczniow = ['jan','marek','Kasia','Ania']

# poprawna_lista_uczniow = []
#
# for uczen in lista_uczniow:
#     poprawna_lista_uczniow.append(uczen.capitalize())

# print(poprawna_lista_uczniow)
#
# poprawna_lista_uczniow_comprehension = [uczen.capitalize() for uczen in lista_uczniow]
#
# print(poprawna_lista_uczniow_comprehension)
#
#
# #nazwa_zmiennej = [<wartosc ktora zapisujemy w liscie> for <tymczasowa_zmiernna> in <ITERABLE>]
#
# kwadraty_liczb = [x**2 for x in range(10)]

# print(kwadraty_liczb)
lista_chlopcow = [uczen.capitalize() for uczen in lista_uczniow if not uczen.lower().endswith('a') ]
lista_dziewczynek = [uczen.capitalize() for uczen in lista_uczniow if uczen.lower().endswith('a')]
print(lista_dziewczynek)
print(lista_chlopcow)
# nazwa_zmiennej = [<wartosc ktora zapisujemy w liscie> for <tymczasowa_zmienna> in <iterable> if warunek>]

######dict comprehensions
slownik = {
    "imie"= "nazwisko",
}
slownik_uczniow = {uczen: uczen.capitalize() for uczen in lista_uczniow}
slownik_uczniow_1 = {index: value for index, valie in enumerate(slownik_uczniow)}

print(slownik_uczniow_1)
print(slownik_uczniow)
dea