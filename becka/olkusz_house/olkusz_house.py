print("Witaj w domu olkusza! Proszę wybrać czynność na następne 5 lat: ")

while True:
    command = input("""
    1. Świętowanie
    2. Koprofag
    3. Noszenie gruzu
    4. Zejście do kuchni
    5. Pora koniom wody dac
    """)
    match command:
        case "1":
            swietowanie = input("czy podwijać łapy? Tak/nie: ").lower()
            if swietowanie == "tak":
                for _ in range(5):
                    print("*wciaganie do dupy powietrza")
                    print("*pierd*")
            elif swietowanie == "nie":
                real_swietowanie = input("Czy wskakiwać do wody? Tak/nie?:").lower()
                if real_swietowanie == "tak":
                    print("SZOROWANIE PAŁY!")
                else:
                    print("Wracam do pokoju tu śmierdzi kałomantom")
                    continue
        case "2":
            print("*koprofag wchodzi do pokoju* Co teraz?")
            activity_koprofag = input(
                "Gramy w faraona czy sramy na dywan?: faraon/dywan"
            ).lower()
            if activity_koprofag == "faraon":
                print("spedzacie upojna noc grajac w faraona")
                continue
            elif activity_koprofag == "dywan":
                print("spedzacie upojna noc srajac na dywan")
                continue
        case "3":
            print("Dziadyga prosi o noszenie 10 ton gruzu, ile dasz rady przeniesc?")
            ilosc_gruzu = float(input("podaj ile ton gruzu przeniesiesz 1-10"))
            if ilosc_gruzu <= 2:
                print("dziadyga spuszcza ci wpierdol nic nie dostajesz, wypierdalaj")
                continue
            elif ilosc_gruzu <= 4:
                print("dostajesz zbyszka od starego grzyba a teraz wypierdalaj")
                continue
            elif ilosc_gruzu >= 6:
                print("dziadzia jest szczesliwy i daje ci niemokrego kotleta")
                continue
        case "4":
            print(
                "schodzisz do kuchni, a w niej babka. Jeszcze cie nie zauwazyla co teraz zrobisz?"
            )
            kitchen_activity = input("Sa 3 opcje: ucieczka/rozmowa/walka").lower()
            if kitchen_activity == "ucieczka":
                print("spierdalasz do pokoju, nie masz nic do picia")
                continue
            elif kitchen_activity == "rozmowa":
                print("babka ci każe pilnować słoninki")
                continue
            elif kitchen_activity == "walka":
                print("stajesz do walki z babsztylem")
                continue
        case "5":
            print("ŁEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
            break
