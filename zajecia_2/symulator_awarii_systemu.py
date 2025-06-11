serwer_awaria = input("serwer odpowiada? (tak/nie)")
serwer_awaria = serwer_awaria.lower()

baza_awaria = input("baza danych dziala? (tak/nie)")
baza_awaria = baza_awaria.lower()
aplikacja_awaria = input("aplikacja webowa jest dostepna? (tak/nie)")
aplikacja_awaria = aplikacja_awaria.lower()

print(
    "natychmiastowa interwencja" * (serwer_awaria == "tak" and baza_awaria == "tak")
    + "awaria czesciowa sprawdz system"
    * (serwer_awaria == "tak" or baza_awaria == "tak" or aplikacja_awaria == "tak")
    + "system dziala poprawnie"
    * (serwer_awaria == "nie" and baza_awaria == "nie" and aplikacja_awaria == "nie")
)
