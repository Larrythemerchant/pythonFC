punktacja_uzytknownika = 0

# pytanie 1
odpowiedz = input("1 typ liczby 5? (int/float):")
punktacja_uzytknownika += 1 * (odpowiedz == "int")

# pytanie2
odpowiedz = input("2.typ wartosci hello? str czy int")
punktacja_uzytknownika += 1 * (odpowiedz == "str")
# pytanie3
odpowiedz = input("3.czy zmiennie maja okreslony typ przy deklaracji? (tak/nie):")
punktacja_uzytknownika += 1 * (odpowiedz == "nie")

odpowiedz = input("4.typ wyniku 5/2 (int/float):")
punktacja_uzytknownika += 1 * (odpowiedz == "float")
