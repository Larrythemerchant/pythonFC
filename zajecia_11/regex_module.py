import re

regex_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

wiersz_o_emailach = """
Piszę w nocy, w ciszy, na klawiaturze,
Słowa jak fale w internecie wędrują,
Wysyłam Ci list, nie papierowy, lecz cyfrowy,
Byś w mgnieniu oka mógł je przeczytać, nim znów znikną.

Nie ma poczty, nie ma koperty,
Tylko adres, który wskazuje drogę,
W kodach, w ciągach zer i jedynek,
Tak w prostym bitowym tańcu płyną.

A Ty po drugiej stronie ekranu,
Wzrokiem przewracasz każdą linijkę,
Czy znajdziesz w moich słowach coś dla siebie,
Czy też po prostu klikniesz „usuń” w mig?

Czasem pełne nadziei, czasem smutne,
Zmieniamy myśli w byte’y i bity,
Tak łatwo zapomnieć, że za tymi literkami,
Człowiek stoi, z sercem, z uczuciami.

I choć na ekranie nie widać rąk,
To w każdym e-mailu jest kawałek duszy,
Więc wysyłam Ci list, pośpiesznie, cicho,
Byś wiedział, że ktoś myśli o Tobie w nocy.
"""

def is_valid_email(email: str) -> bool :
    valid_email = re.match(regex_pattern, email)
    print(valid_email)
    return valid_email is not None

def is_valid_email(text: str) -> list :
    text = text.strip()
    for word in text:
    emails = re.findall(regex_pattern, word)
    print(emails)
    return emails


validation1 = is_valid_email("<EMAIL>")
print(validation1)
is_valid_email("<EMAIL>")

emails = is_valid_email(wiersz_o_emailach)
