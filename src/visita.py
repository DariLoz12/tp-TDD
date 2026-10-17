def calcular_visita(zona, trabajo_mismo_dia, es_fin_de_semana):

    if zona == "centrica":
        visita = 8000
    elif zona == "periferica":
        visita = 12000
    elif zona == "fuera_ciudad":
        visita = 18000
    
    if es_fin_de_semana == True:
        visita = visita + (visita * 0.5)
    
    if trabajo_mismo_dia == True:
        visita = 0

    return visita