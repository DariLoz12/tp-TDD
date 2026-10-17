import pytest
from src.visita import calcular_visita

def test_centrica_sin_trabajo_semana():
    assert calcular_visita("centrica", False, False) == 8000

def test_periferica_sin_trabajo_semana():
    assert calcular_visita("periferica", False, False) == 12000

def test_fuera_ciudad_sin_trabajo_semana():
    assert calcular_visita("fuera_ciudad", False, False) == 18000

def test_cualquier_zona_trabajo_mismo_dia():
    assert calcular_visita("centrica", True, False) == 0

def test_centrica_fin_de_semana():
    assert calcular_visita("centrica", False, True) == 8000 + (8000 * 0.5)

def test_periferica_fin_de_semana_trabajo_mismo_dia():
    assert calcular_visita("periferica", True, True) == 0

def test_zona_inexistente():
    with pytest.raises(ValueError):
        calcular_visita("marte", False, False)