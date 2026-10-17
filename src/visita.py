def calcular_visita(zona, trabajo_mismo_dia, es_fin_de_semana):
    if trabajo_mismo_dia == True:
        return 0
    else:
        if zona == "periferica":
            return 12000
        elif zona == "centrica":
            return 8000
        return 18000