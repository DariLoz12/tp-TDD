def calcular_visita(zona, trabajo_mismo_dia, es_fin_de_semana):
    precios = {
        "centrica": 8000,
        "periferica": 12000,
        "fuera_ciudad": 18000
    }
    
    if zona not in precios:
        raise ValueError("La zona ingresada no existe")
        
    if trabajo_mismo_dia:
        return 0
        
    visita = precios[zona]
    
    if es_fin_de_semana:
        visita += visita * 0.50
        
    return visita