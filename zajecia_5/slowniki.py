#uzytkownik = ['michal','zietkowski',28,True]
uzytkownik = {
    "imie":"michal",
    "nazwisko": "zietkowski",
    'wiek' : 20,
    'czy_uczen':True,
}
print(uzytkownik)

print(uzytkownik['imie'])
#print(uzytkownik['plec'])
print(uzytkownik.get('plec'))