zawod = input("podaj swoj zawod: ")
wiek = int(input('podaj swoj wiek: '))


match zawod:
    case'policjant':
        print(f'do emerytury zostalo ci {45-wiek}: ')
    case _:
        print(f'do emerytury zostalo ci {65-wiek}: ')



liczba = int(input('podaj liczba: '))

