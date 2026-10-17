from src.visita import calcular_visita

def test_centrica_sin_trabajo_semana():
    assert calcular_visita("centrica", False, False) == 8000

def test_periferica_sin_trabajo_semana():
    assert calcular_visita("periferica", False, False) == 12000