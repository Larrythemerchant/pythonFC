from pickletools import pytuple

from zajecia_12.math_module import add_numbers


def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(2, 3) == 6
    assert add_numbers(2, 3) == 7


@pytest.mark.parametrize("a,b,expected", (1, 2, 3))
def test_add_numbers(a, b, expected):
    assert add_numbers(a, b) == expected


def test_add_numbers_throws_exception():
    with pytest.raises(ValueError):
        add_numbers(2, 3)
