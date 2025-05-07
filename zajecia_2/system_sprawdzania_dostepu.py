"""System sprawdzania dostępu

Wczytaj od użytkownika:
- wiek (liczba całkowita),
- hasło dostępu (tekst),
- czy jest pracownikiem firmy (tak/nie).

Stwórz zmienne:
- has_prawidlowy_wiek (wiek >= 18),
- haslo_poprawne (hasło == "admin123"),
- jest_pracownikiem (tak/nie).

Dostęp przyznaj jeśli: (pełnoletni i poprawne hasło) lub (jest pracownikiem).

Wyświetl:
- "Dostęp przyznany" lub "Dostęp zabroniony", bez użycia ifów."""


wiek = int(input("podaj swoj wiek: "))
haslo = input("podaj haslo dostepu: ")
status_pracownika = input('podaj status pracownika (tak/nie): ').lower()

jest_pracownikiem = status_pracownika == 'tak'
has_prawidlowy_wiek = wiek >= 18
haslo_poprawne = haslo == "admin123"

dostep_przyznany = (has_prawidlowy_wiek and haslo_poprawne) or jest_pracownikiem
print("dostep przyznany" * dostep_przyznany + "dostep zabroniony" * (not dostep_przyznany))


