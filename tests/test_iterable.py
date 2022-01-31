from ast import Num
from operator import add, mul
from itermethodchain import IterMethodChain as imc

def even(n: int) -> bool:
    return n % 2 == 0


def double(n: int) -> int:
    return n * 2


def next(n: int) -> int:
    return n + 1


def test_filter():
    assert imc(range(10)).filter(lambda n: n % 2 == 0).list() == [0, 2, 4 ,6, 8]


def test_filter2():    
    assert imc(range(10)).filter(even).list() == [0, 2, 4, 6, 8]


def test_map():
    assert imc(range(10)).map(lambda n: n * 2).list() == [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]


def test_map2():
    assert imc(range(10)).map(double).list() ==  [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]


def test_map_filter():
    assert (
        imc(range(10)).
        filter(lambda n: n % 2 == 0)
        .map(lambda n: n * 2).list()
        ) == [0, 4, 8, 12, 16]


def test_map_filter2():
    assert imc(range(10)).filter(even).map(double).list() == [0, 4, 8, 12, 16]


def test_reduce():
    assert imc(range(10)).reduce(add) == 45


def test_product():
    assert imc(range(10)).map(lambda n: n + 1).reduce(mul) == 3628800


def test_product2():
    assert imc(range(10)).map(next).reduce(mul) == 3628800
