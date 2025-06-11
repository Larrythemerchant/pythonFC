def przywitaj_sie(imie, nazwisko):
    print(f"Witaj!{imie} {nazwisko}")
    return f"Witaj!{imie} {nazwisko}"


przywitaj_sie(imie="lisiewski", nazwisko="krystian")


def przywitaj_sie_z_args(*moje_args):
    argumenty = moje_args
    print(argumenty)


przywitaj_sie_z_args(1, 2, 3, "michal", "zietkowski")


def przywitaj_sie_z_kwargs(**moje_kwargs):
    print(moje_kwargs)


przywitaj_sie_z_kwargs(imie="michal", nazwisko="zietkowski", wiek=30, miasto="szczecin")


def przywitaj_sie_z_kwargs(imie, nazwisko, *moje_args, **moje_kwargs):
    print(imie)
    print(nazwisko)
    print(moje_args)
    print(moje_kwargs)


przywitaj_sie_z_kwargs("jan", "kowalski", 1, 2, 3)
