zamowienie = input("czy zamowienie przekracza 100zl? (tak/nie)")
zamowienie = zamowienie.lower()

vip = input("czy jestes klientem vip? (tak/nie)")
vip = vip.lower()

promocja = input("czy kupiles propdukt promocyjny? (tak/nie)")
promocja = promocja.lower()

zamowienie_powyzej_100 = zamowienie == "tak"
klient_vip = vip == "tak"
produkt_promocyjny = promocja == "tak"

rabat = 0.15 * (zamowienie_powyzej_100 or klient_vip) + 0.05 * produkt_promocyjny

# print(f'twoj rabat wynosi{rabat * 100:.0f}%')
print(f"twoje zamowienie po rabatowaniu wynosi: {zamowienie * (1 - rabat)}")
