from typing import List, Union, TypedDict, Optional


class Osoba(TypedDict):
    imie: str
    nazwisko: str
    wiek: str
    plec: Optional[str] = None


imie: str = "jan"
imiona: List[str] = ["jan", "ewa"]


def zwieksz_moj_wiek_o_wybrana_liczbe(moj_wiek: int, wybrana_liczbe: int) -> int | None:
    x = moj_wiek / wybrana_liczbe
    return moj_wiek + wybrana_liczbe


# zwieksz_moj_wiek_o_wybrana_liczbe("osiemniascie", 2)
