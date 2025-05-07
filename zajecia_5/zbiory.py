zbior_kolory = {'czerwony','niebieski','zielony',24,True,('adam','kowalski')}
print(zbior_kolory)
print(id(zbior_kolory))
zbior_kolory.add('zolty')
print(id(zbior_kolory))
#print(zbior_kolory[0])
zbior_kolory.add('czerwony')
print(zbior_kolory)

zbior_kolory.remove('czerwony')
print(zbior_kolory)
for element in zbior_kolory:
    print(element)

lista_kolorow = list(zbior_kolory)
print(lista_kolorow)