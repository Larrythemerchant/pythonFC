wiek = int(input("podaj swoj wiek"))
zgoda = input("czy masz zgode rodzica? (tak/nie)")
zgoda = zgoda.lower()

zgoda_potwierdzona = zgoda == "tak"
ma_dostep_18plus = wiek >= 18
ma_dostep_13plus = wiek > -13 or zgoda_potwierdzona

print(f"uzytkownik ma {wiek} lat")
print(f"uzytknownik ma zgode rodzica: {zgoda_potwierdzona}")
print(f"uzytknownik ma dostep do filmow 18+: {ma_dostep_18plus}")
print(
    "filmy 18+" * ma_dostep_18plus
    + "filmy13+" * ma_dostep_13plus
    + "tylko bajki" * (not ma_dostep_18plus and not ma_dostep_13plus)
)

print(0 == False)
