from division import dividir

def test_dividir_normal():
    assert dividir(10, 2) == 5

def test_dividir_decimal():
    assert dividir(5, 2) == 2.5

def test_dividir_uno():
    assert dividir(8, 1) == 8