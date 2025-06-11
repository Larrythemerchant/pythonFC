# uzytkownik = ['michal','zietkowski',28,True]
uzytkownik = {
    "imie": "michal",
    "nazwisko": "zietkowski",
    "wiek": 20,
    "czy_uczen": True,
}
# print(uzytkownik)
#
# print(uzytkownik['imie'])
# #print(uzytkownik['plec'])
# print(uzytkownik.get('plec'))
#
# uzytkownik['plec'] = 'mezczyzna'
#
# print(uzytkownik)
#
# uzytkownik['plec'] = 'kobieta'
# print(uzytkownik)
#
# del uzytkownik['plec']
# print(uzytkownik)
#
# uzytkownik.pop('imie')
# print(uzytkownik)
#
# #########iteracje

for item in uzytkownik:
    print(item)

# for value in uzytkownik.values():
#    print(value)


for key in uzytkownik.keys():
    print(key)
for key, value in uzytkownik.items():
    print(f"{key}: {value}")

if "adres" in uzytkownik:
    del uzytkownik["adres"]
else:
    print("nie ma takiego klucza")
# del uzytkownik['adres']
# lista_rzeczy = [1,2,3,4,5]
