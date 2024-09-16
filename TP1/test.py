import pytest
import fonctions as f

def test_puissance_basiques():
    assert f.puissance(2, 3) == 8
    assert f.puissance(2, 2) == 4

def test_puissance_base_negative():
    assert f.puissance(-2, 3) == -8  
    assert f.puissance(-2, 2) == 4   
    assert f.puissance(-2, 0) == 1   

def test_puissance_exposant_negatif():
    with pytest.raises(ValueError):
        f.puissance(2, -2)  

def test_puissance_base_zero():
    assert f.puissance(0, 5) == 0     
    assert f.puissance(0, 0) == 1     
def test_puissance_exposant_zero():
    assert f.puissance(5, 0) == 1     
def test_puissance_valeurs_larges():
    assert f.puissance(10, 6) == 1000000  
    assert f.puissance(2, 20) == 1048576  

def test_puissance_base_non_entier():
    with pytest.raises(TypeError):
        f.puissance(2.5, 3)  

def test_puissance_exposant_non_entier():
    with pytest.raises(TypeError):
        f.puissance(2, 3.5)  

def test_puissance_base_zero_exposant_negatif():
    with pytest.raises(ZeroDivisionError):
        f.puissance(0, -1)

