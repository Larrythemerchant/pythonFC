# wiek = int(input('podaj swoj wiek:'))
#
#
# while wiek < 65:
#     print(f'nie powinienes juz byc na emeryturze! masz {wiek} lat')
#     wiek += 1
# print(f'masz {wiek} lat, powinienes juz byc na emeryturze!')
#
# wiek= int(input('podaj swoj wiek:'))
#
# while wiek >= 65:
#     print('powinienes juz byc na emeryturze!')


# imie = input('podaj swoje imie: ')
#
# while imie != 'michal':
#     print('nie jestes michalem')
#     imie = input('podaj swoje imie: ')

# imie = input("podaj swoje imie: ")
# wiek = int(input("podaj swoje wiek: "))
#
#
# while True:
#     if imie == 'michal':
#         print('czesc michal')
#         break
#         print('kod po breaku!!')
#     else:
#         imie = input('podaj swoje imie: ')
# print('tutaj trafiamy po breaku!!!')

########### petla while:
# while {warunek logiczny}:
#   {blok kodu} a wyknuje sie dopoki warunek logicznt jest spelniony
#
# wiek = int(input('podaj swoj wiekL: '))
#
# while wiek < 65:
#     if wiek== 18:
#         print('masz 18 lat')
#         continue
#     print(f'nie powineienes jeszcze byc an emeryturze! masz {wiek} lat')


wiek = int(input("podaj swoj wiek: "))

if wiek >= 18:
    print("masz 18 lat lub wiecej")
else:
    pass
print("moje kolejne instrukcje")
