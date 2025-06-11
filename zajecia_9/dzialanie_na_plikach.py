import warnings

file = open("piosenka.txt")
# print(file.read())
# print(file.readline())
# print(file.readline())
file.read()
# for line in file:
#    print(line)
print(file.readlines())
file.close()


def odlicz_sume_wydatkow(plik):
    file = open(plik)
    suma = 0
    for line in file:
        kwota = int(line)
        suma += kwota
    file.close()


# odlicz_sume_wydatkow("piosenka.txt")

with open("piosenka.txt") as file:
    for line in file:
        print(line)


# class NaszAsystent:
#     def __enter__(self):
#         print("prosimy zone o pozwolenie")
#         print("obiecujemy ze nie wrocimy na pozno")
#
#
#     def __exit__(self, exc_type, exc_value, traceback):
#         print("prosimy zone o wybaczenie")
#         print("kupujemy kwiaty")
#         print("obiecujemy ze to ostatni raz")
#
# with NaszAsystent() as asystent:
#     print("idziemy na piwo")
# #     print("pijemy piwo")
# #     print("wracamy do domu")
# #
# #with open('piosenka.txt',"w") as plik:
# #   nowy_tekst = "dodatkowa linijka\n"
# #   plik.write(nowy_tekst)
# with open('piosenka.txt',"a") as plik:
#     nowy_tekst = "dodatkowa linijka\n"
#     plik.write(nowy_tekst)
#
# with open('piosenka.txt',"w") as plik:
#     for linia in plik:
#         print(linia)
#     nowy_tekst = "dodatkowa linijka\n"
#     plik.write(nowy_tekst)
#
with open("piosenka2.txt", "r+") as plik:
    for linia in plik:
        print(linia)
    nowy_tekst = "dodatkowa linijka\n"
    plik.write(nowy_tekst)
# with open ('piosenka1.txt',"a+") as plik:
#     for linia in plik:
#         print(linia)
#     nowy_tekst = "dodatkowa linijka\n"
#     plik.write(nowy_tekst)
"""
#w oznacza, ze tworzy ci plik jak nie ma i do tego kursor jest na poczatku pliku - do nowego zapisu bez czytania
#w+ to samo tylko z czytaniem
#a - tworzy plik i kursor na koncu(mozemy dopisywac) nie mozemy czytac
#a+ -tworzy plik, kursor na koncu plus mozemy odczytywac
#r - otwiera plik do odczytu
#r+ - otwiera plik do odczytu i zapisu - kursor na początku
#a+ od r+ różni się tym, że w a+ tworzymy plik jak go nie mamy
"""
